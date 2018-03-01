import pecan
from pecan import make_app
from pecan.deploy import deploy as pecan_deploy
from cloudkitty import config as api_config


def get_pecan_config():
    filename = api_config.__file__.replace('.pyc', '.py')
    return pecan.configuration.conf_from_file(filename)

def setup_app(pecan_config=None, extra_hooks=None):    
    app_conf = get_pecan_config()
    app = make_app(
        app_conf.app.root,
        logging=getattr(app_conf, 'logging', {}),        
    )
    return app

def load_app():    
    filename = api_config.__file__.replace('.pyc', '.py')
    return pecan_deploy(filename)

def build_wsgi_app(argv=None):
    return load_app()


#(pecan-env) bhujay@ubuntu:~/eclipse-workspace/cloudkitty-learning/cloudkitty$ python setup.py devel