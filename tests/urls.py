"""
:copyright: (c) 2010 DISQUS.
:license: Apache License 2.0, see LICENSE for more details.
"""
from __future__ import absolute_import, division, print_function, unicode_literals

import nexus
from django.urls import include, path, re_path
from django.contrib import admin
from django.http import HttpResponse
from django.views.generic.base import RedirectView

admin.autodiscover()
nexus.autodiscover()

urlpatterns = [
    path("nexus/", include(nexus.site.urls)),
    re_path(r"^admin/", admin.site.urls),
    path("foo/", lambda request: HttpResponse(), name="gargoyle_test_foo"),
    path("", RedirectView.as_view(url="/nexus/", permanent=False)),
]
