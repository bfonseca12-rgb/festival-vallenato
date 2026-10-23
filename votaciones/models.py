from django.db import models

class Edicion(models.Model):
    nombre = models.CharField(max_length=100)
    year = models.IntegerField(default=2027)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

    def __str__(self):
        return f"{self.nombre} ({self.year})"

class Categoria(models.Model):
    edicion = models.ForeignKey(Edicion, on_delete=models.CASCADE, related_name='categorias')
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} - {self.edicion.nombre}"

class Votacion(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='votaciones')
    titulo = models.CharField(max_length=150)
    descripcion = models.TextField()
    activa = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo

class Opcion(models.Model):
    votacion = models.ForeignKey(Votacion, on_delete=models.CASCADE, related_name='opciones')
    nombre_candidato = models.CharField(max_length=150)
    descripcion = models.TextField(blank=True, null=True)
    votos = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.nombre_candidato} ({self.votacion.titulo})"