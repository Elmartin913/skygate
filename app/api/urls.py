from django.urls import path

from .views import BookRudAPIView, BookAPIView

urlpatterns = [
    path('<int:pk>', BookRudAPIView.as_view(), name='book-rud'),
    path('', BookAPIView.as_view(), name='book-api'),
]
