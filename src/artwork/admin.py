from django.contrib import admin
from . models import Artwork

# Register your models here.

class ArtworkAdmin(admin.ModelAdmin):
    pass


admin.site.register(Artwork, ArtworkAdmin)