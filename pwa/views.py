from django.http import HttpResponse
from django.template.loader import render_to_string

def service_worker(request):
    response = HttpResponse(
        render_to_string("serviceworker.js"), 
        content_type="application/javascript"
    )
    return response
