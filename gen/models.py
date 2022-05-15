from django.db import models



# Create your models here.

class epassqr(models.Model):
    pass_sl=models.AutoField
    qr_id=models.CharField(max_length=20)
    qr_img=models.ImageField(upload_to='gen/qr_data')
    qr_bit64=models.CharField(max_length=2000)



    def __str__(self):
        return self.qr_id
