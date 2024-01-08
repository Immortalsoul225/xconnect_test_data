from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

# Create your models here.
class Books(models.Model):
    id = models.AutoField(primary_key=True)
    book_name = models.CharField(max_length = 250)
    isbn = models.DecimalField(max_digits=13,decimal_places=0)    
    category = models.CharField(max_length=250)
    avaliable_copys = models.IntegerField(default=0)

    
    def __str__(self):
        return self.book_name


class Reservation(models.Model):
 
    user_id = models.OneToOneField(get_user_model(),on_delete=models.CASCADE)
    book_id = models.ForeignKey(Books,on_delete=models.CASCADE)
    reserve_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(auto_now_add=True)
    states = models.BooleanField(default = True)

    def save(self, *args, **kwargs):
        # Add 60 days to the return_date form date of reserver_date
        new_datetime = self.return_date + timezone.timedelta(days=60)
        
        # Set the new datetime to the field
        self.return_date = new_datetime

        super().save(*args, **kwargs)


class Fine(models.Model):
    status =  models.BooleanField()
    book_status_id = models.BooleanField()
    finePrice = models.FloatField()



    


    
  