import sys
import os.path as osp

pjpath = osp.dirname(osp.realpath(__file__))
sys.path.append(pjpath)

__APPNAME__ = "EISeg"
__VERSION__ = "0.1.7"  # 目前pypi是0.1.6