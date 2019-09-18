cd /afs/cern.ch/user/r/rdelburg/new_dir/CMSSW_9_3_2/src/
cmsRun tau_cfg.py
cmsRun jet_cfg.py
cd /afs/cern.ch/user/r/rdelburg/new_dir/CMSSW_9_3_2/src/test


python test.py configuration_0.py  /afs/cern.ch/work/r/rdelburg/ntuples/data/tau_out.root  ../output_test/tau_configuration_0.root
python test.py configuration_0.py  /afs/cern.ch/work/r/rdelburg/ntuples/data/qcd_out.root  ../output_test/qcd_configuration_0.root
