'''
Module containing tests for DTFitter class
'''
# pylint: disable=import-error
# pylint: disable=no-name-in-module

from dataclasses import dataclass

import pytest
from dmu.logging.log_store   import LogStore

from rx_calibration.hltcalibration               import test_utilities as tut
from rx_calibration.hltcalibration.dt_fitter     import DTFitter

log = LogStore.add_logger('rx_calibration:test_dt_fitter')
# --------------------------------------------
@dataclass
class Data:
    '''
    Class holding shared attributes
    '''
    out_dir    = '/tmp/rx_calibration/tests/fitter'
# --------------------------------------------
@pytest.fixture(scope='session', autouse=True)
def _initialize():
    LogStore.set_level('rx_calibration:dt_fitter', 10)
# --------------------------------------------
def test_simple():
    '''
    Simplest test of Fitter class
    '''

    rdf_dat = tut.get_data_rdf()
    l_comp  = tut.get_fit_components()
    cfg     = tut.get_data_fit_cfg()

    obj = DTFitter(rdf = rdf_dat, components = l_comp, cfg = cfg)
    par = obj.fit()

    print(par)
# --------------------------------------------
