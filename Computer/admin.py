from django.contrib import admin
from .models import Computer, C_Acer, C_Asus, C_Msi, C_Lenovo, C_Mac, C_Mac_A, C_Mac_B, C_Mac_C

@admin.register(Computer)
class ComputerAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'date_post')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(C_Acer)
class C_AcerAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'date_post')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(C_Asus)
class C_AsusAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'date_post')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(C_Msi)
class C_MsiAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'date_post')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(C_Lenovo)
class C_Lenovo(admin.ModelAdmin):
    list_display = ('name', 'price', 'date_post')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(C_Mac)
class C_Mac(admin.ModelAdmin):
    list_display = ('name', 'price', 'date_post')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(C_Mac_A)
class C_Mac_A(admin.ModelAdmin):
    list_display = ('name', 'price', 'date_post')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(C_Mac_B)
class C_Mac_B(admin.ModelAdmin):
    list_display = ('name', 'price', 'date_post')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(C_Mac_C)
class C_Mac_C(admin.ModelAdmin):
    list_display = ('name', 'price', 'date_post')
    prepopulated_fields = {'slug': ('name',)}