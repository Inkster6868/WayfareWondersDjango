from django.contrib import admin
from .models import Tour

# Register your models here.
@admin.register(Tour)
class Tour(admin.ModelAdmin):
    list_display = ('title','featured')  # Customize the list display
    search_fields = ('name',)  # Add search functionality
    list_filter = ('featured',)  # Add filters

    def __str__(self) -> str:
        return self.title

