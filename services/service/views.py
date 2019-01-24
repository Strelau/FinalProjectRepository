# from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView

from .models import Tailor


class TailorListView (DetailView):
    model = Tailor
    fields = '__all__'
    success_url = reverse_lazy("/")

def tailor_view(request, id):
    tailor = Tailor.objects.filter(pk=id)

    if len(tailor) == 0:
        return HttpResponse('nie ma')

    tailor = tailor[0]
    # return  HttpResponse(tailor.name)
    return render(request, 'tailor_detail.html', {'tailor': tailor})

class TailorListViev(View):
    def get(self, request):
        tailorers = Tailor.objects.all
        return render(request, "tailor_list.html", {"tailorers": tailorers})






