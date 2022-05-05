from django.contrib import admin
from app_my_blog.models import Post, Profile, Image
from django.utils.translation import gettext_lazy as _


class ProfileAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "user",
        "date_of_birth",
        "city",
        "number_of_publications"
    ]

    list_filter = [
        "date_of_birth",
        "city"
    ]

    search_fields = ["city"]


class PostInline(admin.TabularInline):
    model = Post


class PostAdmin(admin.ModelAdmin):
    list_display = ["id",
                    "post_author",
                    "post_title",
                    "publication_date",
                    "editing_date",
                    "is_published",
                    "status"
                    ]

    list_filter = ["post_author",
                   "post_title",
                   "publication_date",
                   "editing_date",
                   "is_published",
                   "status"
                   ]

    search_fields = ["post_title"]

    actions = ["mark_as_active", "mark_as_not_active"]

    def mark_as_active(self, request, queryset):
        queryset.update(status="a")

    def mark_as_not_active(self, request, queryset):
        queryset.update(status="no")

    def mark_as_under_consideration(self, request, queryset):
        queryset.update(status="uc")

    mark_as_active.short_description = _("Change to Active status")
    mark_as_not_active.short_description = _("Change to No-active status")


class ImageAdmin(admin.ModelAdmin):
    list_display = [
        "post_id",
        "images"
    ]

    list_filter = [
        "post_id"
    ]


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Image, ImageAdmin)
