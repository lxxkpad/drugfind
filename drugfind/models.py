from django.db import models

# Create your models here.

class SaveImage(models.Model):
    Image_file = models.ImageField(upload_to = 'upload/')

    #ขั้นตอนเกี่ยวกับการเปลี่ยนขนาดภาพ ก็ใช้หลักการเดิมทั้งหมด
    file_format = 'JPEG'
    file_name = 'sample.jpg'
    content_type = 'image/jpeg'