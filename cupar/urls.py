"""cupar URL Configuration

*******************
The `urlpatterns` list routes URLs to views.
*******************

 For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

""" setting the url for 'blog/urls' to ^$ makes the blog/urls the default landing
page for the cupar project and app, because this file is in /cupar/cupar/, ie the 
top level directory. 
"""

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('blog.urls')),
]

"""
Django will now redirect everything that comes into 'http://127.0.0.1:8000/' to blog.urls and look for further instructions there, because of this 2nd entry in urlpatterns.

"""
""" REGEX REMINDER
    ^ for the beginning of the text
    $ for the end of the text
    \d for a digit
    + to indicate that the previous item should be repeated at least once
    () to capture part of the pattern
"""
