from django.urls import path, include
from . import views
from django.contrib.auth.views import LogoutView
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete, CustomLoginView, RegisterPage, UserListView, StatusUpdate
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    #home
    #path("", views.home, name="home"),
    path("", UserListView.as_view(), name="home"),
    #list
    path('accounts/login/', CustomLoginView.as_view(), name='login' ),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout' ),
    path('register/', RegisterPage.as_view(), name='register'),

    path('list/', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/',  TaskDetail.as_view(), name='task'),
    path('task-create/', TaskCreate.as_view(), name='task-create'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', TaskDelete.as_view(), name='task-delete'),
    path('status/update/', StatusUpdate.as_view(), name='status-update'),
    path('search/<int:task_id>/', views.search_wiki, name='wiki')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)