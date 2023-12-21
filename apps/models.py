import os
import uuid

from ckeditor.fields import RichTextField
from django.core.validators import (FileExtensionValidator, RegexValidator,
                                    URLValidator)
from django.db.models import (CASCADE, CharField, EmailField, FileField,
                              ForeignKey, ImageField, IntegerField, Model,
                              URLField)
from django.db.models.signals import pre_delete
from django.dispatch import receiver


class ImageDeletionMixin(Model):
    class Meta:
        abstract = True

    @staticmethod
    def _delete_file(path):
        if os.path.isfile(path):
            os.remove(path)

    def delete(self, *args, **kwargs):
        for field in self._meta.get_fields():
            if isinstance(field, ImageField):
                image_field = getattr(self, field.name)
                if image_field:
                    self._delete_file(image_field.path)
        super().delete(*args, **kwargs)

    def save(self, *args, **kwargs):
        if self.pk:
            orig = self.__class__.objects.get(pk=self.pk)
            for field in self._meta.get_fields():
                if isinstance(field, ImageField):
                    new_image_field = getattr(self, field.name)
                    old_image_field = getattr(orig, field.name)
                    if new_image_field != old_image_field:
                        self._delete_file(old_image_field.path)
        super().save(*args, **kwargs)


@receiver(pre_delete)
def delete_image_files_on_instance_delete(sender, instance, **kwargs):
    if isinstance(instance, ImageDeletionMixin):
        instance.delete()


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


# Service


class Service(Model):
    name = CharField(max_length=255, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"


# About Us
class AboutUs(Model):
    title = CharField(max_length=255, null=True)
    text_up = RichTextField(null=True)
    image = ImageField(max_length=255, upload_to=image_filename)
    text_down = RichTextField(null=True)
    experience = IntegerField(null=True)
    production_area = IntegerField(null=True)
    work_place = IntegerField(null=True)
    monthly_production_output = IntegerField(null=True)

    def __int__(self):
        return int(self.experience)

    class Meta:
        verbose_name = "About Us"
        verbose_name_plural = "About Us"


class Features(Model):
    title = CharField(max_length=255, null=True)
    text = RichTextField()
    about = ForeignKey(AboutUs, CASCADE, related_name="features")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Feature"
        verbose_name_plural = "Features"


class Clients(Model):
    image = ImageField(max_length=255, upload_to=image_filename)

    def __str__(self):
        return self.image.url

    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"


# Contact


class Contact(Model):
    working_hours = CharField(max_length=255, null=True)
    phone_regex = RegexValidator(regex=r"^\+?1?\d{9,15}$")
    phone_1 = CharField(
        validators=[phone_regex], max_length=17, null=True, blank=True, unique=True
    )
    phone_2 = CharField(
        validators=[phone_regex], max_length=17, null=True, blank=True, unique=True
    )
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


class Image(Model):
    image = ImageField(max_length=255, upload_to=image_filename)
    gallery = ForeignKey(Gallery, CASCADE, related_name="images")

    def __str__(self):
        return self.image.url

    class Meta:
        verbose_name = "Image"
        verbose_name_plural = "Images"
