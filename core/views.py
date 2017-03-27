from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm

from core.models import User


class UserCreateForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("username", "password1", "password2")


class RegisterFormView(FormView):
    form_class = UserCreateForm

    template_name = "core/register.html"

    success_url = "/"

    def form_valid(self, form):
        form.save()

        return super(RegisterFormView, self).form_valid(form)
