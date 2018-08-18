from django.test import TestCase, client
from django.urls import reverse, resolve

from app.views import PanelView

# Create your tests here.


class HomeTests(TestCase):
    def test_home_view_status_code(self):
        url = reverse('panel')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/panel/')
        self.assertEquals(view.func.__name__, PanelView.as_view().__name__)
