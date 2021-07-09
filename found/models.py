from django.db import models

# Create your models here.
class FoundItem(models.Model):
    ITEMSTATUS = [
        (0, 'Not verified'), 
        (1, 'Verified'), 
        (2, 'Owner found'), 
    ]
    DEFAULT = 'default.png'

    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    email_id = models.EmailField(max_length=200)
    status = models.IntegerField(default=0, choices=ITEMSTATUS)
    pub_date = models.DateTimeField('date published')
    picture = models.ImageField(upload_to='pictures/%Y/%m/%d/', max_length=200, null=True, blank=True, default=DEFAULT)

    def __str__(self):
        return f'{self.title} : {self.description}'