from django.urls import path
from .views import RegistrationView, LoginView, LoginGuestView, LogoutView


urlpatterns = [
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('login/', LoginView.as_view(), name='login'),
    path('loginguest/', LoginGuestView.as_view(), name='loginguest'),
    path('logout/', LogoutView.as_view(), name='logout'),
]