from django.contrib import admin
from .models import Actor,Movie

admin.site.register([Actor,Movie])
