from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('MyBlogSiteApp.urls')),
    path('accounts/', include('django.contrib.auth.urls')), # login va logout sahifasiga o'tish
    path('accounts/', include('accounts.urls')),  # signup sahifasiga o'tish
]
