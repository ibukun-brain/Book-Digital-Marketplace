from django import forms
from django.contrib.auth.forms import UserCreationForm
from home.models import CustomUser


class SignupForm(UserCreationForm):
    first_name = forms.CharField(
        label="First name",
        widget=forms.TextInput(
            attrs={
                'placeholder': 'First name',
                'required': True,
            }
        )
    )
    last_name = forms.CharField(
        label="Last name",
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Last name',
                'required': True,
            }
        )
    )
    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Password'
            }
        ),
    )
    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Confirm Password'
            }
        ),
        strip=False,
    )
    class Meta:
        model = CustomUser
        fields = [
                'first_name',
                'last_name',
                'email',
                'username',
                'password1',
                'password2'
            ]

        help_texts = {
                    "username":""
                }

        widgets = {  
            'email': forms.EmailInput(
                attrs={
                'placeholder': 'Email address',
            }),
            'username': forms.TextInput(
                attrs={
                'placeholder': 'Username',
            }),
        }

    # def __init__(self, *args, **kwargs):
    #     super(RegistrationForm, self).__init__(*args, **kwargs)
    #     for name, field in self.fields.items():
    #         # print(field.widget)
    #         if name == "first_name":
    #             field.widget.attrs.update({'placeholder':'First Name'})
    #             field.required = True
    #         elif name == "last_name":
    #             field.widget.attrs.update({'placeholder':'Last Name'})
    #             field.required = True

    #         elif name == "email":
    #             field.widget.attrs.update({'placeholder':'Email Address'})
    #         elif name == "username":
    #             field.widget.attrs.update({'placeholder':'Username'})
    #         elif name == "password1":
                # field.widget.attrs.update({'placeholder':'Password'})
            # elif name == "password2":
                # field.widget.attrs.update({'placeholder':'Confirm Password'})
            