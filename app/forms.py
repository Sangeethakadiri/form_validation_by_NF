from django import forms


def check_for_a(value):
    if value[0]=='a':
        raise forms.ValidationError('name start with a')


def check_for_len(value):
    if len(value)<3:
        raise forms.ValidationError('len is less')

class StudentForm(forms.Form):
    name=forms.CharField(max_length=100,validators=[check_for_a,check_for_len])
    age=forms.IntegerField()
    email=forms.EmailField()