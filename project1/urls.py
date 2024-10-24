"""
URL configuration for project1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('a',views.fun2),
    # path('b',views.my),
    # path('c',views.fun3),
    # path('d',views.fun4),
    # path('e',views.fun5),
    # path('f',views.fun6),
    # path('ab',views.fun7),
    # path('er',views.fun8),
    # path('z',views.add_user),
    # path('data',views.fun9),
    # path('bmodel',views.fun10),
    # path('r',views.fun11),
    # path('u',views.fun12,name='v'),
    # path('o',views.funp),
    # path('l',views.funp1,name='a'),
    # path('r\<int:id>',views.delete_emp,name='delete_emp'),
    # path('x\<int:id>',views.update_emp,name='update_emp'),
    # path('delete_cust/<int:pk>',views.deletecust,name='delete_cust'),
    # path('update_cust/<int:pk>',views.updatecust,name='update_cust'),
    # path('cmodel',views.createcust,name='create_cust'),
    # path('redirectcust',views.cust,name='cust'),
    
    # path('bpbmodeltable',views.bpbcreatef,name='publ'),
    # path('bpbmodelform',views.bpbcreate),
    # path('delete_publ/<int:id>',views.bpbcreatedlt,name='delete_publ'),
    # path('update_publ/<int:id>',views.bpbcreateupdate,name='update_publ'), 
    path('addStudent',views.addStudent),
    path('displayStudents',views.displayStudents,name='displayStudents'),
    path('displaySpecificStudent/<int:id>',views.displaySpecificStudent,name='dss'),
    path('updateStudent/<int:id>',views.updateStudent,name='updateStudent'),
    path('deleteStudent/<int:id>',views.deleteStudent,name='deleteStudent'),

    path('add_organizer',views.add_organizer),
    path('add_event',views.add_event),
    path('display_organizer',views.display_organizer,name='display_organizer'),
    path('display_event',views.display_event,name='display_event'),
    path('update_organizer/<int:id>',views.update_organizer,name='update_organizer'),
    path('update_event/<int:id>',views.update_event,name='update_event'),
    path('delete_organizer/<int:id>',views.delete_organizer,name='delete_organizer'),
    path('delete_event/<int:id>',views.delete_event,name='delete_event'),
]
