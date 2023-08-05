from django.urls import path
from . import views

urlpatterns = [
    path("places/", views.PlacesViewset.as_view(), name="place"),
    path("places/<uuid:place_id>/", views.PlacesViewset.as_view(), name="place-delete"),
    path("places/search/", views.PlaceSearchViewset.as_view(), name="place-search"),
    path("places/html-view/", views.PlaceHTMLViewset.as_view(), name="place-html-view"),
]
