from django.contrib import admin

from .models import User, Review, Title, Genre, Category

admin.site.register(User)
admin.site.register(Review)
admin.site.register(Title)
admin.site.register(Genre)
admin.site.register(Category)
