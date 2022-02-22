from django.contrib import admin

# Register your models here.
from django.contrib import admin
# imports the FoodTracker model from the model file in the same directory(.models)
from .models import FoodTracker

# we register the FoodTracker Model on the Admin site so that we have a clear view of it
admin.site.register(FoodTracker)