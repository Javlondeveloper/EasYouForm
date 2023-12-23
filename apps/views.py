from urllib.parse import urlparse

from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import NoReverseMatch
from django.urls.base import resolve, reverse
from django.urls.exceptions import Resolver404
from django.utils import translation
from django.views import View
from django.views.generic import DetailView, ListView

from apps.models import (AboutUs, Category, Clients, Contact, Gallery,
                         IndexAbout, IndexBanner, IndexCategoryText, Product,
                         ProductPage, Service, Socials)


def set_language(request, language):
    view = None

    for lang, _ in settings.LANGUAGES:
        translation.activate(lang)
        try:
            view = resolve(urlparse(request.META.get("HTTP_REFERER")).path)
        except Resolver404:
            pass
        else:
            break

    if view:
        translation.activate(language)
        try:
            next_url = reverse(view.url_name, args=view.args, kwargs=view.kwargs)
            response = HttpResponseRedirect(next_url)
            response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
        except (NoReverseMatch, ObjectDoesNotExist):
            response = HttpResponseRedirect("/")
    else:
        response = HttpResponseRedirect("/")

    return response


class IndexView(View):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        index_banner = IndexBanner.objects.first()
        index_about = IndexAbout.objects.first()
        index_category_text = IndexCategoryText.objects.first()
        services = Service.objects.all()
        contact = Contact.objects.first()
        categories = Category.objects.all()[:4]
        about_us = AboutUs.objects.first()
        clients = Clients.objects.all()
        social = Socials.objects.first()
        context = {
            "index_banner": index_banner,
            "index_about": index_about,
            "services": services,
            "contact": contact,
            "categories": categories,
            "index_category_text": index_category_text,
            "about_us": about_us,
            "clients": clients,
            "social": social,
        }
        return render(request, self.template_name, context)


class ContactView(View):
    template_name = "contact.html"

    def get(self, request, *args, **kwargs):
        contact = Contact.objects.first()
        social = Socials.objects.first()

        context = {
            "contact": contact,
            "social": social,
        }
        return render(request, self.template_name, context)


class AboutUsView(View):
    template_name = "about.html"

    def get(self, request, *args, **kwargs):
        contact = Contact.objects.first()
        social = Socials.objects.first()
        about = AboutUs.objects.first()
        clients = Clients.objects.all()

        context = {
            "contact": contact,
            "social": social,
            "about": about,
            "clients": clients,
        }
        return render(request, self.template_name, context)


class GalleryView(View):
    template_name = "gallery.html"

    def get(self, request, *args, **kwargs):
        contact = Contact.objects.first()
        social = Socials.objects.first()
        clients = Clients.objects.all()
        gallery = Gallery.objects.first()

        context = {
            "contact": contact,
            "social": social,
            "clients": clients,
            "gallery": gallery,
        }
        return render(request, self.template_name, context)


class CategoryProductView(View):
    template_name = "category-product.html"

    def get(self, request, *args, **kwargs):
        contact = Contact.objects.first()
        social = Socials.objects.first()
        clients = Clients.objects.all()
        product_page = ProductPage.objects.first()

        categories = Category.objects.all()
        selected_category = None
        products = Product.objects.all()

        if "category_slug" in kwargs:
            selected_category = Category.objects.get(slug=kwargs["category_slug"])
            products = (
                selected_category.products.all()
            )

        context = {
            "contact": contact,
            "social": social,
            "clients": clients,
            "categories": categories,
            "product_page": product_page,
            "selected_category": selected_category,
            "products": products,
        }
        return render(request, self.template_name, context)


class ProductListView(ListView):
    template_name = "product.html"
    queryset = Product.objects.all()
    context_object_name = "products"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context["social"] = Socials.objects.first()
        context["contact"] = Contact.objects.first()
        context["product_page"] = ProductPage.objects.first()
        return context

    def get_queryset(self):
        queryset = Product.objects.all()

        category_slug = self.kwargs.get("category_slug")
        if category_slug:
            category = get_object_or_404(Category, slug=category_slug)
            queryset = queryset.filter(category=category)

        return queryset


class ProductInnerView(DetailView):
    template_name = "product-inner.html"
    query_pk_and_slug = "slug"
    queryset = Product.objects.all()
    context_object_name = "product"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context["social"] = Socials.objects.first()
        context["contact"] = Contact.objects.first()
        return context
