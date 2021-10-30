from django import forms


class CreateNewClient(forms.Form):
    name = forms.CharField(label="Name", max_length=200)
