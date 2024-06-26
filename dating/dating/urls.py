"""
URL configuration for dating project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from  .views import home_view, search_view, user_detail_view

from accounts import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name = 'home-view'),
 

    path('search/', search_view, name='search'),
    path('users/<int:pk>/', user_detail_view, name='user_detail'),

    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view),
    path('profile/', views.profile_view),
    path('register/', views.register_view),
    # path('relationship/', RelationshipListView.as_view(), name='my-relationship'),
    path('', include('social.urls')),
    path('', include('friends.urls')),
    path('chat/', include('chat.urls')),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)