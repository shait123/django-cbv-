from django.urls import path
from .views import HomeView, ThankYouView, ContactFormView  # Import ContactFormView

app_name = 'classroom'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('thank_you/', ThankYouView.as_view(), name='thank_you'),
    path('contact/', ContactFormView.as_view(), name='contact')  # Correct usage of ContactFormView
]
