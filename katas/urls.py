from django.urls import path

from .views import (
    get_katas,
    kata_list_view,
    kata_detail_view,
    kata_create_view,
    kata_update_view,
    kata_delete_view,
    detail_hx,
    more_detail_hx,
    update_hx,
    delete_hx,
    SeachResultsListView,
)


app_name='katas'
urlpatterns = [
    path('', kata_list_view, name='list'),
    path('get-katas/', get_katas, name='get_katas'),
    path('create/', kata_create_view, name='create'),
    path('search/', SeachResultsListView.as_view(), name='search'),
    path('hx/<slug:slug>/update/', update_hx, name='update_hx'),
    path('hx/<slug:slug>/delete/', delete_hx, name='delete_hx'),
    path('hx/<slug:slug>/more/', more_detail_hx, name='more_detail_hx'),
    path('hx/<slug:slug>/', detail_hx, name='detail_hx'),
    path('<slug:slug>/delete/', kata_delete_view, name='delete'),
    path('<slug:slug>/update/', kata_update_view, name='update'),  
    path('<slug:slug>/', kata_detail_view, name='detail')
]