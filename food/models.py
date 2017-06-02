from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

class Blog(models.Model):
    
	Restaurant Name = models.CharField(max_length=100, unique=True)
	Street Address = models.CharField(max_length=60,unique=True)
	Locations = models.CharField(max_length=60,unique=True)
	
	


def __unicode__(self):
        return self.Restaurant Name

def get_absolute_url(self):
        return reverse('server_edit', kwargs={'pk': self.pk})
		
