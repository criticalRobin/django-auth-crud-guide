from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from apps.main.models import Book
from apps.main.forms import BookForm
from django.shortcuts import render
from django.urls import reverse_lazy


class BookListView(ListView):
    model = Book
    template_name = "books/list.html"

    @method_decorator(login_required(login_url=reverse_lazy("login:login_view")))
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Libros"
        context["list_url"] = reverse_lazy("main:book_list")
        return super().get_context_data(**kwargs)


class BookCreateView(CreateView):
    model = Book
    template_name = "books/create.html"
    form_class = BookForm
    success_url = reverse_lazy("main:book_list")

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
        context["title"] = "Crear Libro"
        context["list_url"] = reverse_lazy("main:book_list")
        return super().get_context_data(**kwargs)


class BookUpdateView(UpdateView):
    model = Book
    template_name = "books/create.html"
    form_class = BookForm
    success_url = reverse_lazy("main:book_list")

    @method_decorator(login_required(login_url=reverse_lazy("login:login_view")))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Edicion de Libro"
        context["list_url"] = reverse_lazy("main:book_list")
        return context


class BookDeleteView(DeleteView):
    model = Book
    template_name = "books/delete.html"
    success_url = reverse_lazy("main:book_list")

    @method_decorator(login_required(login_url=reverse_lazy("login:login_view")))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Eliminar Libro"
        context["list_url"] = reverse_lazy(self.success_url)
        return context
