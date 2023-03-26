from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from config.settings import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('quiz.urls')),
]

if DEBUG:
    urlpatterns += static(
        MEDIA_URL,
        document_root=MEDIA_ROOT
    )
