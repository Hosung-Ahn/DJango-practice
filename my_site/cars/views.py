from django.shortcuts import render, redirect
from django.urls import reverse
from . import forms
from .models import Review

# Create your views here.
def rental_review(request) :

    if request.method == 'POST' :
        form = forms.ReviewForm(request.POST)
        if form.is_valid() :
            review = Review.objects.create(first_name=form.cleaned_data['first_name'],
                                           last_name=form.cleaned_data['last_name'],
                                           stars=form.cleaned_data['stars'])
            return redirect(reverse('cars:thank_you'))
        
    else :
        form = forms.ReviewForm()
    return render(request, 'cars/rental_review.html', context={'form':form})

def thank_you(request) :
    return render(request, 'cars/thank_you.html')