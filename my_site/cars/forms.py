from django import forms

class ReviewForm(forms.Form) :
    first_name = forms.CharField(label='First name', max_length=100)
    last_name = forms.CharField(label='Last name', max_length=100, 
                                widget=forms.TextInput(attrs={'class':'myform'}))
    email = forms.EmailField(label='Email')
    review = forms.CharField(label='Please write your review here.',
                             widget=forms.Textarea(attrs={'class':'myform', 'rows':'2', 
                                                          'cols':'50'}))