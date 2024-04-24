from django.urls import path
from .import views
urlpatterns = [
    path('',views.AddSudent, name='AddSudent'),
    path('delete/<int:id>/', views.DeleteStudent, name='DeleteStudent'),
    path('update<int:id>/', views.UpdateStudent, name='StudentUpdate'),
]