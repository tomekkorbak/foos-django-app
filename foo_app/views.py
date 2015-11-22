from django.http import HttpResponse
from django.views import generic
from .models import Foo
import json


class IndexView(generic.ListView):
    model = Foo


class DetailView(generic.DetailView):
    model = Foo


def APIView(reqest):
    foos_as_jsons = [foo.as_json() for foo in Foo.objects.all()]
    return HttpResponse(json.dumps(foos_as_jsons), content_type="application/json")