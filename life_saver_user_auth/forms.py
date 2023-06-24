from django import forms
from life_saver_user_auth.models import User, Contact

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'