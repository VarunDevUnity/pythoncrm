from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Lead, FollowUp
from django.urls import reverse_lazy
from .forms import FollowUpForm
from django.views.decorators.http import require_POST
from django.http import HttpResponseRedirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import LeadSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class LeadListView(LoginRequiredMixin, ListView):
    model = Lead
    template_name = 'leads/lead_list.html'
    context_object_name = 'leads'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Lead'] = Lead
        return context

class LeadCreateView(LoginRequiredMixin, CreateView):
    model = Lead
    template_name = 'leads/lead_form.html'
    fields = ['name', 'email', 'phone', 'company']
    success_url = reverse_lazy('lead-list')

class FollowUpCreateView(LoginRequiredMixin, CreateView):
    model = FollowUp
    template_name = 'leads/followup_form.html'
    form_class = FollowUpForm
    success_url = reverse_lazy('lead-list')

    def form_valid(self, form):
        form.instance.lead_id = self.kwargs['lead_id']
        response = super().form_valid(form)
        lead = form.instance.lead
        lead.last_follow_up = form.instance.follow_up_date
        lead.save()
        return response

@require_POST
def update_status(request, pk):
    lead = get_object_or_404(Lead, pk=pk)
    new_stage = request.POST.get('status')
    if new_stage in dict(Lead.STAGE_CHOICES):
        lead.stage = new_stage
        lead.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/leads/'))

class LeadKanbanAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        leads = Lead.objects.all()
        serializer = LeadSerializer(leads, many=True)
        return Response(serializer.data)

    def patch(self, request, pk):
        try:
            lead = Lead.objects.get(pk=pk)
        except Lead.DoesNotExist:
            return Response({'error': 'Lead not found'}, status=status.HTTP_404_NOT_FOUND)
        stage = request.data.get('stage')
        if stage in dict(Lead.STAGE_CHOICES):
            lead.stage = stage
            lead.save()
            return Response({'success': True})
        return Response({'error': 'Invalid stage'}, status=400)
