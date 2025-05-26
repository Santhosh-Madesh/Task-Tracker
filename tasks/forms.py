from django import forms

class TaskForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField(widget=forms.Textarea())
    deadline = forms.DateField(widget=forms.SelectDateWidget())