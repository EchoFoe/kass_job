from django.contrib import admin
from django.template.defaultfilters import truncatechars
from .models import *
# from import_export.admin import ImportExportActionModelAdmin
from import_export import resources
from import_export import fields
from import_export.widgets import ForeignKeyWidget


class JobImageInline(admin.TabularInline):
    model = JobImage
    extra = 0

    class JobCategoryAdmin(admin.ModelAdmin):
        list_display = [field.name for field in JobCategory._meta.fields]
        list_filter = ['name', 'id']
        search_fields = ['name', 'id']

        class Meta:
            model = JobCategory

    admin.site.register(JobCategory, JobCategoryAdmin)


class JobResource(resources.ModelResource):
    category = fields.Field(column_name='category', attribute='category',
                            widget=ForeignKeyWidget(JobCategory, 'name'))

    class Meta:
        model = Job
        # fields = [field.name for field in Product._meta.fields if field.name != "id"]
        # exclude = ['id']
        # import_id_fields = ['uuid']


# class JobAdmin(ImportExportActionModelAdmin):
#     resource_class = JobResource
#     # list_display = [field.name for field in Product._meta.fields if field.name != "id"]
#     list_display = ['id', 'name', 'category',
#                     'description_S', 'is_active', 'created', 'updated']
#     inlines = [JobImageInline]
#     list_filter = ['category']
#     search_fields = ['name', 'id']
#
#     class Meta:
#         model = Job
#
#
# admin.site.register(Job, JobAdmin)


class JobImageAdmin(admin.ModelAdmin):
    list_display = [field.name for field in JobImage._meta.fields]

    class Meta:
        model = JobImage


admin.site.register(JobImage, JobImageAdmin)
