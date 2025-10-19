from django.contrib import admin
from .models import Post
from django.utils.html import format_html

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_tag', 'original_price', 'offer_price', 'is_active', 'created_at')
    readonly_fields = ('image_tag',)

    def image_tag(self, obj):
        if obj.img:
            return format_html('<img src="{}" width="100" />'.format(obj.img.url))
        return ""
    image_tag.short_description = 'Image'

admin.site.register(Post, PostAdmin)
