from django.db import models
from django.urls import reverse


# Create your models here.

class Prime(models.Model):

    number = models.IntegerField(primary_key=True, verbose_name="Número", blank=False, null=False)
    prime = models.BooleanField(verbose_name="Es primo?", default=False, blank=False, null=False)

    class Meta:
        verbose_name = "Prime"
        verbose_name_plural = "Primes"

    def __str__(self):
        return (str(self.number))

    def get_absolute_url(self):
        return reverse("Prime_detail", kwargs={"pk": self.pk})
