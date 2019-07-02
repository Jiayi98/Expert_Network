

# Register your models here.
from django.contrib import admin
from .models import ExpertComments, ExpertInfo, WorkExp

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
# Register your models here.

admin.site.register(ExpertComments)
#admin.site.register(ExpertInfo)
admin.site.register(WorkExp)

@admin.register(ExpertInfo)
class ExpertInfoAdmin(admin.ModelAdmin):
    list_display = ('ename','esex','emobile','eemail','etrade','esubtrade','ebirthday',
                    'elandline','elocation','emsn','eqq','ephoto','estate','ecomefrom',
                    'eremark','admin_id','addtime')
    list_filter = ('ename', 'emobile','eemail', 'etrade','elocation','addtime')
    search_fields = ('ename', 'emobile','eemail', 'etrade','elocation','addtime')
    ordering = ('-addtime',)