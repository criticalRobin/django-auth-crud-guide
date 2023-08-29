from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy


# Create your views here.
class LoginFormView(LoginView):
    template_name = "login.html"
    success_url = reverse_lazy("homepage:home")

    def dispatch(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect(self.success_url)
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Iniciar Sesión"
        return context


class LogoutFormView(LogoutView):
    def post(self, request, *args, **kwargs):
        if self.request.method == "POST":
            self.request.session.flush()
            self.request.session.clear_expired()
            return redirect("login:login")
        return super().post(request, *args, **kwargs)