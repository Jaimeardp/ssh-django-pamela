from django.conf.urls import url
from views import session_demo, loginpam
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    #url(r'^sigin/', loginpam, name="_login"),
    url(r'^login/', LoginView.as_view(template_name="accounts/login_form.html"), name="account_login"),
    url(r'^logout/', LogoutView.as_view(), name="account_logout"),
]
