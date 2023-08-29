from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from apps.main.models import Author
from apps.main.forms import AuthorForm
from django.urls import reverse_lazy
from django.shortcuts import render


class AuthorListView(ListView):
    model = Author
    template_name = "authors/list.html"

    @method_decorator(login_required(login_url=reverse_lazy("login:login_view")))
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Autores"
        context["list_url"] = reverse_lazy("main:author_list")
        return super().get_context_data(**kwargs)


class AuthorCreateView(CreateView):
    model = Author
    template_name = "authors/create.html"
    form_class = AuthorForm
    success_url = reverse_lazy("main:author_list")

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
        context["title"] = "Crear Autor"
        context["list_url"] = reverse_lazy("main:author_list")
        return super().get_context_data(**kwargs)


class AuthorUpdateView(UpdateView):
    model = Author
    form_class = AuthorForm
    template_name = "authors/create.html"
    success_url = reverse_lazy("main:author_list")

    @method_decorator(login_required(login_url=reverse_lazy("login:login_view")))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Edicion de Autor"
        context["list_url"] = reverse_lazy("main:author_list")
        return context


class AuthorDeleteView(DeleteView):
    model = Author
    template_name = "authors/delete.html"
    success_url = reverse_lazy("main:author_list")

    @method_decorator(login_required(login_url=reverse_lazy("login:login_view")))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Eliminar Autor"
        context["list_url"] = reverse_lazy(self.success_url)
        return context
