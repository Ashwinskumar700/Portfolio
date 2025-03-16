from django.shortcuts import render,redirect
from .models import Project, Experience
from .forms import ContactForm

def home(request):
    return render(request, 'portfolio/home.html')

def about(request):
    return render(request, 'portfolio/about.html')

def skills(request):
    return render(request, 'portfolio/skills.html')

def education(request):
    return render(request, 'portfolio/education.html')

def projects(request):
    projects = Project.objects.all()  # Fetch all projects
    return render(request, 'portfolio/projects.html', {'projects': projects})

def certifications(request):
    return render(request, 'portfolio/certifications.html')

def experience(request):
    experiences = Experience.objects.all()
    return render(request, 'portfolio/experience.html', {'experiences': experiences})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Save data to the database
            return redirect('home')  # Redirect to home after saving
    else:
        form = ContactForm()
    return render(request, 'portfolio/contact.html', {'form': form})