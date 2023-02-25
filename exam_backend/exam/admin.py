from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Exam)
admin.site.register(User_data)
admin.site.register(Student_Response)
admin.site.register(Question)
