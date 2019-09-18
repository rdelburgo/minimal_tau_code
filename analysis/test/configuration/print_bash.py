import sys



for i in range (160, 196):
    if i < 160:
        msg1 = 'python test.py configuration_' + str(i) + '.py  /afs/cern.ch/work/r/rdelburg/ntuples/data/tau_out.root  ../output_test/tau_configuration_' + str(i) + '.root'
        msg2 = 'python test.py configuration_' + str(i) + '.py  /afs/cern.ch/work/r/rdelburg/ntuples/data/qcd_out.root  ../output_test/qcd_configuration_' + str(i) + '.root'

    if i >=160:
        msg1 = 'python test.py configuration_' + str(i) + '.py  /afs/cern.ch/work/r/rdelburg/ntuples/data/tau_out_nopu.root  ../output_test/tau_configuration_' + str(i) + '.root'
        msg2 = 'python test.py configuration_' + str(i) + '.py  /afs/cern.ch/work/r/rdelburg/ntuples/data/qcd_out_nopu.root  ../output_test/qcd_configuration_' + str(i) + '.root'



    print msg1
    print msg2
    print ''
    


