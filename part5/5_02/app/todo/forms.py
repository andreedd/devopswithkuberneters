from django import forms

class TodoForm(forms.Form):
    todo = forms.CharField(label='Todo', max_length=140)