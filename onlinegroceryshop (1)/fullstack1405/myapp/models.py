from django.db import models

# Create your models here.

class Userdata(models.Model):
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.email 
    
class Product(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='products/')
    dcost=models.IntegerField()
    cost=models.IntegerField()
    desc=models.TextField()

    def __str__(self):
        return self.name

class Cart(models.Model):
    user=models.ForeignKey(Userdata,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.product.name
 

class Payment(models.Model):
    firstName=models.CharField(max_length=100)
    lastName=models.CharField(max_length=100)
    username=models.CharField(max_length=100)
    address=models.CharField(max_length=300)
    country=models.CharField(max_length=20)
    state=models.CharField(max_length=20)
    zipcode=models.CharField(max_length=10)
    paymentMethod=models.CharField(max_length=100)
    totalamount=models.IntegerField(default=0,null=True,blank=True)

    def __str__(self):
        return self.username





    


