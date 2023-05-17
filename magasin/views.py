
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from .models import Produit
from .models import Categorie
from .models import *
from .forms import ProduitForm,UserRegistrationForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib import messages
from rest_framework.views import APIView
from rest_framework.response import Response
from magasin.serializers import CategorySerializer, FournisseurSerializer, ProduitNCSerializer,ProduitSerializer
# Create your views here.
@login_required
def index(request):
   products= Produit.objects.all()
   categorie=Categorie.objects.all()                     
   context={'products':products,'categorie' :categorie}
   return render(request,'magasin/mesProduits.html',context)
@login_required
def listeProduitCategorie(request,id):
   produit=Produit.objects.filter(catégorie=id)
   categorie=Categorie.objects.all()
   context={'products' :produit,'categorie' :categorie}
   return render(request,'magasin/mesProduits.html',context)
@login_required
def descriptionArt(request,id):
   produit=Produit.objects.filter(id=id)
   categorie=Categorie.objects.all()
   context={'products' :produit,'categorie' :categorie}
   return render(request,'magasin/description.html',context)
@login_required
def fournisseur(request):
   categorie=Categorie.objects.all()
   fournisseur=Fournisseur.objects.all()
   context={'Fourniseur' :fournisseur,'categorie' :categorie}
   return render(request,'magasin/fournisseur.html',context)
@login_required
def ajoutProd(request):
   if request.method == "POST" :
      form = ProduitForm(request.POST,request.FILES)
      if form.is_valid():
         form.save()
         return HttpResponseRedirect('/magasin')
   else:
      form = ProduitForm() #créer formulaire vide
      categorie=Categorie.objects.all()
   return render(request,'magasin/majProduits.html',{'form':form,'categorie':categorie})  

def register(request):
   if request.method == 'POST' :
      form = UserRegistrationForm(request.POST)
      if form.is_valid():
         form.save()
         username = form.cleaned_data.get('username')
         password = form.cleaned_data.get('password1')
         user = authenticate(username=username, password=password)
         login(request,user)
         messages.success(request, f'Coucou {username}, Votre compte a été créé avec succès !')
         return redirect('index')
   else:
      form = UserRegistrationForm()
   return render(request,'registration/register.html',{'form':form})
class CategoryAPIView(APIView):
   def get(self, *args, **kwargs):
      categories = Categorie.objects.all()
      serializer = CategorySerializer(categories, many=True)
      return Response(serializer.data)
class ProduitAPIView(APIView):
   def get(self, *args, **kwargs):
      categories = Produit.objects.all()
      serializer = ProduitSerializer(categories, many=True)
      return Response(serializer.data)  
class FournisseurAPIView(APIView):
   def get(self, *args, **kwargs):
      fournisseurs = Fournisseur.objects.all()
      serializer = FournisseurSerializer(fournisseurs, many=True)
      return Response(serializer.data)  

class ProduitNCAPIView(APIView):
   def get(self, *args, **kwargs):
      produitNC = ProduitNC.objects.all()
      serializer = ProduitNCSerializer(produitNC, many=True)
      return Response(serializer.data) 
class ProductViewset(APIView):
   serializer_class = ProduitSerializer
   def get_queryset(self):
      queryset = Produit.objects.filter(active=True)
      category_id = self.request.GET.get('category_id')
      if category_id:
         yset = queryset.filter(categorie_id=category_id)
      return queryset   