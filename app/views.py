from django.shortcuts import render
from django.views import View
from django.http import request
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import BookCreateForm

# Create your views here.


class PanelView(View):
    def get(self, request):
        return render(request, 'panel.html')


class BookCreateFormView(View):
    def get(self, request):
        return render(request, 'book_create_form.html')
