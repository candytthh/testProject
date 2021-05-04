from django.urls import path
from . import views
from django.contrib import admin


urlpatterns = [
    path('', views.index, name='index'),
    # path('main/', views.index, name='index'),
    path('<int:location_id>', views.detail, name='detail'),
    path('admin/', admin.site.urls),
    path('sockettest/', views.socket_test, name='socket_test'),
]

# urlpatterns is a list, with order
