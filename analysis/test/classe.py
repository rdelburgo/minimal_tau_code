import math
import sys
import numpy
from ROOT import TLorentzVector
def my_import(name):
        m = __import__(name)
        for n in name.split(".")[1:]:
            m = getattr(m, n)
        return m

sys.path.append('configuration/configurations/')
m = __import__(sys.argv[1][:-3])
m = my_import(sys.argv[1][:-3])
namespace = {}
globals().update(vars(m))
globals().update(namespace)

target_value = time_variable
smear = False
smear_how_much=0
# marker magellano                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
if target_value != 0.03:
    smear_how_much = pow(pow(target_value,2) - pow(0.03,2),0.5)
    smear = True
rand = Trandom3()


electron_mass_pdg=0.05485
muon_mass_pdg=0.10565
tau_mass_pdg=1.77686
delta_for_pruning=0.1
time_r = 0.05656 # 40 ps                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
time_s = 10      # ps                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
eff_b = 0.85
eff_f = 0.9

# after shortlisting!                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
# we need for item that have a counterpart:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
# pt_reco and pt_true                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
# eta_reco and eta_true                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     

class taus_machine():
    def __init__(self, tau_reco, tau_mc, jet_mc):
        #tlorenzvector                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
        self.tau_reco = tau_reco
        self.tau_mc = tau_mc
        self.return_value = []
    def matching_and_return(self):
        for i, item_1 in self.tau_reco:
            for k, item_2 in self.tau_mc:
                if deltaR(item_1, item_2)< 0.4:
                    self.return_value.append([i,k,item_1,item_2])




def smear_time(time, time_resolution):
        return_value = 0.0
        if time_resolution == 30.0:
                return_value = time
        if time_resolution != 30.0:
            target_value = time_resolution
            x = pow(pow(target_value,2) - pow(30.0,2),0.5)
        return x

'''                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
def makeitunique_lvector(l=[TLorentzVector()]):                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
    r_list=l                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
    if len(l)>0:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
        item_to_be_deleted=[]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
        for i in range(0,len(l)):                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
            delta_unique=10                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
            for j in range(0,len(l)):                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
                if i != j and j>i:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
                    delta= l[i].DeltaR(l[j])                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
                    if delta<delta_for_pruning:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
                        item_to_be_deleted.append(j)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
                        item_to_be_deleted=list(set(item_to_be_deleted))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
        item_to_be_deleted.sort(reverse=True)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
        if len(item_to_be_deleted)!=0:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
            for i in item_to_be_deleted:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
                del r_list[i]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
    return r_list                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
'''
class get_decay_mc():
    def __init__(self, tree, i):
        self.tree = tree
        self.index = i
        self.pi = 0
        self.pi0 = 0
        self.muon = 0
        self.electron = 0
    def get_decay_mode(self):
        self.last = len(self.tree.truth_tau_daughter_n)
        self.tl = []
        self.pdgid = []
#       print ''                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
        for k in range(0,self.last):
                if self.tree.truth_tau_daughter_n.at(k) == self.index:
#                       print self.tree.truth_tau_daughter_pdg.at(k),  self.tree.truth_tau_daughter_pt.at(k), self.tree.truth_tau_daughter_eta.at(k), self.tree.truth_tau_daughter_phi.at(k)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
                        self.tl.append(TLorentzVector())
                        self.pt = self.tree.truth_tau_daughter_pt.at(k)
                        self.eta = self.tree.truth_tau_daughter_eta.at(k)
                        self.phi = self.tree.truth_tau_daughter_phi.at(k)
                        self.tl[-1].SetPtEtaPhiM(self.pt, self.eta, self.phi,0)

                        self.pdgid.append(self.tree.truth_tau_daughter_pdg.at(k))
        for i,item1 in enumerate(self.tl):
                deltar =[]
                deltapt = []
                for item2,k in enumerate(self.tl):
                        if k>i :
                                deltar.append(self.tl[i].DeltaR(self.tl[k]))
                                # deltapt.append(self.tl[i].Pt()-self.tl[k].Pt())                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
                for j in range(len(deltar),0,-1):
                        if deltar[j] < 0.4 : # and abs(deltapt[j])< 20.0:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
                                del self.tl[j]
                                del self.pdgid[j]


        for k in self.pdgid:
