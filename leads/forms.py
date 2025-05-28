from django import forms
from .models import FollowUp

class FollowUpForm(forms.ModelForm):
    follow_up_date = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
        input_formats=['%Y-%m-%dT%H:%M']
    )

    class Meta:
        model = FollowUp
        fields = ['comment', 'follow_up_date'] 