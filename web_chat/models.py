from django.db import models
from web.models import UserProfile
# Create your models here.


class QQGroup(models.Model):
    name = models.CharField(max_length=64,unique=True)
    members = models.ManyToManyField(UserProfile,blank=True)
    admins = models.ManyToManyField(UserProfile,related_name='gruop_admins')
    description = models.CharField(max_length=255,default='nothing....')
    max_member_num = models.IntegerField(default=200)

    def __unicode__(self):
        return self.name

