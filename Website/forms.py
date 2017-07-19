from django import forms


class ContactForm(forms.Form):
    Name = forms.CharField(required = True, label= ("Name"),
            widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    from_email = forms.EmailField(required = True, label= ("Email"),
            widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    subject = forms.CharField(required = True, label= ("Subject"),
            widget=forms.TextInput(attrs={'placeholder': 'Subject'}))

    message = forms.CharField(required=True, label= ("Message"),
            widget=forms.Textarea(attrs={'placeholder': 'Message'}))


