from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

from .forms import UserLoginForm
from .views import (account_register,
                    account_activate,
                    dashboard,
                    edit_details,
                    delete_user,)

app_name = 'account'
urlpatterns = [
    path('login/',auth_views.LoginView.as_view(template_name='account/registration/login.html',
                                               form_class=UserLoginForm), name='login'),
    path('logout/',auth_views.LogoutView.as_view(next_page='/account/login/'), name='logout'),
    path('register/',account_register,name='register'),
    path('activate/<slug:uidb64>/<slug:token>/', account_activate, name='activate'),
    path('dashboard/', dashboard, name='dashboard'),
    path('profile/edit/', edit_details, name='edit_details'),
    path('profile/delete_user/', delete_user, name='delete_user'),
    path('profile/delete_confirm', TemplateView.as_view(template_name='account/user/delete_confirm.html'),name='delete_confirmation')
]