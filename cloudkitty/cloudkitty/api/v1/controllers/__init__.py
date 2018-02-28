import pecan
from pecan import expose

from cloudkitty.api.v1.controllers import storage as storage_api


class V1Controller(object):

    @expose()
    def index(self):
        return "controllers init page"
    
    storage = storage_api.StorageController()
