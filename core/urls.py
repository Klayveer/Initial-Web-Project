from django.urls import path
from .views import Index, TopicoView, NewTopico

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('topico/<slug:slug>', TopicoView.as_view(), name="topico"),
    path('new-topico/', NewTopico.as_view(), name='new-topico'),
]