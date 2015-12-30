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
            recipient_list=['contacto.gigosoft@gmail.com'],
        )
        return super(ContactFormView, self).form_valid(form)

def contact(request):
    contact_form = ContactFormView()
    return render(request, 'Contacto.html', {'contact_form': contact_form})

#def contacto(request):
#    if request.method=='POST':
#        form = ContactForm(request.POST)
#        if form.is_valid():
#            subject = form.cleaned_data['subject']
#            message = form.cleaned_data['message']
#            sender = form.cleaned_data['sender']
#            cc_myself = form.cleaned_data['cc_myself']
#            recipients = ['info@example.com']
#            if cc_myself:
#                recipients.append(sender)
#            send_mail(subject, message, sender, recipients)
#            return HttpResponseRedirect('/')
#    else:
#        formulario = ContactForm()
#    return render(request, 'Contacto.html', {'formulario':formulario})

