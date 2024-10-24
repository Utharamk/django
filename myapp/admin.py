from django.contrib import admin
from .models import *
# Register your models here.
# admin.site.register(user)
# admin.site.register(book)
# admin.site.register(employee)
# admin.site.register(product)
# class customer(admin.ModelAdmin):
#     list_display=('first_name','last_name','address',)
#     search_fields=('first_name',)
#     list_filter=('first_name',)
# admin.site.register(customer1model,customer)
# admin.site.site_header='Uthara'

# admin.site.register(userproduct)
# admin.site.register(productuser)

# class bookadmin(admin.ModelAdmin):
#     list_display=('bpb_title','bpb_isbn','bpb_publisher')
#     search_fields=('bpb_title','bpb_isbn',)
#     list_filter=('bpb_publication_date',)
# admin.site.register(bookpbmodel,bookadmin)
# admin.site.register(publishermodel)

admin.site.register(Student)
admin.site.register(Cours)

admin.site.register(Organizer)
admin.site.register(Event)