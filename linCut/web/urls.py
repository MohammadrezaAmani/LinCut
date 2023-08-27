from django.urls import path, include

# from .views import index, getLink , LinkViewSet
from web import views
from rest_framework import routers

basename = "web"

# router = routers.DefaultRouter()
# router.register(r"link", LinkDetail)``
urlpatterns = [
    # path('links/', views.Link_list),
    # path('links/<int:pk>/', views.link_detail),
    path("clinks/", views.Link3List.as_view()),
    path("clinks/<int:pk>/", views.Link3Detail.as_view()),
    path("users/", views.UserList.as_view()),
    path("users/<int:pk>/", views.UserDetail.as_view()),
]
