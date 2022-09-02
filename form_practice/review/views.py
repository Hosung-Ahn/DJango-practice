from django.shortcuts import render, redirect
from django.urls import reverse
from . import forms
from .models import Review

# Create your views here.


def start(request) :
    if request.method == 'POST' :
        form = forms.ReviewForm(request.POST)
        if form.is_valid() :
            data = form.cleaned_data
            Review.objects.create(first_name=data['first_name'],
                                  last_name=data['last_name'],
                                  stars=data['stars'])
            return redirect(reverse("review:end"))
            
    form = forms.ReviewForm()
    return render(request, 'review/start.html', context={'form':form})

def end(request) :
    all_reviews = Review.objects.all()
    return render(request, 'review/end.html', context={'all_reviews':all_reviews})