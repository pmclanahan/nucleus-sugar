from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.http import HttpResponse

# import session_csrf


# session_csrf.monkeypatch()
admin.autodiscover()  # Discover admin.py files for the admin interface.

urlpatterns = [
    url(r'', include('nucleus.base.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-token-auth/',
        'rest_framework.authtoken.views.obtain_auth_token'),
    url(r'^rna/', include('rna.urls')),

    url(r'', include('django_browserid.urls')),

    url(r'^robots\.txt$', lambda r: HttpResponse(
        "User-agent: *\n%s: /" % 'Allow' if settings.ENGAGE_ROBOTS else 'Disallow',
        mimetype="text/plain")),

    # contribute.json url
    url(r'^(?P<path>contribute\.json)$', 'django.views.static.serve',
        {'document_root': settings.ROOT}),
]
