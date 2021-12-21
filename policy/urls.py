from django.urls import path
from .views import PolicyListView, PolicyUpdateView, PolicyStatView

urlpatterns = [
    path('', PolicyListView.as_view(), name='list'),
    path('<int:pk>/', PolicyUpdateView.as_view(), name='detail'),
    path('stat/', PolicyStatView.as_view(), name='stat'),
]