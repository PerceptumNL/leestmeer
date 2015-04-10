from django.contrib import admin

from adminsortable.models import Sortable
from adminsortable.admin import SortableAdmin

from adminsortable.fields import SortableForeignKey

from landing.models import Block, TextBlock, ImageBlock
from landing.models import BlockHolder

class ImageBlockAdmin(admin.ModelAdmin):
    model = TextBlock
    class Media:
        js = [
            '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
            '/static/tinymce_setup.js',
        ]

class TextBlockAdmin(admin.ModelAdmin):
    model = TextBlock
    class Media:
        js = [
            '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
            '/static/tinymce_setup.js',
        ]

admin.site.register(TextBlock, TextBlockAdmin)
admin.site.register(ImageBlock, ImageBlockAdmin)
