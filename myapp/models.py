from django.db import models

#Creación de tablas en bbdd.

''' Tablas tipo contenido '''
# --> Verificar largo de cada str

class Categoria(models.Model):
    nom_categoria = models.CharField(max_length=20)    # <-- Buena práctica del uso de ForeignKey?

    def __str__(self):
        return self.nom_categoria
    
class Abecedario(models.Model):
    idabc = models.AutoField(primary_key=True)
    letra = models.CharField(max_length=1)
    linkimg = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.idabc}, {self.letra}, {self.linkimg}"


''' Tabla Explicaciones'''
class Explicaciones(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    img = models.CharField(max_length=500)
    vid = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.categoria}, {self.img}, {self.vid}"

''' Tabla Actividades '''
class Actividades(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    videos = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.categoria}, {self.videos}"


