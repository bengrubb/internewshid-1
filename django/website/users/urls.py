from django.conf.urls import patterns, url
from django.contrib.auth.views import login, logout

from .views import (
    AddContact, UpdateContact, DeleteContact, ListContacts,
    SendActivationEmailView,
    UpdatePersonalInfo, ListContactsExport
)


urlpatterns = patterns(
    '',
    url(r'login/$', login, name="login"),
    url(r'logout/$', logout, name="logout"),
    url(r'edit/$', AddContact.as_view(), name='contact_add'),
    url(r'edit/(?P<pk>\d+)/$', UpdateContact.as_view(),
        name='contact_update'),
    url(r'delete/(?P<pk>\d+)/$', DeleteContact.as_view(),
        name='contact_delete'),
    url(r'activate/(?P<pk>\d+)/$', SendActivationEmailView.as_view(),
        name='contact_claim_account'),
    url(r'personal/$', UpdatePersonalInfo.as_view(), name='personal_edit'),
    url(r'export_as_csv/$', ListContactsExport.as_view(), {'format': 'csv'},
        name='contact_list_csv'),
    url(r'export_as_excel/$', ListContactsExport.as_view(), {'format': 'excel'},
        name='contact_list_excel'),
    url(r'$', ListContacts.as_view(), name='contact_list'),
)
