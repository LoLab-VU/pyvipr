from ._version import version_info, __version__

from .pysbviz import pysbViz
from .views import *


def _jupyter_nbextension_paths():
    return [{
        'section': 'notebook',
        'src': 'static',
        'dest': 'viz-pysb-widget',
        'require': 'viz-pysb-widget/extension'
    }]


__all__ = ['pysbViz'] + views.__all__
