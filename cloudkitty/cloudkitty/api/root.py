from pecan import expose, redirect
from webob.exc import status_map
from cloudkitty.api.v1 import controllers as v1_api


class RootController(object):

    @expose()
    def index(self):
        return "Home page"

    v1 = v1_api.V1Controller()
