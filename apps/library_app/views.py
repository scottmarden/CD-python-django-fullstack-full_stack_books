# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import Book

# Create your views here.
def index(request):
	books = Book.objects.all()
	print books
	context = {
		'books': books
	}
	return render(request, 'library_app/index.html', context)

def add_book(request):
	if request.method=='POST':
		Book.objects.create(title=request.POST['title'], author=request.POST['author'], category=request.POST['category'])
	return redirect('/')
