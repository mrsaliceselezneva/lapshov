from django.contrib import admin
from .models import Therm, Connection, XmlFile

admin.site.register(Therm)
admin.site.register(Connection)
admin.site.register(XmlFile)
