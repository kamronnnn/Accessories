from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Category, GamingBuilds, LapTop, Armchair, Mice, Keyboard, Monitor, Comment


# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category_photo')

    def category_photo(self, category_photo):
        return mark_safe(f'<img src="{category_photo.photo.url}" width="75px;">')

    category_photo.short_description = 'Rasm'


class GamingBuildsAdmin(admin.ModelAdmin):
    list_display = ('name', 'cpu', 'ram', 'ssd', 'hdd', 'gpu', 'price', 'gaming_photo')
    list_display_links = ('name',)

    def gaming_photo(self, gaming_photo):
        return mark_safe(f'<img src="{gaming_photo.photo.url}" width="75px;">')

    gaming_photo.short_description = 'Rasm'


class LapTopAdmin(admin.ModelAdmin):
    list_display = ('name', 'cpu', 'ram', 'ssd', 'price', 'laptop_photo')
    list_display_links = ('name',)

    def laptop_photo(self, laptop_photo):
        return mark_safe(f'<img src="{laptop_photo.photo.url}" width="75px;">')

    laptop_photo.short_description = 'Rasm'


class ArmchairAdmin(admin.ModelAdmin):
    list_display = ('name', 'chairtype', 'upholsterymaterial', 'upholsterycolor', 'price', 'armchair_photo')

    def armchair_photo(self, armchair_photo):
        return mark_safe(f'<img src="{armchair_photo.photo.url}" width="75px;">')

    armchair_photo.short_description = 'Rasm'


class MiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'sensortype', 'maximumdpicpiresolution', 'price', 'mice_photo')

    def mice_photo(self, mice_photo):
        return mark_safe(f'<img src="{mice_photo.photo.url}" width="75px;">')

    mice_photo.short_description = 'Rasm'


class KeyboardAdmin(admin.ModelAdmin):
    list_display = ('name', 'keyboardtype', 'switchtype', 'backlight', 'price', 'keyboard_photo')

    def keyboard_photo(self, keyboard_photo):
        return mark_safe(f'<img src="{keyboard_photo.photo.url}" width="75px;">')

    keyboard_photo.short_description = 'Rasm'


class MonitorAdmin(admin.ModelAdmin):
    list_display = ('name', 'diagonal', 'screentype', 'price', 'monitor_photo')

    def monitor_photo(self, monitor_photo):
        return mark_safe(f'<img src="{monitor_photo.photo.url}" width="75px;">')

    monitor_photo.short_description = 'Rasm'



admin.site.register(Comment)
admin.site.register(Category, CategoryAdmin)
admin.site.register(GamingBuilds, GamingBuildsAdmin)
admin.site.register(LapTop, LapTopAdmin)
admin.site.register(Armchair, ArmchairAdmin)
admin.site.register(Mice, MiceAdmin)
admin.site.register(Keyboard, KeyboardAdmin)
admin.site.register(Monitor, MonitorAdmin)
