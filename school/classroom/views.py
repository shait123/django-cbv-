from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from classroom.forms import ContactForm  # Import the form class

class HomeView(TemplateView):
    template_name = 'classroom/home.html'

class ThankYouView(TemplateView):
    template_name = 'classroom/thankyou.html'

class ContactFormView(FormView):
    form_class = ContactForm  # Use the correct form class
    template_name = 'classroom/contact.html'
    success_url = "/classroom/thank_you/"

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
