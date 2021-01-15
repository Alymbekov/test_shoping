from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=200)
    parent = models.ForeignKey('self', related_name='children', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} --> '

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'