
from django.urls import path, include
from firstapp.views import view1,view2,GetUsers

urlpatterns = [
    path('a/', view1.as_view(), name='view1'),
    path('b/', view2.as_view(), name='view2'),
    path('users/', GetUsers.as_view(), name='get-users'),
]
