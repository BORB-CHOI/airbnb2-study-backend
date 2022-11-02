from django.urls import path
from .views import Wishlists, WishlistDetail, RoomLikeToggle, ExperienceLikeToggle

urlpatterns = [
    path("", Wishlists.as_view()),
    path("<int:pk>", WishlistDetail.as_view()),
    path("<int:pk>/rooms/<int:room_pk>", RoomLikeToggle.as_view()),
    path("<int:pk>/experiences/<int:experience_pk>", ExperienceLikeToggle.as_view()),
]
