"""drugfind URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings #add
from django.conf.urls.static import static #add

urlpatterns = [
    path('', views.index, name='Home | Neo-Bhesard'),
    path('PredictDrugClass/', views.upload, name='Predict Drug Class | Neo-Bhesard'),
    path('AboutUs/', views.about, name='About Us | Neo-Bhesard'),
    path('DrugLists/', views.druglists, name='Drug Lists | Neo-Bhesard'),
    path('ContactTeam/', views.contact, name='Contact Team | Neo-Bhesard')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #add
#urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
