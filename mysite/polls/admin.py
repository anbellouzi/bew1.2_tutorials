

# Register your models here.
from django.contrib import admin

from .models import Question, Topping, Pizza

admin.site.register(Question)
admin.site.register(Topping)
admin.site.register(Pizza)
