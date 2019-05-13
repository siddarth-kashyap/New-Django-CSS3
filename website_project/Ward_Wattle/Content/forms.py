from django import forms

class ContactForm(forms.Form):
    contact_name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'field'}), required=True, max_length=30 )
    from_email = forms.EmailField(widget=forms.TextInput(attrs={'class' : 'field'}), required=True)
    subject = forms.CharField(widget=forms.TextInput(attrs={'class' : 'field'}), required=True, max_length=120)
    message = forms.CharField(widget=forms.Textarea(attrs={'class' : 'field4'}), required=True)
    

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['contact_name'].label = "Full Name: "
        self.fields['from_email'].label = "E-Mail ID:  "
        self.fields['subject'].label = "  Subject---:    "
        self.fields['message'].label = "Message :-"
