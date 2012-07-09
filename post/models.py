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
	author=models.ForeignKey(author)
	
	def __unicode__(self):
		return ''



class comment(models.Model):
	name=models.CharField(max_length=60)
	email=models.CharField(max_length=60)
	post=models.ForeignKey(post)
	body=models.TextField()
	created=models.DateField()
	updated=models.DateField()
	def __unicode__(self):
		return self.name
        def body_60(self):
		return self.body[:60]

class commentlnline(admin.TabularInline):
	model=comment
	
class postAdmin(admin.ModelAdmin):
	list_display=('title','created','updated')
	search_fields=('title','body')
	list_filter=('created','author')
	inlines=[commentlnline]
	

class commentAdmin(admin.ModelAdmin):
	list_display=('post','body_60','name','created','updated',)
	filter_fields=('created','author')
	


admin.site.register(post,postAdmin)
admin.site.register(author)
admin.site.register(comment,commentAdmin)


