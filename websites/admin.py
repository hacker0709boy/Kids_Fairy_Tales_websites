from django.contrib import admin

# Register your models here.

from .models import Post, Tag, English, About, Abouttm


admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(English)
admin.site.register(About)
admin.site.register(Abouttm)