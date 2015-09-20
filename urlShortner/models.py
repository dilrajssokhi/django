from django.db import models
import datetime
from django.utils import timezone


# Create your models here.
class urlShortner(models.Model):
    fullurl = models.URLField(max_length=200)
    shorturl = models.URLField(max_length=200,default='')
    entry_date = models.DateTimeField('date entered')

    def __unicode__(self):
        return self.fullurl
    def was_entered_recently(self):
        return self.entry_date >= timezone.now() - datetime.timedelta(days=1)
