from django.db import models

# Create your models here.
choice_item=(('veg','veg'),('Non-Veg','Non-Veg'),('egg','egg'))

class Item(models.Model):
    item_id=models.IntegerField(primary_key=True)
    item_name=models.CharField( max_length=50)
    item_price=models.IntegerField()
    item_desc=models.CharField(max_length=50)
    item_type=models.CharField(choices=choice_item,max_length=50)
    photo=models.ImageField()
    
    
    def __str__(self) :
        return self.item_name