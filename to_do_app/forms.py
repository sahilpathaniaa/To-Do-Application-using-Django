from django import forms
from . models import Task



class TaskCreate(forms.ModelForm): 
    class Meta:
        model = Task
        fields = ( 'title', 'description', 'dueDate', 'status')

        widgets = {
        'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Add Title '}),
        'description': forms.Textarea(attrs={'class':'form-control', 'rows':3, 'placeholder':"Add description ..."}),
        'dueDate': forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
        'status': forms.Select(attrs={'class':'form-control'}),
            
        }
