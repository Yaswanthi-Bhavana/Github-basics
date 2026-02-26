from django.shortcuts import render
colleges={
            'svecw':'shri',
            'vit':'vishnu'
        }

# Create your views here.
def project(request):
    return render(request,"project.html",{
        "clg":colleges,
        })

