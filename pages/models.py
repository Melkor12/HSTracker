from django.db import models

# Create your models here.

# Specifying meal types which will show up in a dropdown menu:
MEAL_CHOICES = (
    ('breakfast', 'BREAKFAST'),
    ('lunch', 'LUNCH'),
    ('dinner', 'DINNER'),
    ('snack', 'SNACK'),
)

class FoodTracker(models.Model):
    mealType =models.CharField(max_length = 20, choices=MEAL_CHOICES, default='breakfast')
    foodType = models.CharField(max_length = 200)
    # foodTypeQuantity = models.DecimalField(verbose_name= "grams")
    explanation = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

# returns the string version of the model for an easier overview later on
def __str__(self):
    return self.mealType