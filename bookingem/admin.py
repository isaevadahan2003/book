from django.contrib import admin
from bookingem import models



class BooksAdmin(admin.ModelAdmin):
    model = models.Books
    list_editable = ["title", "description"]
    list_display = ["id", "title", "description"]
    search_fields = ["title"]
    # list_filter = ["created_date"]

admin.site.register(models.Books, BooksAdmin)
admin.site.register(models.Comment)

