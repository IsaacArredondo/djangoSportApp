from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from sklearn.tree import DecisionTreeClassifier
import joblib

GENDER =(
    (0, 'Female'),
    (1, 'Male'),
)

# Create your models here.
class Data(models.Model):
    name = models.CharField(max_length=100, null=True)
    age = models.PositiveIntegerField(validators = [MinValueValidator(13), MaxValueValidator(19)], null=True)
    height = models.PositiveIntegerField(null=True)
    sex = models.PositiveIntegerField(choices=GENDER, null=True)
    predictions = models.CharField(max_length=100, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.name