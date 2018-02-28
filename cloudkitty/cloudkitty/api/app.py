import os
import pecan
from pecan import make_app
from pecan.deploy import deploy as pecan_deploy
from paste import deploy as paste_deploy

#from cloudkitty.api.v1 import datamodels
from cloudkitty import config as api_config


from oslo_config import cfg
from oslo_log import log
from _warnings import default_action

LOG = log.getLogger(__name__)

auth_opts = [
    cfg.StrOpt('api_paste_config',
               default="api_paste.ini"),    
    ]
api_opts = [
    cfg.IPOpt('host_ip',
              default='0.0.0.0'),
    cfg.PortOpt('port',
                default=8889),
    cfg.BoolOpt('pecan_debug',
                default=False),
    ]

CONF = cfg.CONF
CONF.register_opts(auth_opts)
CONF.register_opts(api_opts, group='api')


def get_pecan_config():
    filename = api_config.__file__.replace('.pyc', '.py')
    return pecan.configuration.conf_from_file(filename)

def setup_app():   
    
    app_conf = get_pecan_config()

    app = make_app(
        app_conf.app.root,
        logging=getattr(config, 'logging', {}),
        **app_conf
    )
    return app

def load_app():
    cfg_file = None
    cfg_path = cfg.CONF.api_paste_config
    if not os.path.isabs(cfg_path):
        cfg_file = CONF.find_file(cfg_path)
    elif os.path.exists(cfg_path):
        cfg_file = cfg_path

    if not cfg_file:
        raise cfg.ConfigFilesNotFoundError([cfg.CONF.api_paste_config])
    LOG.info("Full WSGI config used %s", cfg_file)
    LOG.info("api paste configutartion file name %s"  %cfg.CONF.api_paste_config)
    appname = "cloudkitty"
    filename = api_config.__file__.replace('.pyc', '.py')
    return pecan_deploy(filename)

def build_wsgi_app(argv=None):
    return load_app()
