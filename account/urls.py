from django.urls import path
from django.contrib.auth import views as auth_views

from .forms import UserLoginForm
from .views import account_register, account_activate,dashboard

app_name = 'account'
urlpatterns = [
    path('login/',auth_views.LoginView.as_view(template_name='account/registration/login.html',
                                               form_class=UserLoginForm), name='login'),
    path('register/',account_register,name='register'),
    path('activate/<slug:uidb64>/<slug:token>/',account_activate,name='activate'),
    path('dashboard/', dashboard, name='dashboard'),
]