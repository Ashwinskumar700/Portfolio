from django.contrib import admin
from .models import Project, Experience
from .models import Contact

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'link', 'image')

admin.site.register(Project, ProjectAdmin)
admin.site.register(Experience)
admin.site.register(Contact)