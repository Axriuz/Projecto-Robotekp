from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Producto
from django.urls import reverse_lazy
from .forms import Productoform
from django.db.models import Q
from django.views.defaults import page_not_found
# Create your views here.

 
def error404(request,exception):
    return render(request, 'Tienda/404.html')

def index(request):
    return render(request, 'Tienda/index.html')

class ProductoList(ListView):
    model = Producto
    template_name = 'Tienda/consultar_producto.html'
        
    
class ProductoCreate(CreateView):
    model = Producto
    form_class = Productoform
    template_name= 'Tienda/agregar_producto.html'
    success_url = reverse_lazy('ver_producto')

class ProductoUpdate(UpdateView):
    model = Producto
    form_class= Productoform
    template_name= 'Tienda/modificar_producto.html'
    success_url = reverse_lazy('ver_producto')

class ProductoDelete(DeleteView):
    model = Producto
    form_class= Productoform
    template_name= 'Tienda/eliminar_producto.html'
    success_url = reverse_lazy('ver_producto')
