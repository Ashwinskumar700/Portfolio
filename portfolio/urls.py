from django.urls import path
from .views import home, about, skills, education, projects, certifications, experience, contact

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('skills/', skills, name='skills'),
    path('education/', education, name='education'),
    path('projects/', projects, name='projects'),
    path('certifications/', certifications, name='certifications'),
    path('experience/', experience, name='experience'),
    path('contact/', contact, name='contact'),  # Ensure this exists
]
