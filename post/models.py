from django.db import models
from django.contrib import admin

# Create your models here.
class author(models.Model):
	name=models.CharField(max_length=60)
	email=models.EmailField()
        
	def __unicode__(self):
 		return self.name



class post(models.Model):
	title=models.CharField(max_length=60)
	body=models.TextField()
	created=models.DateField()
	updated=models.DateField()
	#comment=models.ForeignKey('self')
	author=models.ForeignKey(author)
	
	def __unicode__(self):
		return ''



class comment(models.Model):
	name=models.CharField(max_length=60)
	email=models.CharField(max_length=60)
	#post=models.CharField(max_length=60)
	post=models.ForeignKey(post)
	def __unicode__(self):
		return self.name

admin.site.register(post)
admin.site.register(author)
admin.site.register(comment)


