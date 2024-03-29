from django.contrib import admin
from django.contrib.admin import ModelAdmin, StackedInline
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from django.utils.text import Truncator
from modeltranslation.admin import TranslationAdmin

from apps.models import *
from apps.utils import ImagePreviewAdminWidget, VideoPreviewAdminWidget, FilePreviewAdminWidget


@admin.register(IndexBanner)
class IndexBannerAdmin(TranslationAdmin):
    list_display = ("id", "title", "show_video")
    list_display_links = (
        "id",
        "title",
    )
    formfield_overrides = {
        FileField: {"widget": VideoPreviewAdminWidget},
    }

    def show_video(self, obj):
        if obj.video:
            return format_html(
                f'<video width="240" height="180" controls><source src="{obj.video.url}" type="video/mp4">Your browser does not support the video tag.</video>'
            )
        else:
            return "No video available"

    show_video.short_description = "Video"


@admin.register(IndexAbout)
class IndexAboutAdmin(TranslationAdmin):
    list_display = ("id", "title", "display_image")
    list_display_links = (
        "id",
        "title",
    )
    formfield_overrides = {
        ImageField: {"widget": ImagePreviewAdminWidget},
    }

    def display_image(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="max-width:200px; max-height:200px;" />',
                obj.image.url,
            )
        else:
            return "No image available"

    display_image.short_description = "Image"


@admin.register(IndexCategoryText)
class IndexCategoryTextAdmin(TranslationAdmin):
    list_display = ("id", "title", "sub_title")
    list_display_links = ("id", "title")


@admin.register(Service)
class ServiceAdmin(TranslationAdmin):
    list_display = ("id", "name")
    list_display_links = ("id", "name")


class FeaturesInline(StackedInline):
    model = Features
    exclude = ("title", "text")


@admin.register(AboutUs)
class AboutUsAdmin(TranslationAdmin):
    list_display = ("id", "title", "display_image")
    list_display_links = (
        "id",
        "title",
    )
    inlines = (FeaturesInline,)

    formfield_overrides = {
        FileField: {"widget": FilePreviewAdminWidget},
    }

    def display_image(self, obj):
        if obj.image:
            file_type = obj.image.name.split(".")[-1].lower()
            if file_type in ["png", "jpg", "jpeg", "gif"]:
                # Display an image tag if the file is an image
                return format_html(
                    '<img src="{}" style="max-width:200px; max-height:200px;" />',
                    obj.image.url,
                )
            elif file_type in ["mp4", "avi", "mov", "wmv"]:
                # Display a video tag if the file is a video
                return format_html(
                    '<video width="200" height="200" controls><source src="{}" type="video/mp4">'
                    'Your browser does not support the video tag.</video>', obj.image.url
                )
        return "No image or video available"

    display_image.short_description = "Image/Video"


@admin.register(Clients)
class ClientsAdmin(ModelAdmin):
    list_display = ("id", "display_image")
    list_display_links = ("id",)
    formfield_overrides = {
        ImageField: {"widget": ImagePreviewAdminWidget},
    }

    def display_image(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="max-width:200px; max-height:200px;" />',
                obj.image.url,
            )
        else:
            return "No image available"

    display_image.short_description = "Image"


@admin.register(Contact)
class ContactAdmin(TranslationAdmin):
    list_display = ("id", "working_hours", "phone_1", "phone_2")
    list_display_links = (
        "id",
        "working_hours",
    )


@admin.register(Socials)
class SocialsAdmin(ModelAdmin):
    list_display = ("id", "instagram", "whatsup", "telegram")
    list_display_links = ("id", "instagram")
    exclude = ("youtube", "linkedin")


class GalleryImages(StackedInline):
    model = Image
    formfield_overrides = {
        ImageField: {"widget": ImagePreviewAdminWidget},
    }


@admin.register(Gallery)
class GalleryAdmin(TranslationAdmin):
    list_display = ("id", "title", "display_sub_title", "display_image")
    list_display_links = ("id", "title")
    inlines = (GalleryImages,)

    def display_sub_title(self, obj):  # noqa
        return Truncator(obj.sub_title).chars(60)

    def display_image(self, obj):
        first_image = obj.images.first()
        if first_image:
            image_tag = '<img src="{}" width="100" height="100" />'.format(
                first_image.image.url
            )
            return mark_safe(image_tag)
        return "No Image"

    display_image.allow_tags = True
    display_image.short_description = "Image"


@admin.register(ProductPage)
class ProductPageAdmin(TranslationAdmin):
    list_display = (
        "id",
        "title",
        "text",
    )
    list_display_links = (
        "id",
        "title",
    )


@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    list_display = ("id", "title", "display_image")
    list_display_links = ("id", "title")
    exclude = ("slug",)

    formfield_overrides = {
        ImageField: {"widget": ImagePreviewAdminWidget},
    }

    def display_image(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="max-width:200px; max-height:200px;" />',
                obj.image.url,
            )
        else:
            return "No image available"

    display_image.short_description = "Image"


class ProductImagesInline(StackedInline):
    model = ProductImages
    formfield_overrides = {
        ImageField: {"widget": ImagePreviewAdminWidget},
    }


class ProductSizesInline(StackedInline):
    model = ProductSize


@admin.register(Product)
class ProductAdmin(TranslationAdmin):
    list_display = ("id", "name", "price", "compound", "display_image")
    list_display_links = ("id", "name")
    exclude = ("slug",)
    inlines = [ProductImagesInline, ProductSizesInline]

    def display_image(self, obj):
        first_image = obj.images.first()
        if first_image:
            image_tag = '<img src="{}" width="100" height="100" />'.format(
                first_image.image.url
            )
            return mark_safe(image_tag)
        return "No Image"

    display_image.allow_tags = True
    display_image.short_description = "Image"
