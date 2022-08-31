from django.shortcuts import render
from .models import Patient

# Create your views here.
def list_patient(request) :
    all_patient = Patient.objects.all()
    context_list = {"patients" : all_patient}
    return render(request, "model/list.html", context=context_list)