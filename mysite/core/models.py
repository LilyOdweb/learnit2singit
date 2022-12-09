from django.db import models

from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.urls import reverse



# Create your models here.
class Book(models.Model):
	title = models.CharField(max_length=100)
	author = models.CharField(max_length=100)
	pdf = models.FileField(upload_to='books/pdf')
	cover = models.ImageField(upload_to='books/covers/',null=True,blank=True)

	def __str__(self):
		return self.title
		

	def delete(self,*args,**kwargs):
		self.pdf.delete()
		self.cover.delete()
		super().delete(*args,**kwargs)

class Comment(models.Model):
	post = models.ForeignKey(Book, related_name="comments", on_delete=models.CASCADE)
	name = models.CharField(max_length=255)
	body = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return '%s - %s' % (self.post.title, self.name)

