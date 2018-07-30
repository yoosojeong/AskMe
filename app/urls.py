from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        regex=r'^UserBox/$',
        view=views.UserBox.as_view(),
        name='UserBox',
    ),
]
 