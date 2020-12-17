from django.db import models

# Create your models here.


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    
    ##slug field to avoid multiple objects when querying user 
    code = models.CharField(max_length = 250, null = True, blank = True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']
    def __str__(self):
        return self.code

    def save(self, *args, **kwargs):
        for field_name in ['name']:
            val = getattr(self,field_name,False)

            if val:
                setattr(self,'code', val.replace(' ','').lower())
                super(Category,self).save(*args,**kwargs)


class Writer(models.Model):
    name = models.CharField(max_length=100)
    
    ##slug field to avoid multiple objects when querying user 
    code = models.CharField(max_length = 250, null = True, blank = True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']
    def __str__(self):
        return self.code

    def save(self, *args, **kwargs):
        for field_name in ['name']:
            val = getattr(self,field_name,False)

            if val:
                setattr(self,'code', val.replace(' ','').lower())
                super(Writer,self).save(*args,**kwargs)


class Book(models.Model):

    category =  models.ForeignKey(Category,on_delete = models.CASCADE)
    writer =  models.ForeignKey(Writer,on_delete = models.CASCADE)

    # make sure category is already defined in top
    name = models.CharField(max_length=100)
    
    ##slug field to avoid multiple objects when querying user 
    code = models.CharField(max_length = 250, null = True, blank = True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']
    def __str__(self):
        return self.code

    def save(self, *args, **kwargs):
        for field_name in ['name']:
            val = getattr(self,field_name,False)

            if val:
                setattr(self,'code', val.replace(' ','').lower())
                super(Book,self).save(*args,**kwargs)
