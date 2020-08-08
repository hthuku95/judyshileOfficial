from django import forms

class ContactForm(forms.Form):
    firstname = forms.CharField(label='', max_length=100 ,widget=forms.TextInput(attrs={'class':'text-input','placeholder':'firstname'}))
    lastname = forms.CharField(label='', max_length=100,widget=forms.TextInput(attrs={'class':'text-input','placeholder':'lastname'}))
    email = forms.EmailField( label='',max_length=100 ,widget=forms.EmailInput(attrs={'class':'text-input','placeholder':'email'}))
    message = forms.CharField( label='',widget=forms.Textarea(attrs={'class':'text-message','placeholder':'message'}))

