
from django.urls import path, include
from firstapp.views import(
    view1,
    view2,
    GetUsers,
    displayUsers,
    signUp,
    success
)

urlpatterns = [
    path('a/', view1.as_view(), name='view1'),
    path('b/', view2.as_view(), name='view2'),
    path('users/', GetUsers.as_view(), name='get-users'),

    path('users1/', displayUsers, name='display-users'),
    path('signupUsers/',signUp, name = 'signup-user'),
    path('success/',success, name = 'success')
]

