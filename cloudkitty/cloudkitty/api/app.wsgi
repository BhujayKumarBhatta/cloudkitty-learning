from cloudkitty.api import app

application = app.build_wsgi_app(argv=[])

#from pecan.deploy import deploy
#application = deploy('/var/www/simpleapp/config.py')

