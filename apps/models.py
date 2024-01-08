import os
import uuid

from ckeditor.fields import RichTextField
from django.core.validators import FileExtensionValidator, URLValidator
from django.db.models import (CASCADE, CharField, EmailField, FileField,
                              ForeignKey, ImageField, IntegerField, Model,
                              SlugField, URLField)
from slugify import slugify


class ImageDeletionMixin(Model):
    @staticmethod
    def _delete_file(path):
        if os.path.isfile(path):
            os.remove(path)

    def delete_image(self, field_name):
        try:
            image_field = getattr(self, field_name)
            if image_field:
                self._delete_file(image_field.path)
        except AttributeError:
            pass

    def delete(self, *args, **kwargs):
        for field in self._meta.get_fields():
            if isinstance(field, ImageField):
                self.delete_image(field.name)
        super().delete(*args, **kwargs)

    def save(self, *args, **kwargs):
        is_new_instance = not self.pk
        orig = None
        if not is_new_instance:
            orig = self.__class__.objects.get(pk=self.pk)
        super().save(*args, **kwargs)
        if not is_new_instance and orig:
            for field in self._meta.get_fields():
                if isinstance(field, ImageField):
                    new_image_field = getattr(self, field.name)
                    old_image_field = getattr(orig, field.name)
                    if new_image_field != old_image_field:
                        self.delete_image(old_image_field.name)

    class Meta:
        abstract = True


def image_filename(instance, filename):
    extension = filename.split(".")[-1]
    unique_filename = f"{uuid.uuid4()}.{extension}"
    return f"images/{unique_filename}"


# Index Banner


