from django.contrib import admin
import csv
from django.http import HttpResponse
from .models import Post, User, Category, Tag, Comment


class ExportCsvMixin:
    def export_as_csv(self, request, queryset):

        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = "Export Selected"

@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin, ExportCsvMixin):
	list_display = ("author", "title", "published_date","category",)
	search_fields = ("title",)
	list_filter = ( "author", "title", "category", "tag",)
	actions = ["export_as_csv"]
	autocomplete_fields = ["category", "author"]
	filter_horizontal = ('tag',)


@admin.register(User)
class UserModelAdmin(admin.ModelAdmin, ExportCsvMixin):
	list_display = ("username", "first_name", "last_name", "gender", "phone_no", "email",)
	search_fields = ("username","gender",)
	list_filter = ("username", "first_name", "last_name", "gender", "phone_no","email",)
	actions = ["export_as_csv"]

	


@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin, ExportCsvMixin):
	list_display = ("name",)
	search_fields =("name",)
	list_filter =("name",)
	actions = ["export_as_csv"]



@admin.register(Tag)
class TagModelAdmin(admin.ModelAdmin, ExportCsvMixin):
	list_display = ("name",)
	search_fields =("name",)
	list_filter =("name",)
	actions = ["export_as_csv"]


@admin.register(Comment)
class CommentModelAdmin(admin.ModelAdmin, ExportCsvMixin):
	list_display = ("name","created_date","email",)
	search_fields =("name","created_date","email",)
	list_filter = ("name","created_date","email",)
	actions = ["export_as_csv"]



