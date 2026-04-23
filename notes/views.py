from django.shortcuts import render

# Create your views here.
from rest_framework import generics
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

        return queryset


class NoteDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Handles GET (specific ID), PUT (update), and DELETE by ID.
    """

    queryset = Note.objects.all()
    serializer_class = NoteSerializer
