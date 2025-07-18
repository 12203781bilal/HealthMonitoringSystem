from django import forms
from .models import VitalRecord, Feedback


class VitalRecordForm(forms.ModelForm):
    class Meta:
        model = VitalRecord
        fields = [
            'systolic',
            'diastolic',
            'heart_rate',
            'temperature',
            'sugar_level'
        ]
        widgets = {
            'systolic': forms.NumberInput(attrs={'class': 'form-control'}),
            'diastolic': forms.NumberInput(attrs={'class': 'form-control'}),
            'heart_rate': forms.NumberInput(attrs={'class': 'form-control'}),
            'temperature': forms.NumberInput(attrs={'class': 'form-control'}),
            'sugar_level': forms.NumberInput(attrs={'class': 'form-control'}),
        }




class PatientLoginForm(forms.Form):
    username = forms.CharField(
        label="Patient Name",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        label="Password (Floor+Room+Bed)",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )



class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['message']
        widgets = {
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Write your feedback...'
            })
        }
