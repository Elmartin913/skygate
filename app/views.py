from django.shortcuts import render
from django.views import View
from django.http import request

# Create your views here.


class PanelView(View):
    def get(self, request):
        return render(request, 'panel.html')
