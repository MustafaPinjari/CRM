from django.contrib import admin
from .models import User, lead , Agent

admin.site.register(User)
admin.site.register(lead)
admin.site.register(Agent)