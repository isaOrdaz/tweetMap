from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    template = loader.get_template("/Users/aaronyanes/tweetMap/index.html")
    return HttpResponse(template.render())




    
