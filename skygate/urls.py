
"""skygate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib.auth.views import (
    LogoutView,
    LoginView,
)

from app.views import (
    StartView,
    PanelView,
    BookDetailView,
    BookCreateView,
    BookListView,
    AuthorListView,
    AuthorDetailView,
    TagListView,
    BookUpdateView,
    AuthorUpdateView,
    TagUpdateView,
    BookDeleteView,
    AuthorDeleteView,
    AuthorCreateView,
    TagDeleteView,
    TagCreateView,
    signup,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', StartView.as_view(), name='index'),
    # panel vielw
    path('panel/', PanelView.as_view(), name='panel'),
    # books
    path('book-list', BookListView.as_view(), name='book-list'),
    path('book/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('book/<int:pk>/edit', BookUpdateView.as_view(), name='book-edit'),
    path('book/<int:pk>/delete', BookDeleteView.as_view(), name='book-delete'),
    path('book-create', BookCreateView.as_view(), name='book-create'),
    # authors
    path('author-list', AuthorListView.as_view(), name='author-list'),
    path('author/<int:pk>/', AuthorDetailView.as_view(), name='author-detail'),
    path('author/<int:pk>/edit', AuthorUpdateView.as_view(), name='author-edit'),
    path('author/<int:pk>/delete', AuthorDeleteView.as_view(), name='author-delete'),
    path('author-create', AuthorCreateView.as_view(), name='author-create'),
    # tags
    path('tag-list', TagListView.as_view(), name='tag-list'),
    path('tag/<int:pk>/edit', TagUpdateView.as_view(), name='tag-edit'),
    path('tag/<int:pk>/delete', TagDeleteView.as_view(), name='tag-delete'),
    path('tag-create', TagCreateView.as_view(), name='tag-create'),
    # account
    path('signup', signup, name='signup'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('login', LoginView.as_view(template_name='login.html'), name='login'),
    # aapi
    path('api/', include('app.api.urls'), name='book-api'),
]
