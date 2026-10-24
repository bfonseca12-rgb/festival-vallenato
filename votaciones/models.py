from django.db import models

class Edicion(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    edicion = models.ForeignKey(Edicion, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nombre


class Votacion(models.Model):
    titulo = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True, blank=True)
    activa = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo


class Opcion(models.Model):
    votacion = models.ForeignKey(Votacion, on_delete=models.CASCADE, related_name='opciones', null=True, blank=True)
    nombre = models.CharField(max_length=100)
    votos = models.IntegerField(default=0)
    imagen = models.ImageField(upload_to='cantantes/imagenes/', blank=True, null=True)
    audio = models.FileField(upload_to='cantantes/audios/', blank=True, null=True)

    def __str__(self):
        return self.nombre