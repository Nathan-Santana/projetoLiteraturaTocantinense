from django.contrib import admin
from django.urls import path, include
from aplicacao.urls import router

urlpatterns = [
    path('api/v1/', include(router.urls)),   
    path('admin/', admin.site.urls),
    path('auth/', include('rest_framework.urls'))
]
