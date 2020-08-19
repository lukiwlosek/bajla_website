from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'base.html')

def ideas(request):
    return render(request, 'ideas.html')

def planning(request):
    return render(request, 'planning.html')

def video(request):
    return render(request, 'video.html')

def final(request):
    return render(request, 'final.html')
def second(request):
    return render(request, 'second_idea.html')
def third(request):
    return render(request, 'third_idea.html')