class IndexBanner(Model):
    title = CharField(max_length=255)
    video = FileField(
        upload_to="image_filename",
        null=True,
        validators=[
            FileExtensionValidator(
                allowed_extensions=["MOV", "avi", "mp4", "webm", "mkv"]
            )
        ],
        help_text=(
            "Upload a video file for the banner. Allowed formats: MOV, avi, mp4, webm, mkv.",
        ),
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = " Main Page Banner"
        verbose_name_plural = "Main Page Banner"


class IndexAbout(ImageDeletionMixin, Model):
    title = CharField(max_length=255)
    text = RichTextField()
    image = ImageField(max_length=255, upload_to=image_filename)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "IndexAbout"
        verbose_name_plural = "IndexAbout"


class IndexCategoryText(Model):
    title = CharField(max_length=255)
    sub_title = CharField(max_length=400)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "IndexCategoryText"
        verbose_name_plural = "IndexCategoryText"


# Service


class Service(Model):
    name = CharField(max_length=255, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"


# About Us
class AboutUs(ImageDeletionMixin, Model):
    title = CharField(max_length=255, null=True)
    text_up = RichTextField(null=True)
    image = FileField(max_length=255, upload_to=image_filename)
    text_down = RichTextField(null=True)
    experience = IntegerField(null=True)
    production_area = IntegerField(null=True)
    work_place = IntegerField(null=True)
    monthly_production_output = IntegerField(null=True)

    def __int__(self):
        return self.title

    class Meta:
        verbose_name = "About Us"
        verbose_name_plural = "About Us"


class Features(Model):
    title = CharField(max_length=255, null=True)
    icon = CharField(
        max_length=100,
        null=True,
        blank=True,
        help_text="добавьте сюда только remix icons here https://remixicon.com/",
    )
    text = RichTextField()
    about = ForeignKey(AboutUs, CASCADE, related_name="features")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Feature"
        verbose_name_plural = "Features"


class Clients(ImageDeletionMixin, Model):
    image = ImageField(max_length=255, upload_to=image_filename)

    def __str__(self):
        return self.image.url

    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"


# Contact


class Contact(Model):
    working_hours = CharField(max_length=255, null=True)
    phone_1 = CharField(max_length=25, null=True, blank=True, unique=True)
    phone_2 = CharField(max_length=25, null=True, blank=True, unique=True)
    email = EmailField(max_length=255, unique=True)
    address = CharField(max_length=255)
    map = CharField(max_length=350)

    def __int__(self):
        return self.id

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"


# Socials
class Socials(Model):
    instagram = URLField(
        max_length=255,
        blank=True,
        null=True,
        unique=True,
        validators=[
            URLValidator,
        ],
    )
    whatsup = URLField(
        max_length=255,
        blank=True,
        null=True,
        unique=True,
        validators=[
            URLValidator,
        ],
    )
    youtube = URLField(
        max_length=255,
        blank=True,
        null=True,
        unique=True,
        validators=[
            URLValidator,
        ],
    )
    linkedin = URLField(
        max_length=255,
        blank=True,
        null=True,
        unique=True,
        validators=[
            URLValidator,
        ],
    )
    telegram = CharField(max_length=255, blank=True, null=True, unique=True)

    def __int__(self):
        return self.id


# Gallery
class Gallery(Model):
    title = CharField(max_length=255)
    sub_title = CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Gallery"
        verbose_name_plural = "Galleries"


class Image(ImageDeletionMixin, Model):
    image = ImageField(max_length=255, upload_to=image_filename)
    gallery = ForeignKey(Gallery, CASCADE, related_name="images")

    def __str__(self):
        return self.image.url

    class Meta:
        verbose_name = "Image"
        verbose_name_plural = "Images"


# Product
class ProductPage(Model):
    title = CharField(max_length=255)
    text = RichTextField(null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Product Page"
        verbose_name_plural = "Product Pages"


class Category(ImageDeletionMixin, Model):
    title = CharField(max_length=255, null=True, unique=True)
    image = ImageField(max_length=255, upload_to=image_filename)
    slug = SlugField(max_length=255, unique=True)

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        if not self.pk:  # noqa
            self.slug = slugify(self.title)
        else:
            if self.products.exists():
                old_instance = self.products.first()
                if self.title != old_instance.name:
                    self.slug = slugify(self.title)
            else:
                self.slug = slugify(self.title)

        while Category.objects.filter(slug=self.slug).exclude(pk=self.pk).exists():
            if "-" in self.slug:  # noqa
                parts = self.slug.split("-")
                if parts[-1].isdigit():
                    count = int(parts[-1])
                    self.slug = "-".join(parts[:-1]) + "-" + str(count + 1)
                else:
                    self.slug += "-1"
            else:
                self.slug += "-1"

        super().save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Product(Model):
    name = CharField(max_length=255, unique=True)
    price = IntegerField(default=0)
    compound = CharField(max_length=300)
    size = CharField(max_length=200, null=True, blank=True)
    colour = CharField(max_length=40)
    height_image = IntegerField()
    pockets = IntegerField(default=2)

    category = ForeignKey(Category, CASCADE, related_name="products")

    slug = SlugField(max_length=255, unique=True)

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        if not self.pk:  # Check if it's a new instance (not saved before)
            self.slug = slugify(self.name)
        else:
            try:
                old_instance = Product.objects.get(pk=self.pk)
                if self.name != old_instance.name:
                    self.slug = slugify(self.name)
            except (
                Product.DoesNotExist
            ):  # Handle the case when the object doesn't exist
                pass

        while (
            Product.objects.filter(slug=self.slug).exclude(pk=self.pk).exists()
        ):  # noqa
            if "-" in self.slug:
                parts = self.slug.split("-")
                if parts[-1].isdigit():
                    count = int(parts[-1])
                    self.slug = "-".join(parts[:-1]) + "-" + str(count + 1)
                else:
                    self.slug += "-1"
            else:
                self.slug += "-1"

        super().save(force_insert, force_update, using, update_fields)

    def __int__(self):
        return self.pk

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"


class ProductImages(ImageDeletionMixin, Model):
    image = ImageField(max_length=255, upload_to=image_filename)
    product = ForeignKey(Product, CASCADE, related_name="images")

    def __str__(self):
        return f"{self.product.name}image"


class ProductSize(Model):
    size = CharField(max_length=50, null=True, blank=True)
    product = ForeignKey(Product, CASCADE, related_name="sizes")
