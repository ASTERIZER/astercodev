from django.shortcuts import render
from django.views.generic import TemplateView

# Class based view
class home(TemplateView):
    template_name = 'base.html'

# Function based view
# def home(request):
#     return render(request, template_name='base.html')