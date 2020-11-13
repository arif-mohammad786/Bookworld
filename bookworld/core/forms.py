from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django.utils.translation import gettext,gettext_lazy as _
from .models import book_category,available_book,buy_book_model

class signupform(UserCreationForm):
    password1=forms.CharField(label='Password',label_suffix=" ",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(label='Password Confirmation(again)',label_suffix=" ",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
        labels={'username':'Username','first_name':'First Name','last_name':'Last Name','email':'Email'}
        widgets={
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'})
        }
        


class loginform(AuthenticationForm):
    username=UsernameField(label_suffix=" ",widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'}))
    password=forms.CharField(label_suffix=" ",label=_("Password"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))


class book_category_form(forms.ModelForm):
    class Meta:
        model=book_category
        fields=['category']
        labels={'category':'Book Category'}
        widgets={'category':forms.TextInput(attrs={'class':'form-control'})}


class available_book_form(forms.ModelForm):
    class Meta:
        model=available_book
        fields=['title','author','publisher','category','price','image']
        labels={'title':'Book Title','author':'Book Author','publisher':'Publisher','category':'Category','price':'Price','image':'Upload Image'}
        widgets={'title':forms.TextInput(attrs={'class':'form-control'}),
            'author':forms.TextInput(attrs={'class':'form-control'}),
            'publisher':forms.TextInput(attrs={'class':'form-control'}),
            'category':forms.TextInput(attrs={'class':'form-control'}),
            'price':forms.NumberInput(attrs={'class':'form-control'}),
            'image':forms.FileInput(attrs={'class':'form-control'})
        }



class buy_book_form(forms.ModelForm):
    class Meta:
        model=buy_book_model
        fields=['title','author','publisher','category','name','phone','address']
        labels={'title':'Book Title','author':'Book Author','publisher':'Publisher','category':'Category','name':'Your Name','phone':'Phone No.','address':'Your Address'}
        widgets={'title':forms.TextInput(attrs={'class':'form-control'}),
            'author':forms.TextInput(attrs={'class':'form-control'}),
            'publisher':forms.TextInput(attrs={'class':'form-control'}),
            'category':forms.TextInput(attrs={'class':'form-control'}),
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'phone':forms.TextInput(attrs={'class':'form-control'}),
            'address':forms.Textarea(attrs={'class':'form-control','rows':3})
        }


class search_form(forms.Form):
    search=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Search Book'}))
