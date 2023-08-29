from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from apps.main.models import Publisher
from apps.main.forms import PublisherForm
from django.shortcuts import render


class PublisherListView(ListView):
    model = Publisher
    template_name = "publishers/list.html"

    @method_decorator(login_required(login_url=reverse_lazy("login:login_view")))
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Editoriales"
        context["list_url"] = reverse_lazy("main:publisher_list")
        return super().get_context_data(**kwargs)


class PublisherCreateView(CreateView):
    model = Publisher
    template_name = "publishers/create.html"
    form_class = PublisherForm
    success_url = reverse_lazy("main:publisher_list")

    @method_decorator(login_required(login_url=reverse_lazy("login:login_view")))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(self.success_url)
        self.object = None
        context = self.get_context_data(**kwargs)
        context["form"] = form
        return render(request, self.template_name, context)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Crear Editorial"
        context["list_url"] = reverse_lazy("main:publisher_list")
        return super().get_context_data(**kwargs)


class PublisherUpdateView(UpdateView):
    model = Publisher
    form_class = PublisherForm
    template_name = "publishers/create.html"
    success_url = reverse_lazy("main:publisher_list")

    @method_decorator(login_required(login_url=reverse_lazy("login:login_view")))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Edicion de Editorial"
        context["list_url"] = reverse_lazy("main:publisher_list")
        return context


class PublisherDeleteView(DeleteView):
    model = Publisher
    template_name = "publishers/delete.html"
    success_url = reverse_lazy("main:publisher_list")

    @method_decorator(login_required(login_url=reverse_lazy("login:login_view")))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Eliminar Editorial"
        context["list_url"] = reverse_lazy(self.success_url)
        return context
