from django.db import models

# Create your models here.



class Tag(models.Model):
	name = models.CharField(max_length = 200)


	def __str__(self):
		return self.name


class Post(models.Model):
	headline = models.CharField(max_length = 200)
	sub_headline = models.CharField(max_length = 200, null = True, blank = True)
	images = models.ImageField(null=True, blank=True, upload_to="img")
	body = models.TextField(max_length = 200)
	created = models.DateTimeField(auto_now_add = True)
	active = models.BooleanField(default = False)
	featured = models.BooleanField(default = False)
	tags = models.ManyToManyField(Tag, null = True)

	#slug


	def __str__(self):
		return self.headline


class English(models.Model):
	headline = models.CharField(max_length = 200)
	sub_headline = models.CharField(max_length = 200, null = True, blank = True)
	images = models.ImageField(null=True, blank=True, upload_to="img")
	body = models.TextField(max_length = 200)
	created = models.DateTimeField(auto_now_add = True)
	active = models.BooleanField(default = False)
	featured = models.BooleanField(default = False)
	tags = models.ManyToManyField(Tag, null = True)

	#slug


	def __str__(self):
		return self.headline




class About(models.Model):
	headline = models.CharField(max_length = 200)
	sub_headline = models.CharField(max_length = 200, null = True, blank = True)
	images = models.ImageField(null=True, blank=True, upload_to="img")
	body = models.TextField(max_length = 200)
	created = models.DateTimeField(auto_now_add = True)
	active = models.BooleanField(default = False)
	featured = models.BooleanField(default = False)
	tags = models.ManyToManyField(Tag, null = True)

	#slug


	def __str__(self):
		return self.headline








class Abouttm(models.Model):
	headline = models.CharField(max_length = 200)
	sub_headline = models.CharField(max_length = 200, null = True, blank = True)
	images = models.ImageField(null=True, blank=True, upload_to="img")
	body = models.TextField(max_length = 200)
	created = models.DateTimeField(auto_now_add = True)
	active = models.BooleanField(default = False)
	featured = models.BooleanField(default = False)
	tags = models.ManyToManyField(Tag, null = True)

	#slug


	def __str__(self):
		return self.headline