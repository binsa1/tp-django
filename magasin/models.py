from django.db import models
from datetime import date
class Produit(models.Model):
    type_choices=[('em','emballe'),('fr','frais'),('cs','conserve')]
    libelle=models.CharField(max_length=100)
    description=models.TextField(default='Non define')
    prix=models.DecimalField(max_digits=10,decimal_places=3)
    type=models.CharField(max_length=2,choices=type_choices,default='em')
    catégorie=models.ForeignKey('Categorie',on_delete=models.CASCADE,null=True)
    img=models.ImageField(blank=True)
    Fournisseur=models.ForeignKey('Fournisseur',on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.libelle+" "+self.description+" "+str(self.prix)
class Categorie(models.Model):
    type_choices=[('Al','Alimentaire'), ('Mb','Meuble'),
('Sn','Sanitaire'), ('Vs','Vaisselle'),
('Vt','Vêtement'),('Jx','Jouets'),('Lg','Linge de Maison'),('Bj','Bijoux'),('Dc','Décor')]
    name=models.CharField(max_length=50,choices=type_choices,default='Al')
    def __str__(self):
        return self.name

class Fournisseur(models.Model):
    nom=models.CharField(max_length=100)
    adresse=models.TextField()
    email=models.TextField()
    telephone=models.CharField(max_length=8)
    def __str__(self):
        return self.nom+" "+self.adresse+" "+self.email+" "+self.telephone
class ProduitNC(Produit):
    Duree_garantie=models.CharField(max_length=100)
    def __str__(self):
        return super().__str__()+f"({self.Duree_garantie})"    
class Commande(models.Model):
    dateCde=models.DateField(null=True,default=date.today)
    totalCde=models.DecimalField(max_digits=10,decimal_places=3)
    produits=models.ManyToManyField('Produit')
    def __str__(self):
        return self.dateCde+" : "+self.totalCde