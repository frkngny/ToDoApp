from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('accounts.urls'), name='accounts'),
    path('notes/', include('notes.urls'), name='notes'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

