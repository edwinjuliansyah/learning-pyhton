from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    html = """
        <html>
        <head>
        </head>
        <body style="background-color:black;">
        <h1 style="color: white; text-align: center;">Warkop Emun</h1>
        </body>
        </html>


    """
    return HttpResponse(html)