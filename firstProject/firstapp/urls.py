
from django.urls import path, include
from firstapp.views import(
    view1,
    view2,
    GetUsers,
    displayUsers,
    signUp,
    success,
    profile_edit,
    cusmodel_users,
    dynamicUser_edit,
)

urlpatterns = [
    path('a/', view1.as_view(), name='view1'),
    path('b/', view2.as_view(), name='view2'),
    path('users/', GetUsers.as_view(), name='get-users'),

    path('users1/', displayUsers, name='display-users'),
    path('signupUsers/',signUp, name = 'signup-user'),
    path('profileEdit/',profile_edit, name = 'edit-user'),

    path('cusModelUsers/',cusmodel_users, name = 'cus-model-user'),

    path('users/change/<int:id>/', dynamicUser_edit, name= 'dynamic-user-edit'),


    path('success/',success, name = 'success')
]

