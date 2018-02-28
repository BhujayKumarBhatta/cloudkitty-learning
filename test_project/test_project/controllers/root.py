from pecan import expose, redirect
from webob.exc import status_map


class BooksSection(object):
    @expose()
    def index(self):
        return "Welcome to Book Section"

    @expose()
    def bestsellers(self):
        return "here are the top 5 books"

class Catalog(object):
    @expose()
    def index(self):
        return "Welcome to the catalog page"

    books = BooksSection()

class RootController(object):

    @expose()
    def index(self):
        return "Welcome to the Store"

    catalog = Catalog()
