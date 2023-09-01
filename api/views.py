from rest_framework import viewsets
from .sereializers import ProgrammerSerializer
from .models import Programmer

# Create your views here.
class ProgrammerViewSet(viewsets.ModelViewSet):
    #obtener los elementos
    queryset = Programmer.objects.all()
    serializer_class = ProgrammerSerializer