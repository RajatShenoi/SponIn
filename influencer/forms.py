from typing import Any
import uuid
from django import forms
from main.models import MyUser
from django.contrib.auth.forms import UserCreationForm

class InfluencerRegistrationForm(UserCreationForm):
    category = forms.CharField(max_length=100)
    niche = forms.CharField(max_length=100)
    reach = forms.IntegerField()

    class Meta:
        model = MyUser
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'profile_picture']

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.fields['profile_picture'].widget.attrs.update({'class': 'grow file-input file-input-bordered w-full'})   
    
    def save(self, commit=True):
        instance = super().save(commit=False)
        if 'profile_picture' in self.cleaned_data and self.cleaned_data['profile_picture']:
            file = self.cleaned_data['profile_picture']
            ext = file.name.split('.')[-1]
            unique_filename = f"{uuid.uuid4()}.{ext}"
            file.name = unique_filename
            instance.profile_picture = file
        if commit:
            instance.save()
        return instance