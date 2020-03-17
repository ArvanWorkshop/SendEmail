from django.db import models



class Form(models.Model):
    company = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    add1 = models.CharField(max_length=300)
    add2 = models.CharField(max_length=300)
    zipC = models.IntegerField()
    state = models.CharField(max_length=150, default=None)

    first_name = models.CharField(max_length=123, default=None)
    last_name = models.CharField(max_length=123, default=None)
    email = models.EmailField(max_length=123, default=None)
    phone = models.IntegerField(default=None)    
    image = models.ImageField(upload_to='images', default=None)


    def __str__(self):
        return self.company
