from django import forms
from .models import Review
from django.forms import ModelForm

# class ReviewForm(forms.Form) :
#     first_name = forms.CharField(label='First name', max_length=100)
#     last_name = forms.CharField(label='Last name', max_length=100, 
#                                 widget=forms.TextInput(attrs={'class':'myform'}))
#     email = forms.EmailField(label='Email')
#     review = forms.CharField(label='Please write your review here.',
#                              widget=forms.Textarea(attrs={'class':'myform', 'rows':'2', 
#                                                           'cols':'50'}))

class ReviewForm(ModelForm) :
    class Meta :
        model = Review
        fields = "__all__"
        
        labels= {
            'first_name':'your first name',
            'last_name':'Last name',
            'stars':'Rating',
        }
        
        error_messages = {
            'stars' : {
                'min_value' : "Min value is 1",
                'max_value' : "Max value is 5",
            }
        }
        
