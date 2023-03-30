from django import forms


class AddContact(forms.Form):
    name = forms.CharField(label='Full Name', max_length=200)
    number = forms.IntegerField(label='Phone Number')
    email = forms.EmailField(label='Email Address', max_length=200)
    relation = forms.CharField(label='Relationship', max_length=200)
