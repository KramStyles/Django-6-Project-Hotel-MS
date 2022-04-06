from django import forms


class QueryForm(forms.Form):
    check_in = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    check_out = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    min_price = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    max_price = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
