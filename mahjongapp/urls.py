from django.urls import path
from .views import indexfunc, loginfunc, historyTopfunc, historyDetailfunc, historyDetailAddfunc, userCtlfunc

urlpatterns = [
    path('index/', indexfunc, name='index'),
    path('login/', loginfunc, name='login'),
    path('', historyTopfunc, name='historyTop'),
    path('historyDetail/', historyDetailfunc, name='historyDetail'),
    path('historyDetailAdd/', historyDetailAddfunc, name='historyDetailAdd'),
    path('userCtl/', userCtlfunc, name='userCtl'),
]
