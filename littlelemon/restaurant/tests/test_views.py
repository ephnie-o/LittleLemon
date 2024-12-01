from django.test import TestCase
from restaurant.models import MenuTable
from rest_framework import status
from restaurant.serializer import MenuTableSerializer
from django.urls import reverse

class MenuViewTest(TestCase):
    def setup(self):
        self.menu1 = MenuTable.objects.create(title="Burger", price=100, inventory=10)
        self.menu2 = MenuTable.objects.create(title="Pasta", price=150, inventory=10)

    def test_getall(self):
        response = self.client.get(reverse('menu-list'))
        menu = MenuTable.objects.all()
        serialized_menu = MenuTableSerializer(menu, many=True).data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), serialized_menu)