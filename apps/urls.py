from django.urls import path

from apps.views import (
    AboutUsView,
    CategoryProductView,
    ContactView,
    GalleryView,
    IndexView,
    ProductInnerView,
    ProductListView,
)

urlpatterns = [
    path("", IndexView.as_view(), name="home"),
    path("contact/", ContactView.as_view(), name="contact"),
    path("about/", AboutUsView.as_view(), name="about"),
    path("gallery/", GalleryView.as_view(), name="gallery"),
    path("category-products/", CategoryProductView.as_view(), name="category-product"),
    path(
        "products/category/<slug:category_slug>/",
        ProductListView.as_view(),
        name="products",
    ),
    path("product/<slug:slug>/", ProductInnerView.as_view(), name="product_detail"),
]
