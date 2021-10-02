
from django.urls import path, include
# sirve para cargar todo el grupo de rutas estaticas del proyecto (CSS, JS, IMG, otros)
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cms/', include('cms.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# document_root => contenido que renderizara cuando se llame a determinada ruta con su nombre de archivo
