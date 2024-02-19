
from django.urls import path
from .views import Journel,PublishersList

urlpatterns=[ 
    path("test/", Journel.as_view(), name="create_views"),
        path("tester/<int:pk>/", Journel.as_view(), name="create_views"),
        path("publisher/", PublishersList.as_view(), name="publisher_list"),
        path("publisher/<int:pk>/", PublishersList.as_view() , name="lost" )
]