from urllib.parse import urlparse

import requests
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
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
    for lang, _ in settings.LANGUAGES:
        translation.activate(lang)
        try:
            view = resolve(urlparse(request.META.get("HTTP_REFERER")).path)
        except Resolver404:
            view = None
        if view:
            break
    if view:
        translation.activate(language)
        next_url = reverse(view.url_name, args=view.args, kwargs=view.kwargs)
        response = HttpResponseRedirect(next_url)
        response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
    else:
        response = HttpResponseRedirect("/")
    return response


class IndexView(View):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        index_banner = IndexBanner.objects.first()
        title_words = index_banner.title.split(" ")
        first_part = " ".join(title_words[:2])
        second_part = " ".join(title_words[2:]) if len(title_words) > 2 else ""

        index_about = IndexAbout.objects.first()
        index_category_text = IndexCategoryText.objects.first()
        services = Service.objects.all()
        contact = Contact.objects.first()
        categories = Category.objects.all()[:8]
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
            "first_part_title": first_part,
            "second_part_title": second_part,
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
    template_name = "about2.html"

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
            products = selected_category.products.all()

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
    template_name = "product-inner2.html"
    query_pk_and_slug = "slug"
    queryset = Product.objects.all()
    context_object_name = "product"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            {
                "social": Socials.objects.first(),
                "contact": Contact.objects.first(),
                "same_products": Product.objects.filter(
                    category=self.object.category
                ).exclude(pk=self.object.pk)[:10],
            }
        )
        return context

    def post(self, request, *args, **kwargs):  # noqa
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        information = request.POST.get("information")
        selected_size = request.POST.get("selected_size")

        text = (
            f"Вам отправили заявку:\n\n👩‍🦰👨‍🦰 Имя: {name}\n☎️ Номер телефона: {phone} \n📏 "
            f"Размер: {selected_size}\n\nДополнительная информация: {information}"
        )
        token = "5639438823:AAHXtBfhuexxbhIUjOZ1BYpnAqNLd00DcSU"
        user_ids = ["1237819772"]

        for user_id in user_ids:
            url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={user_id}&text={text}"

            try:
                response = requests.get(url)
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                print(f"Request to Telegram API failed: {e}")

        return redirect(reverse("home"))
