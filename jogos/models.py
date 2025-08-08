from django.db import models

# Create your models here.
class Jogo(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    image = models.ImageField(upload_to='jogos/', blank=True, null=True)
    trailer = models.CharField(max_length=500, help_text='link do youtube')
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if self.trailer:
            if 'watch?v=' in self.trailer:
                self.trailer = self.trailer.replace('watch?v=', 'embed/')
            elif 'youtu.be/' in self.trailer:
                video_id = self.trailer.split('youtu.be/')[1]
                self.trailer = f'https://www.youtube.com/embed/{video_id}'
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name_plural="Jogos"