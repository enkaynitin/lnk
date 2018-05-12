from django import forms

# our new form

#
# class ContactForm(forms.Form):
#
#     contact_name = forms.CharField(required=True)
#     contact_email = forms.EmailField(required=True)
#     content = forms.CharField(
#         required=True,
#         widget=forms.Textarea
#     )
#

class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    subject = forms.CharField(required=False)
    content = forms.CharField(
        required=True,
        widget=forms.Textarea
    )

    # the new bit we're adding
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['contact_name'].label = "Name:"
        self.fields['contact_email'].label = "Email:"
        self.fields['subject'].label = "Subject:"
        self.fields['content'].label = "Message:"