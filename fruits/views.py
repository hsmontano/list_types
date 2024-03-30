from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
import re

def home(request):
    print(f"{request}")
    return HttpResponse("Hello world from Django")

# Create your views here.

def hello_there(request, name):
    now = datetime.now()
    formatted_now = now.strftime("%a, %d %b, %Y at %X")

    # Filter the name argument to letters only using regular expressions. URL arguments
    # can contain arbitrary text, so we restrict to safe characters only.
    match_object = re.match("[a-zA-Z]+", name)

    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Friend"

    content = "Hello there, " + clean_name + "! It's " + formatted_now
    return HttpResponse(content)