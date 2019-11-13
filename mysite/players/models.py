from django.db import models

from django.utils import timezone

class Players(models.Model):
    nombre = models.TextField()
    Correo = models.EmailField(max_length=254)
    MMR = models.IntegerField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.nombre
