from django.http import response
from django.test import Client, TestCase, client

from Tomperrus.views import products
from .models import Product, Flavour, Image

# Create your tests here.
class ProductTestCase(TestCase):
    def setUp(self):
        p1 =  Product.objects.create(Name = "produto", Price = 12, ImageFile = "media/images/chimichurri.jpeg", 
        ImageFile1 = "media/images/chimichurri.jpeg", Description  = "des", Validade = "val")
    def test_index(self):
        c = Client()
        response = c.get("")
        self.assertEqual(response.status_code, 200)
       # self.assertEqual(response.context["product"].count(), 3)
    def test_valid_product_page(self):
        c = Client()
        p = Product.objects.get(Name="produto")
        response = c.get(f"/{p.Name}")
        self.assertEqual(response.status_code, 200)
