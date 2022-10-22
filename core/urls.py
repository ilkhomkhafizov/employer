from django.contrib import admin
from django.urls import path, include
from core.config import CONFIG

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('employee.urls'))
]
if CONFIG.debug:
    urlpatterns += [
        path('__debug__/', include('debug_toolbar.urls')),
    ]
