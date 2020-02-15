from django.contrib import admin
from .models import Article, Comment, PetOnShow
from .models import Profile

admin.site.register(Profile)
admin.site.register(Article)
admin.site.register(PetOnShow)
