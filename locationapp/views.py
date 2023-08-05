from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from .models import Place
from rest_framework.pagination import PageNumberPagination
from .serializers import PlaceSerializer
from django.db.models import Q
from django.contrib.gis.geos import Point

# Create your views here.


class PlacesViewset(APIView):
    def get(self, request):
        paginator = PageNumberPagination()
        places = Place.objects.all()
        paginated_places = paginator.paginate_queryset(places, request)
        places_list = [place.get_details() for place in paginated_places]
        return paginator.get_paginated_response(places_list)

    def post(self, request):
        place_serializer = PlaceSerializer(data=request.data)

        if not place_serializer.is_valid():
            return Response(status=400, data=place_serializer.errors)

        serialized_data = place_serializer.validated_data

        name = serialized_data.get("name")
        description = serialized_data.get("description")
        latitude = serialized_data.get("latitude")
        longitude = serialized_data.get("longitude")

        co_ordinates = Point(longitude, latitude)

        try:
            place_instance, created = Place.objects.get_or_create(
                name=name, description=description, location=co_ordinates
            )
            if not created:
                return Response(
                    status=400, data=f"{place_instance.name} Place Already exists."
                )
            else:
                place_instance.save()
        except Exception as e:
            raise e
                
        return Response(
            status=201, data=f"{place_instance.name} Place Added Successfully"
        )

    def delete(self, request, place_id):
        place_instance = Place.objects.filter(place_id=place_id).last()

        if not place_instance:
            return Response(status=400, data="Invalid Place ID.")

        place_instance.delete()

        return Response(status=200, data="Place Deleted Successfully.")


class PlaceSearchViewset(APIView):
    def get(self, request):
        search = request.query_params.get("search", "")
        place_instances = Place.objects.filter(
            Q(name__icontains=search) | Q(description__icontains=search)
        )
        place_list = [place.get_details() for place in place_instances]
        return Response(status=200, data=place_list)


class PlaceHTMLViewset(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "place_list.html"

    def get(self, request):
        places = Place.objects.all()
        places_list = [place.get_details() for place in places]
        return Response({"places_list": places_list})
