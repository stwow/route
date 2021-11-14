from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView
from .models import City
from django.views import View
from .forms import CityForm


def cities(request, pk =None):
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            form.save()
    # if pk:
    #     city = get_object_or_404(City, id = pk)
    #     context = {'object': city}
    #     return render(request, 'cities/detail.html', context)
    form = CityForm()
    qs = City.objects.all()
    lst = Paginator(qs, 5)
    page_number = request.GET.get('page')
    page_obj = lst.get_page(page_number)
    context = {'page_obj': page_obj, 'form': form}
    return render(request, 'cities/home.html', context)


class CityDetailView(DetailView):
    queryset = City.objects.all()
    template_name = 'cities/detail.html'


class CityCreateView(SuccessMessageMixin, CreateView):
    model = City
    form_class = CityForm
    template_name = 'cities/create.html'
    success_url = reverse_lazy('cities:cities')
    success_message = "Город успешно создан"


class CityUpdateView(SuccessMessageMixin, UpdateView):
    model = City
    form_class = CityForm
    template_name = 'cities/update.html'
    success_url = reverse_lazy('cities:cities')
    success_message = "Город успешно отредактирован"


class CityDeleteView(DeleteView):
    model = City
   # template_name = 'cities/delete.html'
    success_url = reverse_lazy('cities:cities')

    def get(self, request, *args, **kwargs):   #удаление - без перехода на форму (т.е. без подтверждения. только по урлу)
        messages.success(request,'Город успешно удалён')
        return self.post(request, *args, **kwargs)


class CityView(ListView):
    paginate_by = 3
    model = City
    template_name = 'cities/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = CityForm()
        context['form'] = form
        return context

