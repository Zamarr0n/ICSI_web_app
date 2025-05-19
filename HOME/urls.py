from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import blog , DetailBlog

urlpatterns = [ 
    path("", views.index,name="index"),
    path ("marcas/", views.marcas, name="marcas"),
    path ("servicios/", views.servicios, name="servicios"),
    path ("nosotros/", views.nosotros, name="nosotros"),
    #este es el apartado para el blog:
    # path("blog/", views.blog, name="blog")
    path("blog/", blog.as_view(), name ="blog"),
    path("article/<int:pk>", DetailBlog.as_view(), name="blog_complete"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)