from django.contrib import admin

# Register your models here.

from .models import Person,Note,Webpage,Place,City,Vehicle,File,Telephone

admin.site.register(Place)

class PlaceInstanceInline(admin.TabularInline):
    model = Place.persons.through
    extra = 1

class TelephoneInstanceInline(admin.TabularInline):
    model = Telephone
    extra = 1

class VehicleInstanceInline(admin.TabularInline):
    model = Vehicle
    extra = 1

class WebpageInstanceInline(admin.TabularInline):
    model = Webpage
    extra = 1

class FileInstanceInline(admin.TabularInline):
    model = File
    extra = 1

class NoteInstanceInline(admin.TabularInline):
    model = Note
    extra = 1

class PersonAdmin(admin.ModelAdmin):
        list_display = ('name','surname','nickname')
        list_filter = ('places__city__name',)
        search_fields = ['name','surname','nickname']
        inlines = [PlaceInstanceInline,TelephoneInstanceInline,VehicleInstanceInline,WebpageInstanceInline,FileInstanceInline,NoteInstanceInline]

admin.site.register(Person,PersonAdmin)

