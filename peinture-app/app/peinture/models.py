from django.db import models



from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)



class marque(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name



class couleur(models.Model):
    name = models.CharField(max_length=500)
    hex_code = models.CharField(max_length=7, unique=True)
    color_code = models.CharField(max_length=6,default='')
    def __str__(self):
        return self.name



class voiture(models.Model):
    name = models.CharField(max_length=100)
    annee = models.IntegerField()
    parent = models.ForeignKey(marque, on_delete=models.CASCADE)
    code = models.ForeignKey(couleur, on_delete=models.CASCADE)
    def __str__(self):
        return self.name




       



class Base_Couleur(models.Model):
    name = models.CharField(max_length=50)
    color_code = models.CharField(max_length=7)
    hex_code = models.CharField(max_length=7,default='')

    def __str__(self):
        return self.name





class Formule_Base_Couleur(models.Model):
    formule = models.ForeignKey(couleur, on_delete=models.CASCADE)
    base_color = models.ForeignKey(Base_Couleur, on_delete=models.CASCADE)
    qte = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.base_color} {self.qte}g"



