from django.contrib import admin


# import your model
from collection.models import Profile


class ThingAdmin(admin.ModelAdmin):
    model = Profile
    list_display = ('name', 'description',)
    prepopulated_fields = {'slug': ('name',)}

# and register it
admin.site.register(Profile, ThingAdmin)

