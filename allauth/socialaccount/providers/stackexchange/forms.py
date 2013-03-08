from django import forms

class StackExchangeConnectForm(forms.Form):
    access_token = forms.CharField(required=True)
