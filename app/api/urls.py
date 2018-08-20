from django.urls import path

from .views import BookAPIView

urlpatterns = [
    path('<int:pk>', BookAPIView.as_view(), name='book-rud'),
]
