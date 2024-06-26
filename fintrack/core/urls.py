from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name = "home"),
	path('property/', views.property, name = "property"),
	path('property_single', views.property_single, name = 'property_single'),
	path('contact', views.contact, name='contact'),
	path('blog_grid', views.blog_grid, name='blog_grid'),
	path('blog_single', views.blog_single, name='blog_single'),
	path('agent_single', views.agent_single, name='agent_single'),
	path('agents_grid', views.agents_grid, name='agents_grid'),
]