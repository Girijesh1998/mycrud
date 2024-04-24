from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model= Student
        fields = ['id','fname','lname','roll','mobile','email']
        widgets = {
        'id'   :forms.NumberInput(),
        'fname':forms.TextInput(attrs={'class':'form-control'}),
        'lname':forms.TextInput(attrs={'class':'form-control'}),
        'roll' :forms.TextInput(attrs={'class':'form-control'}),
        'mobile':forms.NumberInput(attrs={'class':'form-control'}),
        'email':forms.EmailInput(attrs={'class':'form-control'}),   
        }
    
