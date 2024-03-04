from django.db import models

# Create your models here.
class Product_Cate(models.Model):
    product_cate_id=models.IntegerField()
    product_cate_Name=models.CharField(max_length=100)

    def __str__(self):
        return self.product_cate_Name
    
class Product(models.Model):
    Product_Cate_Name=models.ForeignKey(Product_Cate,on_delete=models.CASCADE)
    Product_Id=models.IntegerField(primary_key=True)
    Product_Name=models.CharField(max_length=100)
    Product_Price=models.IntegerField()
    Product_Brand=models.CharField(max_length=100)


    def __str__(self):
        return self.Product_Name