from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from send_mail import *
# Create your models here.


class  Post(models.Model):
	"""docstring for  Post"""
	


	#Les differents champs de la table Post
	categorie = models.CharField(max_length=200)
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()


	def __str__(self):
		return self.title



class  Biographie(models.Model):
	"""docstring for  Biographie"""

	contenu = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

class Contact(models.Model):
	"""docstring for contact"""

	mail= models.CharField(max_length=1000)
	objet = models.CharField(max_length=1000)
	message = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		
		return self.mail+" [ "+self.objet+" ]"