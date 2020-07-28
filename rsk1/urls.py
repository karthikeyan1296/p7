from django.urls import path
from rsk1  import views
app_name="rsk1" #is used to create a namespace(called url mapping)

urlpatterns = [
    path('',views.index,name="index"),
    path('home',views.home,name="home"),
    path('fact/<n>',views.fact,name="fact"),
    path('child',views.child,name="child"),
    path('base',views.base,name="base")
    #path("secondary suffix",address of function,name of mapping)
]
