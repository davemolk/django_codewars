from django.urls import path

from .views import (
    get_katas,
    kata_list_view,
    kata_detail_view,
    kata_create_view,
    kata_update_view,
    kata_delete_view,
)


app_name='katas'
urlpatterns = [
    path('', kata_list_view, name='list'),
    path('get-katas/', get_katas, name='get_katas'),
    path('create/', kata_create_view, name='create'),
    path('<slug:slug>/delete/', kata_delete_view, name='delete'),
    path('<slug:slug>/update/', kata_update_view, name='update'),  
    path('<slug:slug>/', kata_detail_view, name='detail')
]