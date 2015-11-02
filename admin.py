from django.contrib import admin
from myapp.models import *

admin.site.register(Forumpost, Forumpost.Admin)
admin.site.register(Tag, Tag.Admin)