# from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import Stock

class StockModelTest(TestCase):

    def test_string_representation(self):
        stock = Stock.objects.create(name="Pen", quantity=50)
        self.assertEqual(str(stock), "Pen")

    def test_default_quantity(self):
        stock = Stock.objects.create(name="Notebook")
        self.assertEqual(stock.quantity, 1)

    def test_is_deleted_flag(self):
        stock = Stock.objects.create(name="Marker", is_deleted=True)
        self.assertTrue(stock.is_deleted)

    def test_unique_name_constraint(self):
        Stock.objects.create(name="Eraser")
        with self.assertRaises(Exception):
            Stock.objects.create(name="Eraser")  # Should raise error due to unique constraint
