from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):

    def setUp(self):
        Menu.objects.create(title="IceCream", price=8.00, inventory=100)
        Menu.objects.create(title="Pizza", price=12.00, inventory=50)
        Menu.objects.create(title="Pasta", price=10.00, inventory=30)

    def test_getall(self):
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)

        self.assertEqual(len(serializer.data), 3)
        self.assertEqual(serializer.data[0]['title'], "IceCream")