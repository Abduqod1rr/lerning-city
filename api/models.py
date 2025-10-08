from django.db import models
from users.models import CustomUser
from decimal import Decimal
# Create your models here.

#
class Lesson(models.Model):

    title=models.CharField(max_length=30,default='**title**')
    content=models.FileField(upload_to='lessons/')
    price=models.DecimalField(max_digits=8, decimal_places=2,default=Decimal('0.00'))
    owner=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    put_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=['-put_at']
    
    def __str__(self):
        return self.title , self.content
    
#
class boughtLessons(models.Model):

    student=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    lesson=models.ForeignKey(Lesson, on_delete=models.CASCADE)
    bought_at=models.DateTimeField(  auto_now_add=True)