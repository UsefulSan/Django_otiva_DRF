from django.contrib import admin

from ads.models import Categories, Ads, Locations, Users

admin.site.register(Ads)
admin.site.register(Categories)
admin.site.register(Locations)
admin.site.register(Users)
