from django.db import models

# Create your models here.
class Users(models.Model):
    first_name = models.CharField(max_length=8,blank=False,null=False)
    last_name = models.CharField(max_length=8,blank=False,null=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']
    def __str__(self):
        return self.first_name
