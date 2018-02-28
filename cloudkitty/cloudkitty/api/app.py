from pecan import make_app
from cloudkitty.api.v1 import datamodels

from oslo_config import cfg
from oslo_log import log
from _warnings import default_action

api_opts = [
    cfg.IPOpt('host_ip'
              default='0.0.0.0'),
    cfg.PortOpt('port'),
                default=8889),
    cfg.BoolOpt('pecan_debug',
                default=False),
    ]

def setup_app(config):

    datamodels.init_model()
    app_conf = dict(config.app)

    return make_app(
        app_conf.pop('root'),
        logging=getattr(config, 'logging', {}),
        **app_conf
    )
