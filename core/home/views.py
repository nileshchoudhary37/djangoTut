from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    peoples =[
        {'name': "Abhijeet G", 'age' : 26},
        {'name': "Rohan", 'age' : 23},
        {'name': "Vicky ", 'age' : 17},
        {'name': "Deepanshu", 'age' : 16},
        {'name': "Sandeep", 'age' : 63},
    ]
    text = """Lorem ipsum dolor sit amet consectetur adipisicing elit. Illo reprehenderit cupiditate sunt aliquid praesentium molestias ullam nam dolore possimus sed sequi blanditiis quisquam, labore est, distinctio corrupti libero! Ullam officia excepturi nihil?"""
    return render(request, 'dome/index.html', context = {'page' : 'home', 'peoples' : peoples, 'text' : text})

def about(request):
    context = {'page' : 'About'}
    return render(request, 'dome/about.html', context )
def contact(request):
    context = {'page' : 'Contact'}
    return render(request, 'dome/contact.html', context )

# Create your views here.