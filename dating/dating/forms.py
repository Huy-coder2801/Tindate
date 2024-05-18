from django import forms

class UserSearchForm(forms.Form):
    query = forms.CharField(widget=forms.TextInput(attrs={
        'id': "query",
        'placeholder': 'Typing information user search',
        'class': 'w-100 py-2 px-4 rounded'
    }))