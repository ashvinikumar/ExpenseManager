from django.conf.urls import patterns, include, url
from django.contrib import admin
from registration.backends.simple.views import RegistrationView


class MyRegistrationView(RegistrationView):
    def get_success_url(self, request, user):
        return '/expense/'


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'expense_manager.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^expense/', include('expense.urls')),
    url(r'^accounts/', include('registration.backends.simple.urls')),
)