from django.shortcuts import render
from .forms import UserRegForm


def register(request):
    register_button = request.POST.get("m-btn-reg")
    name = ''
    email = ''
    id_number = ''
    date_of_birth = ''
    password = ''
    form = UserRegForm(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data.get("name")
        email = form.cleaned_data.get("email")
        id_number = form.cleaned_data.get("id_number")
        date_of_birth = form.cleaned_data.get("date_of_birth")
        password = form.cleaned_data.get("password")

    context = {'form': form, 'name': name, 'email': email,
               'id_number': id_number,
               'date_of_birth': date_of_birth,
               'password': password,
               'register_button': register_button}
    return render(request, 'register.html', context)