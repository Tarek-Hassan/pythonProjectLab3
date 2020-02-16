from django import forms
from app1.models import Student,Track

class TrackForm(forms.ModelForm):
        class Meta:
                model=Track
                fields=('trackName',)

class StudentForm(forms.ModelForm):
        class Meta:
                model=Student
                fields=('fname','lname','age','studentTrack',)            
                widgets={
                'fname':forms.TextInput(attrs={'class':'form-control'}),
                'lname':forms.TextInput(attrs={'class':'form-control'}),
                'age':forms.TextInput(attrs={'class':'form-control'}),
                # 'studentTrack':forms.TextInput(attrs={'class':'form-control'})

        }