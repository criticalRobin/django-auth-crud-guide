from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.models import User
from apps.user.forms import CustomUserCreationForm as UserForm

# Create your views here.


class UserCreateView(CreateView):
    model = User
    template_name = "create.html"
    form_class = UserForm
    success_url = reverse_lazy("homepage:home")

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
        context["title"] = "Crear Usuario"
        context["list_url"] = reverse_lazy("homepage:home")
        return super().get_context_data(**kwargs)
