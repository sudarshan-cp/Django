from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from jobs.views import home

admin.site.site_header = "Jobnest Administration"
admin.site.site_title = "Jobnest Admin"
admin.site.index_title = "Welcome to Jobnest"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.Acc_urls")),
    path("jobs/", include("jobs.jobs_urls")),
    path("", home, name="home"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
