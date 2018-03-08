from django.conf.urls import url
from django.contrib.auth.views import logout as logoutview
from django.urls import reverse_lazy

from example.app.views import home_view
from stravauth.views import StravaAuth

urlpatterns = [
    url(r'^$', home_view, name="home"),
    url(r'^login', StravaAuth.as_view(url=reverse_lazy("home")), kwargs={"approval_prompt": "force"}, name="login"),
    url(r'^logout$', logoutview, kwargs={'next_page': '/'}, name="logout"),
]
