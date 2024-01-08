from django.contrib.admin import ModelAdmin
from django.forms import TextInput
from django.forms.widgets import FileInput
from django.utils.html import format_html


class BaseAdmin(ModelAdmin):
    def has_add_permission(self, request):
        existing_count = self.model.objects.count()
        return existing_count < 1


class FilePreviewAdminWidget(FileInput):
    def render(self, name, value, attrs=None, renderer=None):
        output = []

        if value and hasattr(value, "url"):
            file_type = value.name.split(".")[-1].lower()
            if file_type in ["png", "jpg", "jpeg", "gif"]:
                # Display an image tag if the file is an image
                image_html = format_html(
                    '<img src="{}" style="max-width:300px; max-height:300px;" />', value.url
                )
                output.append(image_html)
            elif file_type in ["mp4", "avi", "mov", "wmv"]:
                # Display a video tag if the file is a video
                video_html = format_html(
                    '<video width="300" height="300" controls><source src="{}" type="video/mp4">'
                    'Your browser does not support the video tag.</video>', value.url
                )
                output.append(video_html)
            else:
                # Display a link for other file types
                file_html = format_html(
                    '<p><a href="{}">{}</a></p>',
                    value.url,
                    value.name if hasattr(value, 'name') else str(value),
                )
                output.append(file_html)

        output.append(super().render(name, value, attrs, renderer))
        return format_html("".join(output))


class ImagePreviewAdminWidget(FileInput):
    def render(self, name, value, attrs=None, renderer=None):
        output = []
        if value and hasattr(value, "url"):
            image_html = format_html(
                '<img src="{}" style="max-width:300px; max-height:300px;" />', value.url
            )
            output.append(image_html)
        output.append(super().render(name, value, attrs, renderer))
        return format_html("".join(output))


class VideoPreviewAdminWidget(FileInput):
    def render(self, name, value, attrs=None, renderer=None):
        output = []
        if value and hasattr(value, "url"):
            video_html = format_html(
                '<video width="320" height="240" controls><source src="{}" type="video/mp4">Your browser does not support the video tag.</video>',
                value.url,
            )
            output.append(video_html)
        output.append(super().render(name, value, attrs, renderer))
        return format_html("".join(output))


class YouTubeVideoAdminWidget(TextInput):
    def render(self, name, value, attrs=None, renderer=None):
        output = []
        if value:
            output.append(
                format_html(
                    '<iframe width="320" height="240" src="{}" frameborder="0" allowfullscreen></iframe>',
                    value,
                )
            )
        output.append(super().render(name, value, attrs, renderer))
        return format_html("".join(output))
