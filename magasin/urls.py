from django.urls import path,include

from . import views
from .views import CategoryAPIView, FournisseurAPIView,ProductViewset, ProduitAPIView, ProduitNCAPIView
from rest_framework import routers
router = routers.SimpleRouter()
router.register('produit', ProductViewset, basename='produit')
urlpatterns = [
    path('', views.index,name='index'),
    path('listeCat/<int:id>',views.listeProduitCategorie,name='listeCat'),
    path('descArt/<int:id>',views.descriptionArt,name='description'),
    path('listeFournisseur',views.fournisseur,name='listeFour'),
    path('ajoutProd',views.ajoutProd,name='ajoutProduit'),
    path('register/',views.register, name = 'register'),
    path('api/category/', CategoryAPIView.as_view()),
    path('api/Produit/<int:id>', ProduitAPIView.as_view()),
    path('api/Fournisseur/', FournisseurAPIView.as_view()),
    path('api/ProduitNC/', ProduitNCAPIView.as_view()),
]