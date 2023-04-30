from django.test import TestCase
from .models import Menu

class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(item, "IceCream : 80")


class MenuViewTest(TestCase):

    def setUp(self):
        Menu.objects.create(title="IceCream1", price=81, inventory=100)
        Menu.objects.create(title="IceCream2", price=82, inventory=100)
        Menu.objects.create(title="IceCream3", price=83, inventory=100)



    def test_getall(self):
        self.assertEqual(Menu.objects.count(), 3)
