from django.urls import path

from .views import (
    get_katas,
    kata_list_view,
    detail_hx,
    more_detail_hx,
    update_hx,
    delete_hx,
    search_view,
    save_all_katas,
)


app_name='katas'
urlpatterns = [
    path('', kata_list_view, name='list'),
    path('get-katas/', get_katas, name='get_katas'),
    path('save-all-katas/', save_all_katas, name='save_all_katas'),
    path('search/', search_view, name='search'),
    path('hx/<slug:slug>/update/', update_hx, name='update_hx'),
    path('hx/<slug:slug>/delete/', delete_hx, name='delete_hx'),
    path('hx/<slug:slug>/more/', more_detail_hx, name='more_detail_hx'),
    path('hx/<slug:slug>/', detail_hx, name='detail_hx'),
]