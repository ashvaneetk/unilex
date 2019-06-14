from django.contrib import admin

from tag.models import Record, Tag


class TagInline(admin.TabularInline):
    model = Tag
    raw_id_fields = ['concept']
    extra = 0


@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    search_fields = ['title', 'desc', 'uri']
    list_display = ('title', 'uri',)
    inlines = [TagInline]
