from django.conf.urls import url

from .views import ApplicationsView, AllApplicationsView, ApplicationView


app_name = "baserow.api.group"


urlpatterns = [
    url(r"group/(?P<group_id>[0-9]+)/$", ApplicationsView.as_view(), name="list"),
    url(r"(?P<application_id>[0-9]+)/$", ApplicationView.as_view(), name="item"),
    url(r"$", AllApplicationsView.as_view(), name="list"),
]
