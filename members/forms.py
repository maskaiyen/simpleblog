from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms

# class SignInForm(UserCreationForm):
#     username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
#     password = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
#     class Meta:
#         model = User
#         fields = ('username', 'password')
#
#         # widgets = {
#         #     'username': forms.TextInput(attrs={'class': 'form-control'},),
#         #     'password': forms.PasswordInput(attrs={'class': 'form-control'}, ),
#         #     # 'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
#         # }
#     def __init__(self, *args, **kwargs):
#         super(SignInForm, self).__init__(*args, **kwargs)
#
#         self.fields['username'].widget.attrs['class'] = 'form-control'
#         self.fields['password'].widget.attrs['class'] = 'form-control'

class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2') # register page 的順序

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

class EditProfileForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = None # UserChangeForm does include password field, so need to override it. Then the form would exclude it.
    # password = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'})),
    last_login = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # is_superuser = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    # is_groups = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    # is_user_permissions = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # is_stuff = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    # is_active = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))

    class Meta:
        model = User
        # fields = ('username', 'first_name', 'last_name', 'email', 'last_login', 'is_superuser',
        #           'is_stuff', 'is_active')
        fields = ('username', 'first_name', 'last_name', 'email', 'last_login')

class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(label=("Old password"), widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
    new_password1 = forms.CharField(label=("New password"), max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
    new_password2 = forms.CharField(label=("New password confirmation"), max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')