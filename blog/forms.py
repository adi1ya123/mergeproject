from django import forms
from .models import User

from .models import Post, Category, Tag, Comment


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text', 'category', 'tag', 'featured_image', 'thumbnail_image')

class UserForm(forms.ModelForm):
    password1 =forms.CharField(widget=forms.PasswordInput)
    password2 =forms.CharField(widget=forms.PasswordInput, label='confirm password')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.validationError("password do not match")
        return password2

    class Meta:
        model = User
        fields = ['username', 'image', 'first_name', 'last_name', 'gender', 'password1', 'password2', 'phone_no','email', ]

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']

class ProfileForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'image', 'first_name', 'last_name', 'gender', 'phone_no', 'email', ]

class ProfileEditForm(forms.ModelForm):
                
    class Meta:
        model = User
        fields = ['username', 'image', 'first_name', 'last_name', 'gender', 'phone_no', 'email', ]

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ['name','email','text']
                
        

