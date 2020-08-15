from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views.generic import CreateView, FormView
from .forms import UserCreationForm, UserLoginForm


class RegisterView(CreateView):
    template_name = 'accounts/register.html'
    form_class = UserCreationForm

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()

        messages.success(self.request, 'Usuário criado com sucesso.')
        return redirect(reverse_lazy('login'))