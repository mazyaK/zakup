from django.urls import path
from django.contrib.auth import views as login_logout_views
from . import views as custom_views

app_name = 'accounts'
urlpatterns = [
    path('login/', custom_views.CustomLoginView.as_view(), name='login'),
    path('logout/', login_logout_views.LogoutView.as_view(), name='logout'),
    path('registration/', custom_views.RegistrationView.as_view(), name='registration'),
    path('profile/<slug:slug>/', custom_views.ProfileDetailView.as_view(), name='profile_detail'),
    path('profile/<slug:slug>/edit/', custom_views.ProfileUpdateView.as_view(), name='profile_edit'),
]