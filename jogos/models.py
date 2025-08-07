from django.db import models

# Create your models here.
class Jogo(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    image = models.ImageField(upload_to='jogos/', blank=True, null=True)
    trailer = models.CharField(max_length=500)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural="Jogos"