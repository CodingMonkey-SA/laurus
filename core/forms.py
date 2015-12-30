from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class ContactForm(forms.Form):

    name = forms.CharField(
        label = "Nombre:",
        max_length = 80,
        required = True,
    )

    email = forms.EmailField(
        label = "EMail:",
        max_length = 80,
        required = True,
    )

    subject = forms.CharField(
        label = "Asunto:",
        max_length = 80,
        required = True,
    )

    message = forms.CharField(
        widget = forms.Textarea,
        label = "Mensaje:",
        required = True,
    )

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('send', 'Enviar'))
