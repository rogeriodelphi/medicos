from django.contrib import admin
from .models import *

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role', 'birth', 'specialtiesList', 'addressesList',)
    empty_value_display = '----'
    list_display_links = ('user', 'role')
    list_filter = ('user__is_active', 'role')
    # fields = ('user', ('role', ), 'image', 'birthday',  'specialties', 'addresses',)
    exclude = ('favorites', 'created_at', 'updated_at')
    readonly_fields = ('user',)
    search_fields = ('user__username',)
    date_hierarchy = 'created_at'

    fieldsets = (
        ('Usuário', {
            'fields': ('user', 'birthday', 'image')
        }),
        ('Função', {
            'fields': ('role',)
        }),
        ('Extras', {
            'fields': ('specialties', 'addresses')
        }),
    )

    def specialtiesList(self, obj):
        return [i.name for i in obj.specialties.all()]

    def addressesList(self, obj):
        return [i.name for i in obj.addresses.all()]

    def birth(self, obj):
        if obj.birthday:
            return obj.birthday.strftime("%d/%m/%Y")

    birth.empty_value_display = '___/___/_____'


        # css = {
        #     "all": ("css/custom.css",)
        # }
        # js = ("js/custom.js",)

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Address)
admin.site.register(DayWeek)
admin.site.register(Rating)
admin.site.register(Speciality)
admin.site.register(City)
admin.site.register(State)
admin.site.register(Neighborhood)


