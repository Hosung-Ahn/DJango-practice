from django import forms
from .models import Review
from django.forms import ModelForm

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
        
