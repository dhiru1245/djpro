from django import forms


class  RegistrationForm(forms.Form):
    first_name = forms.CharField(
        label= 'Enter first name',
        widget= forms.TextInput(
            attrs= {
                'class':'form-control',
                'placeholder':'enter  first name'
            }
        )
    )

    last_name = forms.CharField(
        label='Enter  last name',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'enter  last name'
            }
        )
    )

    user_name = forms.CharField(
        label='Enter uer name',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'enter user  name'
            }
        )
    )

    password = forms.CharField(
        label='Enter password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'enter password'
            }
        )
    )
    email = forms.CharField(
        label='Enter email',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'enter email'
            }
        )
    )

    number = forms.IntegerField(
        label='Enter mob number',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'enter number'
            }
        )
    )


class LoginForm(forms.Form):
    user_name = forms.CharField(
        label='Enter uer name',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'enter user  name'
            }
        )
    )

    password = forms.CharField(
        label='Enter password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'enter password'
            }
        )
    )