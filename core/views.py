from django.shortcuts import render
from django.core.mail import send_mail
from core.forms import ContactForm
from django.views.generic.edit import FormView

def index(request):
    return render(request, 'Index.html', {})

def cervezas(request):
    return render(request, 'Cervezas.html', {})

class ContactFormView(FormView):

    form_class = ContactForm
    template_name = "Contacto.html"
    success_url = '/'

    def form_valid(self, form):
        message = "{name} / {email} said: ".format(
            name=form.cleaned_data.get('name'),
            email=form.cleaned_data.get('email'))
        message += "\n\n{0}".format(form.cleaned_data.get('message'))
        send_mail(
            subject=form.cleaned_data.get('subject').strip(),
            message=message,
            from_email='contacto.gigosoft@myapp.com',
            recipient_list=['simoncellisantiago@gmail.com'],
        )
        return super(ContactFormView, self).form_valid(form)

def contact(request):
    contact_form = ContactFormView()
    return render(request, 'Contacto.html', {'contact_form': contact_form})
