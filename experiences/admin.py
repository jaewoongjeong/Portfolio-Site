from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from experiences.models import PostModel

# Register your models here.
@admin.register(PostModel)
class PostAdmin(SummernoteModelAdmin, admin.ModelAdmin):
    summernote_fields = ('content',)
    prepopulated_fields = {'slug': ('place',)}

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')

