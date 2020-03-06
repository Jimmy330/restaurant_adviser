from django import forms
from django.contrib.auth.models import User
from rest_adv.models import UserProfile,Review

class ReviewForm(forms.ModelForm):
    rate = forms.IntegerField()
    message = forms.CharField()
    class Meta:
        model = Review
        fields = ('rate', 'message',)


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture',)