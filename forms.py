from django import forms
from .models import Etablissement, User

#Creation form Etablissement
class registrationForm_Et(forms.ModelForm):
    username = forms.CharField(max_length=150, required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    pwd = forms.CharField(required=True,max_length=100, widget=forms.PasswordInput(attrs={'class':'form-control'}))
    pwd_conf = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class':'form-control'}))
    address = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(required=True,max_length=100, widget=forms.EmailInput(attrs={'class':'form-control'}))
    city = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    description = forms.CharField(max_length=255, required=True,widget=forms.Textarea(attrs={'class':'form-control'}))
    image = forms.ImageField()
    cate = forms.CharField(max_length=25, required=True, widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = Etablissement
        fields = ['username', 'email', 'address',  'city' , 'description',  'pwd', 'pwd_conf','image', 'cate']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("pwd")
        password_confirm = cleaned_data.get("pwd_conf")
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Les mots de passe ne correspondent pas.")


class loginForm_Et(forms.Form):
    username = forms.CharField(label=" nom utilisateur ",max_length=150, widget=forms.TextInput(attrs={'class':'form-control'}))
    pwd = forms.CharField(label=" mot de pass ",max_length=16,widget=forms.PasswordInput(attrs={'class':'form-control'}))


#Creation form Utilisateur
class registrationForm_Us(forms.ModelForm):
    username = forms.CharField(max_length=150,  widget=forms.TextInput(attrs={'class':'form-control'}))
    pwd = forms.CharField(max_length=100, required=True, widget=forms.PasswordInput(attrs={'class':'form-control'}))
    pwd_conf = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class':'form-control'}))
    email = forms.EmailField(required=True,max_length=100, widget=forms.EmailInput(attrs={'class':'form-control'}))
    city = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    image = forms.ImageField()

    class Meta:
        model = User
        fields = ['username', 'email',  'city' ,  'pwd', 'pwd_conf','image']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("pwd")
        password_confirm = cleaned_data.get("pwd_conf")
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Les mots de passe ne correspondent pas.")
        
        
class loginForm_Us(forms.Form):
    username = forms.CharField(label=" nom utilisateur ",max_length=150, widget=forms.TextInput(attrs={'class':'form-control'}))
    pwd = forms.CharField(label=" mot de pass ",max_length=16,widget=forms.PasswordInput(attrs={'class':'form-control'}))



class ContactForm(forms.Form):
    full_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Votre nom complet',
        })
    )
    
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'votre@email.com',
        })
    )
    
    subject = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Sujet de votre message',
        })
    )
    
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 5,
            'placeholder': 'Votre message ici...',
        })
    )

