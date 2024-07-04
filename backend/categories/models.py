from django.db import models


class Category(models.Model):
	name = models.CharField(max_length=255)
	color = models.CharField(max_length=7)

	def __str__(self):
		return self.name


class Subcategory(models.Model):
	name = models.CharField(max_length=255)
	category = models.ForeignKey(Category, related_name='subcategories', on_delete=models.CASCADE)

	def __str__(self):
		return self.name
