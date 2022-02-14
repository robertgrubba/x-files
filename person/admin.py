from django.contrib import admin

# Register your models here.

from .models import Person,Note,Webpage,Place,City,Vehicle,File,Telephone

admin.site.register(Person)
admin.site.register(Note)
admin.site.register(Webpage)
admin.site.register(Place)
admin.site.register(City)
admin.site.register(Vehicle)
admin.site.register(File)
admin.site.register(Telephone)

#class CityAdmin(admin.ModelAdmin):
#    readonly_fields = ['addresses']
#
#    def addresses(self,City):
#        return f"{City.places.street} {City.places.number}"
#
#admin.site.register(City,CityAdmin)
