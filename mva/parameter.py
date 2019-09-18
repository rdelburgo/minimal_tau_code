import sys
import ROOT
from ROOT import *

if sys.argv[-1]== "25ns":
    variable_list=["iso_25", "eta", "pt"]
    variable_type=['F', 'F', 'F']
    cut_sig=TCut("iso_25<800")
    cut_bkg=TCut("iso_25<800")

if sys.argv[-1]== "30ps":
    variable_list=["iso_30", "eta", "pt"]
    variable_type=['F', 'F', 'F']
    cut_sig=TCut("iso_30<800")
    cut_bkg=TCut("iso_30<800")

if sys.argv[-1]== "25ns_nocut":
    variable_list=["iso_25", "eta", "pt"]
    variable_type=['F', 'F', 'F']
    cut_sig=TCut("iso_25")
    cut_bkg=TCut("iso_25")

if sys.argv[-1]== "30ps_nocut":
    variable_list=["iso_30", "eta", "pt"]
    variable_type=['F', 'F', 'F']
    cut_sig=TCut("iso_30")
    cut_bkg=TCut("iso_30")
