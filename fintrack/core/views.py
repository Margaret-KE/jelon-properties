from django.shortcuts import render

# Create your views here.
def home(request):
	return render (request, 'index.html')

def property(request):
	return render(request , 'property-grid.html')

def property_single(request):
	return render(request, 'property-single.html')

def contact(request):
	return render(request, 'contact.html')

def blog_grid(request):
	return render(request, 'blog-grid.html')

def blog_single(request):
	return render(request, 'blog-single.html')

def agent_single(request):
	return render(request, 'agent-single.html')

def agents_grid(request):
	return render(request, 'agents-grid.html')