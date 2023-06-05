from django import forms


# create a user registration form
class UserRegForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    id_name = forms.CharField()
    date_of_birth = forms.CharField()
    password = forms.CharField()