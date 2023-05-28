from rest_framework.serializers import ModelSerializer
from .models import *
class CategorySerializer(ModelSerializer):
    class Meta:
        model = Categorie
        fields = ['id', 'name']
class ProduitSerializer(ModelSerializer):
    class Meta:
        model = Produit
        fields = ['id', 'libelle','description','catégorie_id']
        
class FournisseurSerializer(ModelSerializer):
    class Meta:
        model = Fournisseur
        fields = '__all__'
class ProduitNCSerializer(ModelSerializer):
    categorie = CategorySerializer()
    fournisseur = FournisseurSerializer()

    class Meta:
        model = ProduitNC
        fields = '__all__'