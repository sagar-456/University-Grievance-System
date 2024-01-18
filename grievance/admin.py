from django.contrib import admin
from grievance.models import  Contact, UserData, Complaint, UserNotice, UserResponse
# Register your models here.

admin.site.register(UserData)
admin.site.register(Contact)
admin.site.register(Complaint)
admin.site.register(UserNotice)
admin.site.register(UserResponse)
