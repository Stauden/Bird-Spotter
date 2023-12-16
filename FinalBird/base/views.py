from typing import Any
from .forms import StatusForm
from django.db.models.query import QuerySet
from .models import Task
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.models import User

#Design view 
#def home(request):
    #return render(request, "home.html")

#List structure
#login
class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    field = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')
    
class RegisterPage(FormView):
    template_name = 'base/register.html'
    form_class = UserCreationForm
    redirect_aithenticated_user = True
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage,self).form_valid(form)
    
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(RegisterPage, self).get(*args, **kwargs)


class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(complete=False).count()

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(title__icontains=search_input)
        
        context['search_input'] = search_input
        return context
        
class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'base/task.html'

class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task 
    fields = ['title', 'description', 'wingspan', 'species', 'sex', 'age','injured', 'image', 'complete']
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)   
    
class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'description', 'wingspan', 'species', 'sex', 'age','injured', 'image', 'complete']
    success_url = reverse_lazy('tasks')

class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')

class UserListView(ListView):
    model = User
    template_name = 'home.html'
    context_object_name = 'users'
     
    def get_queryset(self):
        return User.objects.prefetch_related('task_set').all()
    
class StatusUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = StatusForm
    template_name = 'status.html'

    def get_object(self, queryset=None):
        return Task.objects.filter(user=self.request.user).first()
        #obj, created = Task.objects.get_or_create(user=self.request.user)
        #return obj

    def get_success_url(self):
        return reverse_lazy('home')
    
def search_wiki(request, task_id):
    task = get_object_or_404(Task, id=task_id)  # Get Task by ID
    search_term = task.species  # Assuming 'species' is the field you want
    search_url = f'https://www.allaboutbirds.org/news/search/?q={search_term}'
    return redirect(search_url)
