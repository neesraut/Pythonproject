
from django.urls import path, include
from MyLibrary.views import(
  libraryHome
)

urlpatterns = [
     path('library/',libraryHome, name = 'library-Home')
]

