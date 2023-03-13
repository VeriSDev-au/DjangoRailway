from django.shortcuts import render
from django.http.response import HttpResponse
import os

# Create your views here.
def home(request):
    return HttpResponse(
        "Hello World, this is value from environment variable in Railway.App setting = "
        + os.environ.get("VSD_VAR_TEST")
    )
