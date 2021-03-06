from distutils.log import error
from django.shortcuts import render
from Tomperrus.models import Product, Flavour, Image
from django.http import Http404

# Create your views here.
#products = [['Chimichurri tradicional', 'pão de alho.jpg', 'descrição'],['Chimichurri sabor bacon', 'pão de alho.jpg', 'descrição'],['Chimichurri sabor apimentado', 'pão de alho.jpg', 'descrição'], ['Farofa de soja', 'farofa1.jpg', 'descrição'],['Pão de alho',  'imagem', 'pão de alho.jpg']]
def index(request):
    return render(request, "tomperrus/index.html", {
        "products": Product.objects.all()
    })
def products(request, Product_Name):
    try:
        Pr = Product.objects.get(Name = Product_Name)
    except Product.DoesNotExist:
        return render(request, "tomperrus/index.html", 
        {"error" : "Produto não encontrado, volte a pagina inicial"})
    product = Product.objects.get(Name = Product_Name)
    flavours = Flavour.objects.filter(ProductN = product)
    images = Image.objects.filter(ProductN = product)
    return render(request, "tomperrus/products.html", {
    "product": product,
    "flavours": flavours,
    "images": images
    })
   