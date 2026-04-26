from django.urls import path
from .views import NoteListCreate, NoteDetail

urlpatterns = [
    path("get/notes/", NoteListCreate.as_view()),
    path("get/notes/<int:pk>/", NoteDetail.as_view()),
    path("put/notes/<int:pk>/", NoteDetail.as_view()),
    path("delete/notes/<int:pk>/", NoteDetail.as_view()),
]
