from django.urls import path
from . import views
from django.shortcuts import render

urlpatterns = [
    path('', views.LeadListView.as_view(), name='lead-list'),
    path('new/', views.LeadCreateView.as_view(), name='lead-create'),
    path('<int:lead_id>/followup/', views.FollowUpCreateView.as_view(), name='followup-create'),
    path('<int:pk>/update-status/', views.update_status, name='update-status'),
    path('api/kanban/', views.LeadKanbanAPIView.as_view(), name='kanban-list'),
    path('api/kanban/<int:pk>/', views.LeadKanbanAPIView.as_view(), name='kanban-update'),
    path('kanban/', lambda request: render(request, 'leads/kanban.html'), name='kanban-board'),
] 