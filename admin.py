from django.contrib import admin
from user.models import User
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_filter = ['updated', 'is_active']
    search_fields = ['email']
    exclude = ('password','newsletter','invited_others','username')
    
#     def get_form(self, request, obj=None, **kwargs):
#         self.exclude = []
#         if not request.user.is_super_admin:
#             self.exclude.append('is_staff')
#             self.exclude.append('is_super_admin')
#         return super(UserAdmin, self).get_form(request, obj, **kwargs)


admin.site.register(User, UserAdmin)

