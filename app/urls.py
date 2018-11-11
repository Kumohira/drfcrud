
from django.urls import path, include
# from .apiviews import ChoiceList, CreateVote, PollViewSet, UserViewSet, UserCreate#, LoginView  PollList, PollDetail,


from .apiviews import CategoryViewSet, CProduct, RudProduct, ProductsByCategory, ClientViewSet#, UserViewSet
from rest_framework.routers import DefaultRouter

from rest_framework.authtoken import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register('categories', CategoryViewSet, base_name='categories')
# router.register('users', UserViewSet, base_name='users')
router.register('clients', ClientViewSet, base_name='clients')

urlpatterns = [
    # path("login/", LoginView.as_view(), name="login"),
    # path("login/", views.obtain_auth_token, name="login"),
    path("login/", include('rest_framework.urls')),

    path("token/", TokenObtainPairView.as_view()),
    path("token/refresh/", TokenRefreshView.as_view()),

    path("products/", CProduct.as_view(), name="products_list"),
    path("products/<int:pk>/", RudProduct.as_view(), name="products_detail"),
    path("category/<int:pk>/products/", ProductsByCategory.as_view(), name="ProductsByCategory"),

    # path("clients/current/", ClientViewSet, name="clients"),

    # path("polls/<int:pk>/", PollDetail.as_view(), name="polls_detail"),
    # path("polls/<int:pk>/choices/", ChoiceList.as_view(), name="choice_list"),
    # path("polls/<int:pk>/choices/<int:choice_pk>/vote/", CreateVote.as_view(), name="create_vote"),
    # path("users/", UserCreate.as_view(), name="user_create"),


    # path("choices/", ChoiceList.as_view(), name="choice_list"),
    # path("vote/", CreateVote.as_view(), name="create_vote"),
]

urlpatterns += router.urls
