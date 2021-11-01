from django.db import models
from django.db.models.fields import BLANK_CHOICE_DASH, Field

# Create your models here.
class Product(models.Model):
    id = models.BigAutoField(primary_key=True)
    Name = models.CharField(max_length= 64)
    Price = models.FloatField()
    ImageFile = models.ImageField(upload_to = 'images/', blank = True)
    ImageFile1 = models.ImageField(upload_to = 'images/', blank = True)
    Description = models.TextField(blank=True)
    Validade = models.TextField(blank=True, default="Validade de 60 dias; Conservar o produto refrigeração; Após aberto consumir em 30 dias.")
    def __str__(self) -> str:
        return f"{self.Name}, id: {self.id}"
class Flavour(models.Model):
    ProductN = models.ForeignKey(Product, on_delete=models.CASCADE)
    Flavour1 = models.CharField(max_length=32)
    Ingredients = models.TextField(blank=True)
    Color = models.CharField(max_length= 64, default="green", blank=True)
    def __str__(self) -> str:
        return f"{self.ProductN}, sabor: {self.Flavour1}"
class Image(models.Model):
    ProductN = models.ForeignKey(Product, on_delete=models.CASCADE)
    ImageFile = models.ImageField(upload_to = 'images/', blank = True)
    Image1 = models.CharField(max_length= 64,blank = True, default='media/images/NOME DO ARQUIVO')
    def __str__(self) -> str:
        return f"Imagens do produto: {self.ProductN}"