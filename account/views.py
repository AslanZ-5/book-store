import imp
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponseRedirect
from django.utils.http import  urlsafe_base64_encode,urlsafe_base64_decode
from django.shortcuts import redirect, render
from django.utils.encoding import force_bytes, force_str 
from django.template.loader import render_to_string
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .token  import account_activation_token
from .forms import RegistrationForm, UserEditForm, UserAddressForm
from .models import Customer, Address
from orders.views import user_orders

@login_required
def dashboard(request):
    orders = user_orders(request)
    return render(request,'dashboard.html',{'orders':orders})

@login_required
def edit_details(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)

        if user_form.is_valid():
            user_form.save()
    else:
        user_form = UserEditForm(instance=request.user)

    return render(request,
                  'edit_details.html', {'user_form': user_form})

@login_required
def delete_user(request):
    user = Customer.objects.get(user_name=request.user)
    user.is_active = False
    user.save()
    logout(request)
    return redirect('account:delete_confirmation')



def account_register(request):

    if request.user.is_authenticated:
        return redirect('/')
    
    if request.method == 'POST':
        registerForm = RegistrationForm(request.POST)
        if registerForm.is_valid():
            user = registerForm.save(commit=False)
            user.email = registerForm.cleaned_data['email']
            user.set_password(registerForm.cleaned_data['password'])
            user.is_active = False
            user.save()
            # Setup email
            current_site = get_current_site(request)
            subject = "Activate your Account"
            message = render_to_string('account_activation_email.html',{
                'user':user,
                'domain':current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject=subject, message=message)
            return render(request, 'register_confirm.html')
    else:
        registerForm = RegistrationForm()
    
    return render(request, 'register.html', {'form': registerForm})


def account_activate(request,uidb64,token):

    uid = force_str(urlsafe_base64_decode(uidb64))
    user = Customer.objects.get(pk=uid)
    
    if user is not None and account_activation_token.check_token(user,token):
        user.is_active = True
        user.save()
        login(request,user)
        return redirect('account:dashboard')
    else:
        return render(request,'activation_invalid.html')
    

# Adresses
@login_required
def view_address(request):
    addresses = Address.objects.filter(customer=request.user)
    return render(request, "adresses.html", {'addresses':addresses})

@login_required
def add_address(request):
    if request.method == "POST":
        address_form = UserAddressForm(data=request.POST)
        if address_form.is_valid():
            address_form = address_form.save(commit=False)
            address_form.customer = request.user
            address_form.save()
            return HttpResponseRedirect(reverse("account:addresses"))
    else:
        address_form = UserAddressForm()
    return render(request, "edit_address.html", {"form":address_form})