from django.db import models
from django.contrib.auth import get_user_model
from categories.models import Subcategory
from interests.models import Interest


class Service(models.Model):
	name = models.CharField(max_length=255)
	data_start = models.DateField()
	data_end = models.DateField()
	description = models.TextField(blank=True, null=True)
	img_url = models.URLField(blank=True, null=True)
	pdf_url = models.URLField(blank=True, null=True)
	subcategory = models.ForeignKey(Subcategory, related_name='services', on_delete=models.CASCADE)
	interests = models.ManyToManyField(Interest, related_name='services', blank=True)

	def __str__(self):
		return self.name


class UserService(models.Model):
	user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
	service = models.ForeignKey(Service, on_delete=models.CASCADE)
	priority = models.IntegerField()

	class Meta:
		unique_together = ('user', 'service')
