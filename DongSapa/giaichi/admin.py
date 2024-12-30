from django.contrib import admin
from .models import Nhanvien, Phongban, Giaichi

# Register your models here.
admin.site.register(Giaichi)
admin.site.register(Phongban)
admin.site.register(Nhanvien)
