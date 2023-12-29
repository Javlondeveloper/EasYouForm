from modeltranslation.translator import TranslationOptions, register

from .models import *


@register(IndexBanner)
class IndexBannerTranslation(TranslationOptions):
    fields = ("title",)


@register(IndexAbout)
class IndexAboutTranslation(TranslationOptions):
    fields = ("title", "text")


@register(IndexCategoryText)
class IndexCategoryTextTranslation(TranslationOptions):
    fields = ("title", "sub_title")


# Service translation
@register(Service)
class ServiceTranslation(TranslationOptions):
    fields = ("name",)


# About Us translations


@register(AboutUs)
class AboutUsTranslation(TranslationOptions):
    fields = (
        "title",
        "text_up",
        "text_down",
    )


@register(Features)
class FeaturesTranslation(TranslationOptions):
    fields = (
        "title",
        "text",
    )


@register(Contact)
class ContactTranslation(TranslationOptions):
    fields = ("working_hours", "address")


@register(Gallery)
class GalleryTranslation(TranslationOptions):
    fields = ("title", "sub_title")


@register(ProductPage)
class ProductPageTranslation(TranslationOptions):
    fields = ("title", "text")


@register(Category)
class CategoryTranslation(TranslationOptions):
    fields = ("title",)


@register(Product)
class ProductPageTranslation(TranslationOptions):
    fields = ("name", "compound", "colour")
