from django.contrib import admin
from .models import Image
from .models import Contact
@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display=('photo','title','content')

admin.site.register(Contact)
