from django.contrib import admin
from django.contrib.admin import ModelAdmin, StackedInline

from apps.models import *


@admin.register(IndexBanner)
class IndexBannerAdmin(ModelAdmin):
    list_display = ("id", "title", "video")
    list_display_links = (
        "id",
        "title",
    )


@admin.register(IndexAbout)
class IndexAboutAdmin(ModelAdmin):
    list_display = ("id", "title", "image")
    list_display_links = (
        "id",
        "title",
    )


@admin.register(IndexCategoryText)
class IndexCategoryTextAdmin(ModelAdmin):
    list_display = ("id", "title", "sub_title")
    list_display_links = ("id", "title")


@admin.register(Service)
class ServiceAdmin(ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("id", "name")


class FeaturesInline(StackedInline):
    model = Features


@admin.register(AboutUs)
class AboutUsAdmin(ModelAdmin):
    list_display = ("id", "title", "image")
    list_display_links = (
        "id",
        "title",
    )
    inlines = (FeaturesInline,)


@admin.register(Clients)
class ClientsAdmin(ModelAdmin):
    list_display = ("id", "image")
    list_display_links = ("id",)


@admin.register(Contact)
class ContactAdmin(ModelAdmin):
    list_display = ("id", "working_hours", "phone_1", "phone_2")
    list_display_links = (
        "id",
        "working_hours",
    )


@admin.register(Socials)
class SocialsAdmin(ModelAdmin):
    list_display = ("id", "instagram", "whatsup", "youtube")
    list_display_links = ("id", "instagram")


class GalleryImages(StackedInline):
    model = Image


@admin.register(Gallery)
class GalleryAdmin(ModelAdmin):
    list_display = ("id", "title", "sub_title")
    list_display_links = ("id", "title")
    inlines = (GalleryImages,)


@admin.register(ProductPage)
class ProductPageAdmin(ModelAdmin):
    list_display = (
        "id",
        "text",
    )
    list_display_links = ("id", "text")


@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = ("id", "title", "image")
    list_display_links = ("id", "title")
    exclude = ("slug",)


class ProductImagesInline(StackedInline):
    model = ProductImages


class ProductSizesInline(StackedInline):
    model = ProductSize


@admin.register(Product)
class ProductAdmin(ModelAdmin):
    list_display = ("id", "name", "price", "compound")
    list_display_links = ("id", "name")
    inlines = (
        ProductImagesInline,
        ProductSizesInline,
    )
    exclude = ("slug",)
