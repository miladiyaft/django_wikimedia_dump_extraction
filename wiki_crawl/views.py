from django.shortcuts import render
from django.http import HttpResponse


def main(request):
    return HttpResponse("Go to other end points...")

def save_data(request):
    
    print("Salam")
    return HttpResponse("salllllllllllam")

