"""
URL configuration for python28_2_first_month project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from posts.views import hello_view, now_date, good_bye, posts_view, main_page_view
from product.views import product_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello_view),
    path('now_date/', now_date),
    path('goodby/', good_bye),
    path('', main_page_view),
    path('posts/', posts_view),
    path('products/', product_view),
]
