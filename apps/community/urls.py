from tornado.web import url

from apps.community.handler import *

urlpattern = (
    url("/groups/", GroupHandler),
)