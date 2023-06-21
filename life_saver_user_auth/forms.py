from django import forms
from life_saver_user_auth.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'