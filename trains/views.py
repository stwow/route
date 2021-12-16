from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView
from .models import Train
from django.views import View
from .forms import TrainForm


def home(request, pk =None):
    qs = Train.objects.all()
    lst = Paginator(qs, 5)
    page_number = request.GET.get('page')
    page_obj = lst.get_page(page_number)
    context = {'page_obj': page_obj}
    return render(request, 'trains/home.html', context)


class TrainView(ListView):
    paginate_by = 3
    model = Train
    template_name = 'trains/home.html'


class TrainDetailView(DetailView):
    queryset = Train.objects.all()
    template_name = 'trains/detail.html'


class TrainCreateView(SuccessMessageMixin, CreateView):
    model = Train
    form_class = TrainForm
    template_name = 'trains/create.html'
    success_url = reverse_lazy('trains:trains')
    success_message = "Поезд успешно создан"


class TrainUpdateView(SuccessMessageMixin, UpdateView):
    model = Train
    form_class = TrainForm
    template_name = 'trains/update.html'
    success_url = reverse_lazy('trains:trains')
    success_message = "Поезд успешно отредактирован"


class TrainDeleteView(DeleteView):
    model = Train
   # template_name = 'trains/delete.html'
    success_url = reverse_lazy('trains:trains')

    def get(self, request, *args, **kwargs):   #удаление - без перехода на форму (т.е. без подтверждения. только по урлу)
        messages.success(request,'Поезд успешно удалён')
        return self.post(request, *args, **kwargs)



