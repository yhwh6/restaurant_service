from django.contrib.auth.models import AbstractUser

from django.core.validators import MaxValueValidator

from django.db import models

from django.urls import reverse


class DishType(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ["id"]

    def __str__(self) -> str:
        return self.name


class Cook(AbstractUser):
    years_of_experience = models.IntegerField(null=True, blank=True, validators=[MaxValueValidator(80)])

    class Meta:
        verbose_name = "cook"
        verbose_name_plural = "cooks"
        ordering = ["id"]

    def __str__(self) -> str:
        return f"{self.username} ({self.first_name} {self.last_name})"

    def get_absolute_url(self):
        return reverse("restaurant:cook-detail", kwargs={"pk": self.pk})


class Dish(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    dish_type = models.ForeignKey(DishType, on_delete=models.CASCADE)
    cooks = models.ManyToManyField(Cook, related_name="dishes")

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ["name"]
