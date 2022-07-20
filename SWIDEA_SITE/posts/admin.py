# admin.py
from django.contrib import admin
from .models import Post
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class PostResource(resources.ModelResource):
	class Meta:
		model = Post
		fields = ('id', 'idea', 'photo', 'content', 'interest', 'tool')
		export_order = fields


class PostAdmin(ImportExportModelAdmin):
	fields = ('idea', 'photo', 'content', 'interest', 'tool')
	list_display = ('id', 'idea', 'photo', 'content', 'interest', 'tool')
	resource_class = PostResource


admin.site.register(Post, PostAdmin)
