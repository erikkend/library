from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import DetailView
from django.contrib.auth import get_user_model
from users.forms import CustomUserCreationForm, CustomUserChangeForm

User = get_user_model()


class Register(View):
    template_name = 'registration/register.html'

    def get(self, request):
        context = {
            'form': CustomUserCreationForm
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = CustomUserCreationForm(data=request.POST)

        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=password)
            login(request, user)
            return redirect('home')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)


class UserChange(View):
    template_name = 'registration/user_change.html'

    def get(self, request):
        context = {
            'form': CustomUserChangeForm
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = CustomUserChangeForm(data=request.POST)

        if form.is_valid():
            form.save()
            cl_data = form.cleaned_data()
            print(cl_data)
            return redirect('home')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)


class ProfileView(DetailView):
    model = User
    template_name = 'users/profile.html'

    def get_context_data(self, *args, **kwargs):
        users = User.objects.all()
        context = super(ProfileView, self).get_context_data(**kwargs)
        page_user = get_object_or_404(users, id=self.kwargs['pk'])
        context['page_user'] = page_user

        return context
