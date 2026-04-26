from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Note
from .serializers import NoteSerializer

class NoteListCreate(generics.ListCreateAPIView):
    serializer_class = NoteSerializer

    def get_queryset(self):
        queryset = Note.objects.all()

        # Requirement: Search notes by text (?searchtext=games)
        search_query = self.request.query_params.get("searchtext")
        if search_query:
            queryset = queryset.filter(text__icontains=search_query)

        # Requirement: Fetch notes between date range (?start=2026-01-01&end=2026-12-31)
        start_date = self.request.query_params.get("start")
        end_date = self.request.query_params.get("end")
        if start_date and end_date:
            queryset = queryset.filter(created_at__range=[start_date, end_date])

        # --- ADDED: Fetch by priority (?priority=High) ---
        priority_query = self.request.query_params.get("priority")
        if priority_query:
            queryset = queryset.filter(priority=priority_query)

        return queryset


class NoteDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Handles GET (specific ID), PUT (update), and DELETE by ID.
    """
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    # --- ADDED: Constraint for priority change ---
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        
        # Check if the note is already marked as done
        if instance.is_done:
            # If they are trying to change the priority field specifically
            if 'priority' in request.data and request.data['priority'] != instance.priority:
                return Response(
                    {"error": "Cannot change priority of a note that is already marked as done."},
                    status=status.HTTP_400_BAD_REQUEST
                )
                
        return super().update(request, *args, **kwargs)