#               print '****' , k                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
                if abs(k) == 211.0:
                    self.pi = self.pi + 1
                if abs(k) == 111.0:
                    self.pi0 = self.pi0 + 1
                if abs(k) == 11.0:
                    self.electron = 1
                if abs(k) == 13.0:
                    self.muon = 1
        return decaymode(self.pi, self.pi0,self.muon, self.electron)

def decaymode(pi=0,pi0=0,muon=0,electron=0):

    value = -1
    if electron!=0:
        value = 'electron'
    if muon!=0:
        value = 'muon'
    if pi==1 and pi0==0:
        value =0
    if pi==1 and pi0==1:
        value =1
    if pi==1 and pi0==2:
        value =2
    if pi==1 and pi0==3:
        value =3
    if pi==1 and pi0>3:
        value =4
    if pi==2 and pi0==0:
        value =5
    if pi==2 and pi0==1:
        value =6
    if pi==2 and pi0==2:
        value =7
    if pi==2 and pi0==3:
        value =8
    if pi==2 and pi0>3:
        value =9
    if pi==3 and pi0==0:
        value =10
    if pi==3 and pi0==1:
        value =11
    if pi==3 and pi0==2:
        value =12
    if pi==3 and pi0==3:
        value =13
    if pi==3 and pi0>3:
        value =14
    if pi>3:
        value= 15
#    if value == -1:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
#        print 'pi, pi0', pi, pi0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           

    return value
def find_decay_mode(dummy=[]):
    value=-1
    prong=dummy.count(211)+dummy.count(-211)
    pi0=dummy.count(111)
    electron=dummy.count(11)+dummy.count(-11)
    muon=dummy.count(13)+dummy.count(-13)
    if electron==0 and muon==0 and (decaymode(prong,pi0) in whichdm):
        value=decaymode
    return value
def deta(eta1=0,phi1=0,eta2=0,phi2=0):
    d_eta=eta1-eta2
    d_phi=phi1-phi2
    dd=math.sqrt(d_eta*d_eta + d_phi*d_phi)
    return dd

class compute_iso:

    def __init__(self, values, time_cut):
        self.values = values
        self.r_value=[]
        self.time_cut = time_cut
        for item in values:
            self.r_value.append(0)

    def fill(self,dz, pt):
        for i in range(0, len(self.values)):
            if abs(dz) < self.values[i]:
                self.r_value[i]=self.r_value[i]+pt
    def fill_in_time(self,dz, dt, pt):
        for i in range(0, len(self.values)):
                if smear == True:
                        # marker magellano                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
                        dt = dt + rand.Gaus(0,smear_how_much)
            if abs(dz) < self.values[i] and abs(dt) <self.time_cut:
                    self.r_value[i]=self.r_value[i]+pt
    def getIso(self):
        return self.r_value

class selection:
    def __init__(self, decay_mode, eta_range, pt_range, max_dz ):
        self.decay_mode = decay_mode
        self.eta_range = eta_range
        self.pt_range = pt_range
        self.max_dz = max_dz
    def check(self,dm, eta, pt, dz, status):
        check_value = False
        if dm in self.decay_mode and abs(eta) > self.eta_range[0] and abs(eta) < self.eta_range[1] and status == status_final :
            if pt > self.pt_range[0] and pt < self.pt_range[1] and abs(dz) < self.max_dz:
                check_value = True
        return check_value

class get_candidate_and_compute_isolations:
    def __init__(self, last, index, iso, tree, eta, phi):
        self.last = last
        self.index = index
        self.iso = iso
        self.tree = tree
        self.eta = eta
        self.phi = phi
    def compute(self, smear = 0.0):
        for k in range(0, self.last):
            iso_cand_id = self.tree.identifier.at(k)
            sig_cand = self.tree.sig_cand.at(k)
            if iso_cand_id == self.index and sig_cand == 0:
                iso_cand_pt = self.tree.pt.at(k)
                iso_cand_eta = self.tree.eta.at(k)
                iso_cand_phi = self.tree.phi.at(k)
                if deta(iso_cand_eta, iso_cand_phi, self.eta, self.phi)<=0.4:
                    iso_cand_dz = self.tree.dz.at(k)
                    iso_cand_dt = self.tree.dt.at(k)
                    #                    self.iso.fill(iso_cand_dz , iso_cand_pt)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
                    self.iso.fill_in_time(iso_cand_dz, iso_cand_dt, iso_cand_pt)

        r_value = self.iso.getIso()
        return r_value













