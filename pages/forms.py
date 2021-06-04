from clients.models import Client
from django import forms


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('first_name', 'last_name')

        CHOICES = (
            ('M', 'Male'),
            ('F', 'Female'),
            ('O', 'Other')
        )

        widgets = {
            # 'business_owner': forms.Select(),
            # 'agent': forms.Select(),
            'first_name': forms.TextInput(),
            'last_name': forms.TextInput(),
            # 'birthdate': forms.DateTimeField(),
            # 'email': forms.EmailField(),
            # 'phone_number': forms.TextInput(),
            # 'address': forms.TextInput(),
            # 'gender': forms.Select(),
            # 'profile_picture': forms.ImageField()
        }
