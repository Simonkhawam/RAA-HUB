from django.urls import path
from .views import (
    ComandaCreateView, ComandaListView, ComandaUpdateView, ComandaDeleteView,
    UtilizatorCreateView, UtilizatorListView, UtilizatorUpdateView, UtilizatorDeleteView
)
urlpatterns = [
    path('comanda/', ComandaListView.as_view(), name='comanda-list'),
    path('comanda/create/', ComandaCreateView.as_view(), name='comanda-create'),
    path('comanda/update/<int:pk>/', ComandaUpdateView.as_view(), name='comanda-update'),
    path('comanda/delete/<int:pk>/', ComandaDeleteView.as_view(), name='comanda-delete'),
    path('utilizator/', UtilizatorListView.as_view(), name='utilizator-list'),
    path('utilizator/create/', UtilizatorCreateView.as_view(), name='utilizator-create'),
    path('utilizator/update/<int:pk>/', UtilizatorUpdateView.as_view(), name='utilizator-update'),
    path('utilizator/delete/<int:pk>/', UtilizatorDeleteView.as_view(), name='utilizator-delete'),
]
