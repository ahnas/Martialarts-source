from django.contrib import admin
from .models import Referee,Judge,Examinar,Author,Team

# Register your models here.


admin.site.register(Referee)
admin.site.register(Judge)
admin.site.register(Examinar)
admin.site.register(Author)
admin.site.register(Team)