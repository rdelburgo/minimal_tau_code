// system include files
#include <memory>
#include "CommonTools/UtilAlgos/interface/TFileService.h"                    
#include "DataFormats/Candidate/interface/Candidate.h"
#include "DataFormats/Candidate/interface/LeafCandidate.h"                                                                                        
#include "DataFormats/Common/interface/Handle.h" 
#include "DataFormats/Common/interface/TriggerResults.h"        
#include "DataFormats/GsfTrackReco/interface/GsfTrack.h"        
#include "DataFormats/GsfTrackReco/interface/GsfTrackFwd.h"     
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"   
#include "DataFormats/HepMCCandidate/interface/GenParticleFwd.h"
#include "DataFormats/Math/interface/deltaR.h"                  
#include "DataFormats/MuonReco/interface/MuonQuality.h"
#include "DataFormats/MuonReco/interface/MuonSelectors.h"
#include "DataFormats/PatCandidates/interface/Electron.h"       
#include "DataFormats/PatCandidates/interface/Jet.h"
#include "DataFormats/PatCandidates/interface/MET.h"
#include "DataFormats/PatCandidates/interface/Muon.h"            
#include "DataFormats/PatCandidates/interface/PackedCandidate.h"
#include "DataFormats/PatCandidates/interface/PackedGenParticle.h"
#include "DataFormats/PatCandidates/interface/Photon.h"
#include "DataFormats/PatCandidates/interface/Tau.h"                         
#include "DataFormats/PatCandidates/interface/TriggerEvent.h"
#include "DataFormats/PatCandidates/interface/TriggerObjectStandAlone.h"     
#include "DataFormats/VertexReco/interface/Vertex.h"                         
#include "DataFormats/VertexReco/interface/VertexFwd.h"
#include "EgammaAnalysis/ElectronTools/interface/ElectronEffectiveArea.h"    
#include "FWCore/Common/interface/TriggerNames.h"                            
#include "FWCore/Framework/interface/EDAnalyzer.h"                           
#include "FWCore/Framework/interface/ESHandle.h"                             
#include "FWCore/Framework/interface/Event.h"                                
#include "FWCore/Framework/interface/Frameworkfwd.h"                         
#include "FWCore/Framework/interface/MakerMacros.h"                          
#include "FWCore/Framework/interface/one/EDAnalyzer.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ServiceRegistry/interface/Service.h"                        
#include "PhysicsTools/PatUtils/interface/TriggerHelper.h"
#include "RecoTauTag/RecoTau/interface/ConeTools.h"
#include "RecoTauTag/RecoTau/interface/RecoTauQualityCuts.h"
#include "RecoTauTag/RecoTau/interface/RecoTauVertexAssociator.h"
#include "RecoTauTag/RecoTau/interface/TauDiscriminationProducerBase.h"
//#include "RecoTauTag/phase2Taus/plugins/PATTauClusterVariables.h"
#include "RecoVertex/KalmanVertexFit/interface/KalmanVertexFitter.h"
#include "RecoVertex/PrimaryVertexProducer/interface/VertexHigherPtSquared.h"
#include "RecoVertex/VertexPrimitives/interface/TransientVertex.h"           
#include "RecoVertex/VertexTools/interface/VertexDistance3D.h"               
#include "RecoVertex/VertexTools/interface/VertexDistanceXY.h"               
#include "TTree.h"
#include "TrackingTools/IPTools/interface/IPTools.h"
#include "TrackingTools/Records/interface/TransientTrackRecord.h"
#include "TrackingTools/TransientTrack/interface/TransientTrack.h"           
#include "TrackingTools/TransientTrack/interface/TransientTrackBuilder.h"

#include <math.h>
#include <TMath.h>
#include <TRandom3.h>
#include <TLorentzVector.h>
#include <algorithm>  // std::sort, std::swap
#include <iostream>  // std::cout, std::endl
#include <string>

class tauAnalyzer : public edm::EDAnalyzer {
public:
	explicit tauAnalyzer(const edm::ParameterSet&);
private:
   virtual void analyze(const edm::Event&, const edm::EventSetup&);
   edm::EDGetTokenT<std::vector<pat::Muon>> muonsToken_;
   edm::EDGetTokenT<std::vector<pat::Electron>> elecsToken_;
   edm::EDGetTokenT<std::vector<reco::Vertex>> token_vertices;
   edm::EDGetTokenT<std::vector <reco::GenParticle> > prunedGenToken_;

   edm::EDGetTokenT<pat::PackedCandidateCollection> pfToken_;
   edm::EDGetTokenT<pat::TauCollection> tauToken_;
   edm::EDGetTokenT<std::vector<pat::Jet> > jetSrc_;
   edm::EDGetTokenT<reco::GenJetCollection> genJetSrc_; 

  
   TTree * tree;
   TTree * treemc;
   std::vector<unsigned int>  truth_event_number, event_number;
   std::vector<unsigned int>  truth_run_number, run_number;
   std::vector<double>  pv_z;
   std::vector<double> manyvertex;
   // reco tau
   std::vector<double> tau_dz;
   std::vector<double> tau_pt, tau_eta, tau_phi, tau_mass;
   std::vector<double> tau_decayModeFinding;
   std::vector<int>    tau_decayMode;
   std::vector<double> newChIso30_3,newChIso35_3,newChIso25ns_3;
   // reco jet
   std::vector<double> jet_id;
   std::vector<double> jet_identifier;
   std::vector<double> jet_pt, jet_eta, jet_phi, jet_mass;
   std::vector<double> jet_partonFlavour;
   std::vector<int>    jet_multiplicity;
   // mc taus
   std::vector<double> n_of_truth_taus;
   std::vector<double> truth_tau_status;
   std::vector<double> truth_tau_pt, truth_tau_eta, truth_tau_phi, truth_tau_daughter_pdg,truth_tau_daughter_n;
   std::vector<double> truth_tau_visible_pt,truth_tau_visible_eta,truth_tau_visible_phi;
   std::vector<int>    truth_tau_decay_mod;
   std::vector<int>    truth_tau_mother;
   std::vector<double> truth_tau_daughter_pt, truth_tau_daughter_eta, truth_tau_daughter_phi;
   // Recotau matched to genjet or genlepton
   std::vector<unsigned int> truth_genJet_recoTau_matched;
   std::vector<unsigned int> truth_genTau_recoTau_matched;
   std::vector<unsigned int> truth_genMuon_recoTau_matched;
   std::vector<unsigned int> truth_genEle_recoTau_matched;
   std::vector<unsigned int> truth_tau_matched_Higgs_daughter;
   // Jet MC
   std::vector<double> truth_jet_pt,truth_jet_eta, truth_jet_phi, truth_jet_mother,truth_jet_mass;
   // iso cand info
   std::vector<double> pt, pt2, time0,time,eta,phi,identifier,dz,matched_to_jet, matched_to_tau, sig_cand,dt;
   // function
   reco::Candidate::LorentzVector GetVisibleP4(std::vector<const reco::GenParticle*>& daughters);
   void findDaughters(const reco::GenParticle* mother, std::vector<const reco::GenParticle*>& daughters);
   bool isNeutrino(const reco::Candidate* daughter);

};

tauAnalyzer::tauAnalyzer(const edm::ParameterSet& iConfig)
{
   muonsToken_        = consumes<std::vector<pat::Muon>>(iConfig.getParameter<edm::InputTag>("muonCollection"));
   elecsToken_        = consumes<std::vector<pat::Electron>>(iConfig.getParameter<edm::InputTag>("electronCollection"));
   token_vertices     = consumes<std::vector<reco::Vertex>>(iConfig.getParameter<edm::InputTag>("vertexCollection"));
   prunedGenToken_    = consumes<reco::GenParticleCollection>(iConfig.getParameter<edm::InputTag>("pruned"));
   pfToken_           = consumes<pat::PackedCandidateCollection>(iConfig.getParameter<edm::InputTag>("pfCands"));
   tauToken_          = consumes<pat::TauCollection>(iConfig.getParameter<edm::InputTag>("taus"));
   jetSrc_            = consumes<std::vector<pat::Jet>>(iConfig.getParameter<edm::InputTag>("jets"));
   genJetSrc_         = consumes<reco::GenJetCollection>(iConfig.getParameter<edm::InputTag>("genJets"));

   edm::Service<TFileService> fs;
   tree = fs->make<TTree>("tree", "tree");
   tree->Branch("event_number", &event_number);
   tree->Branch("run_number", &run_number);
   tree->Branch("pv_z", &pv_z);
   tree->Branch("manyvertex",&manyvertex);
   tree->Branch("tau_dz",&tau_dz);
   tree->Branch("tau_decayMode", &tau_decayMode);
   tree->Branch("tau_pt",   &tau_pt);
   tree->Branch("tau_eta",  &tau_eta);
   tree->Branch("tau_phi",  &tau_phi);
   tree->Branch("tau_mass", &tau_mass);
   tree->Branch("tau_decayModeFinding", &tau_decayModeFinding);
   tree->Branch("jet_id",&jet_id);
   tree->Branch("jet_identifier",&jet_identifier);
   tree->Branch("jet_pt",  &jet_pt);
   tree->Branch("jet_eta", &jet_eta);
   tree->Branch("jet_phi", &jet_phi);
   tree->Branch("jet_partonFlavour", &jet_partonFlavour);
   tree->Branch("jet_multiplicity", &jet_multiplicity);
   tree->Branch("truth_genJet_recoTau_matched",&truth_genJet_recoTau_matched);
   tree->Branch("truth_genEle_recoTau_matched",&truth_genEle_recoTau_matched);
   tree->Branch("truth_genMuon_recoTau_matched",&truth_genMuon_recoTau_matched);
   tree->Branch("truth_genTau_recoTau_matched",&truth_genTau_recoTau_matched);


   treemc = fs->make<TTree>("treemc", "treemc");
   treemc->Branch("truth_event_number", &truth_event_number);
   treemc->Branch("truth_run_number", &truth_run_number);
   treemc->Branch("truth_tau_visible_pt",  &truth_tau_visible_pt);
   treemc->Branch("truth_tau_visible_eta",  &truth_tau_visible_eta);
   treemc->Branch("truth_tau_visible_phi",  &truth_tau_visible_phi);
   treemc->Branch("truth_tau_status",  &truth_tau_status);
   treemc->Branch("truth_tau_pt",  &truth_tau_pt);
   treemc->Branch("truth_tau_eta", &truth_tau_eta);
   treemc->Branch("truth_tau_phi", &truth_tau_phi);
   treemc->Branch("truth_tau_decay_mod",&truth_tau_decay_mod);
   treemc->Branch("truth_tau_mother", &truth_tau_mother);
   treemc->Branch("truth_tau_matched_Higgs_daughter", &truth_tau_matched_Higgs_daughter);

   treemc->Branch("truth_tau_daughter_pdg", &truth_tau_daughter_pdg);
   treemc->Branch("truth_tau_daughter_n", &truth_tau_daughter_n);
   treemc->Branch("truth_tau_daughter_pt",  &truth_tau_daughter_pt);
   treemc->Branch("truth_tau_daughter_eta", &truth_tau_daughter_eta);
   treemc->Branch("truth_tau_daughter_phi", &truth_tau_daughter_phi);
   treemc->Branch("truth_jet_mother",  &truth_jet_mother);
   treemc->Branch("truth_jet_pt",  &truth_jet_pt);
   treemc->Branch("truth_jet_eta", &truth_jet_eta);
   treemc->Branch("truth_jet_phi", &truth_jet_phi);
   treemc->Branch("truth_jet_mass", &truth_jet_mass);




   tree->Branch("pt", &pt);
   tree->Branch("eta", &eta);
   tree->Branch("phi", &phi);
   tree->Branch("dz", &dz);
   tree->Branch("dt", &dt);
   tree->Branch("identifier",&identifier);
   tree->Branch("sig_cand",&sig_cand);
   tree->Branch("matched_to_jet", &matched_to_jet);
   tree->Branch("matched_to_tau", &matched_to_tau);

}

void tauAnalyzer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
   edm::Handle<std::vector<pat::Muon>> muons;
   iEvent.getByToken(muonsToken_, muons);

   edm::Handle<std::vector<pat::Electron>> electrons;
   iEvent.getByToken(elecsToken_, electrons);

   edm::ESHandle<TransientTrackBuilder> builder;
   iSetup.get<TransientTrackRecord>().get("TransientTrackBuilder", builder);

   edm::Handle<pat::PackedCandidateCollection> pfs;
   iEvent.getByToken(pfToken_, pfs);

   edm::Handle<pat::TauCollection> taus;
   iEvent.getByToken(tauToken_, taus);

   edm::Handle<std::vector<reco::GenParticle> > genParticles;
   iEvent.getByToken(prunedGenToken_, genParticles);

   edm::Handle<std::vector<pat::Jet> > JetObjects;
   iEvent.getByToken(jetSrc_, JetObjects);

   edm::Handle<reco::GenJetCollection> genJets;
   iEvent.getByToken(genJetSrc_, genJets);
   
   pv_z.clear();
   manyvertex.clear();
   tau_pt .clear(); tau_mass.clear();
   tau_eta.clear(); tau_decayMode.clear();
   tau_phi.clear(); tau_decayModeFinding.clear();

   jet_pt .clear(); jet_partonFlavour.clear(); jet_id.clear(); jet_identifier.clear();
   jet_multiplicity.clear();
   jet_eta.clear();
   jet_phi.clear();

   truth_jet_mother.clear(); truth_jet_pt.clear(); truth_jet_eta.clear();truth_jet_phi.clear();truth_jet_mass.clear();

   newChIso30_3.clear();
   newChIso35_3.clear();
   newChIso25ns_3.clear();
   truth_tau_daughter_n.clear();
   truth_tau_daughter_pdg.clear(); truth_tau_daughter_pt.clear();
   truth_tau_daughter_pt.clear();  
   truth_tau_status.clear();
   truth_tau_decay_mod.clear();
   truth_tau_daughter_eta.clear(); 
   truth_tau_eta.clear(); truth_tau_pt.clear();
   truth_tau_visible_pt.clear(); truth_tau_visible_eta.clear(); truth_tau_visible_phi.clear();
   truth_tau_daughter_phi.clear(); 
   truth_tau_phi.clear();
   
   truth_tau_mother.clear();

   truth_event_number.clear(); event_number.clear();
   truth_run_number.clear(); run_number.clear();
   truth_tau_matched_Higgs_daughter.clear(); 
   truth_genJet_recoTau_matched.clear();
   truth_genEle_recoTau_matched.clear(); 
   truth_genTau_recoTau_matched.clear();
   truth_genMuon_recoTau_matched.clear();
   truth_tau_mother.clear();
   

   pt.clear();
   eta.clear();
   phi.clear();
   dt.clear();
   dz.clear();
   matched_to_jet.clear();
   matched_to_tau.clear();
	   
   tau_dz.clear();
   identifier.clear();
   sig_cand.clear();
   //start the MC things                                                                                                                                   
   for (unsigned int iGenJet = 0; iGenJet < genJets->size() ; ++iGenJet){
     reco::GenJetRef genJet(genJets, iGenJet);
     truth_jet_pt.push_back(genJet->pt());
     truth_jet_eta.push_back(genJet->eta());
     truth_jet_phi.push_back(genJet->phi());
     truth_jet_mass.push_back(genJet->mass());

   }



   std::vector<const reco::GenParticle*> GenTaus;
   std::vector<const reco::GenParticle*> GenMuons;
   std::vector<const reco::GenParticle*> GenElectrons;
   for(std::vector<reco::GenParticle>::const_iterator genParticle = genParticles->begin(); genParticle != genParticles->end(); genParticle++){
     
     if(TMath::Abs(genParticle->pdgId()) == 15) GenTaus.push_back(&(*genParticle));

     if(TMath::Abs(genParticle->pdgId()) == 13) GenMuons.push_back(&(*genParticle));

     if(TMath::Abs(genParticle->pdgId()) == 11) GenElectrons.push_back(&(*genParticle));
   }
   



   int k=0;
   for(auto genTau : GenTaus){
     
     std::vector<const reco::GenParticle*> genTauDaughters;
     findDaughters(genTau, genTauDaughters);
       for(size_t i = 0; i < genTauDaughters.size(); ++i){
	 //	 std::cout << genTauDaughters[i]->status() << ' ' << genTauDaughters[i]->pdgId() << std::endl;
	 if (!isNeutrino(genTauDaughters[i]) && (genTauDaughters[i]->status() == 1 || genTauDaughters[i]->status() == 2)){  
	   truth_tau_daughter_n.push_back(k);
	   truth_tau_daughter_pdg.push_back(genTauDaughters[i]->pdgId());
	   truth_tau_daughter_pt.push_back (genTauDaughters[i]->pt());
	   truth_tau_daughter_eta.push_back(genTauDaughters[i]->eta());
	   truth_tau_daughter_phi.push_back(genTauDaughters[i]->phi());
	 }
       }
       k=k+1;

       reco::Candidate::LorentzVector p4=GetVisibleP4(genTauDaughters);
       truth_tau_visible_pt.push_back(p4.pt());
       truth_tau_visible_eta.push_back(p4.eta());
       truth_tau_visible_phi.push_back(p4.phi());
       truth_tau_status.push_back(genTau->status());
       truth_tau_pt.push_back(genTau->pt());
       truth_tau_eta.push_back(genTau->eta());
       truth_tau_phi.push_back(genTau->phi());

       // checking if the gentau is from the higgs decay
       int matched_truth_tau_matched_Higgs_daughter = 0;
       for(std::vector<reco::GenParticle>::const_iterator genParticle = genParticles->begin(); genParticle != genParticles->end(); genParticle++)
	 if(TMath::Abs(genParticle->pdgId()) == 25)
	   for (size_t j = 0; j < genParticle->numberOfDaughters(); ++j)
	     if (TMath::Abs(genParticle->daughter(j)->pdgId()) == 15) {
	       if (reco::deltaR(genParticle->daughter(j)->eta(), genParticle->daughter(j)->phi(), genTau->eta(), genTau->phi())<0.4)
		 matched_truth_tau_matched_Higgs_daughter=1;
	       if (genParticle->daughter(j)->pt() == genTau->pt())
		 truth_tau_mother.push_back(genParticle->pdgId());
	     }
       truth_tau_matched_Higgs_daughter.push_back(matched_truth_tau_matched_Higgs_daughter);
   }

  // ******
  // VERTEX
  // ******

   edm::Handle<std::vector<reco::Vertex>> reco_vertices;
   iEvent.getByToken(token_vertices, reco_vertices);
   bool first_vertex = true;
   reco::Vertex primary_vertex;
   for (unsigned int vertex=0; vertex < reco_vertices->size(); ++vertex) {
     manyvertex.push_back(vertex);
     if (    // Criteria copied from twiki (mythical)
         !((*reco_vertices)[vertex].isFake())
         && ((*reco_vertices)[vertex].ndof() > 4)
         && (fabs((*reco_vertices)[vertex].z()) <= 24.0)
         && ((*reco_vertices)[vertex].position().Rho() <= 2.0)
        ) {
         if (first_vertex) {
           first_vertex = false;
           primary_vertex=(*reco_vertices)[vertex];
	   pv_z.push_back((*reco_vertices)[vertex].z());
         }
     }
   }

   int counter;
   counter=0;
   for (unsigned int iTau=0;iTau!=taus->size();++iTau) {
     pat::Tau tau = taus->at(iTau);
     pat::PackedCandidate const* packedLeadTauCand = dynamic_cast<pat::PackedCandidate const*>(tau.leadChargedHadrCand().get());
     tau_dz.push_back(packedLeadTauCand->dz());
     tau_pt.push_back (tau.pt());
     tau_eta.push_back(tau.eta());
     tau_phi.push_back(tau.phi());
     tau_decayMode.push_back(tau.decayMode());
     tau_mass.push_back(tau.mass());
     tau_decayModeFinding.push_back(tau.tauID("decayModeFinding"));

     //matching to gentau genele genmuon and genjet
     int genTaumatched=0;
     for (unsigned int iGenJet = 0; iGenJet < genJets->size() ; ++iGenJet){  
       reco::GenJetRef genJet(genJets, iGenJet);
       if (reco::deltaR(tau.eta(), tau.phi(), genJet->eta(), genJet->phi())<=0.4)
	 genTaumatched = 1;
       if (genTaumatched != 1)
	 genTaumatched = 0;
     }
     truth_genJet_recoTau_matched.push_back(genTaumatched);
     genTaumatched=0;
     for(auto genEle : GenElectrons){
       if (reco::deltaR(tau.eta(), tau.phi(), genEle->eta(), genEle->phi())<=0.4)
	 genTaumatched = 1;
       if (genTaumatched != 1)
	 genTaumatched = 0;
     }
     truth_genEle_recoTau_matched.push_back(genTaumatched);
     genTaumatched=0;
     for(auto genMuon : GenMuons){
       if (reco::deltaR(tau.eta(), tau.phi(), genMuon->eta(), genMuon->phi())<=0.4)
	 genTaumatched = 1;
       if (genTaumatched != 1)
	 genTaumatched = 0;
     }
     truth_genMuon_recoTau_matched.push_back(genTaumatched);
     genTaumatched=0;
     for(auto genTau : GenTaus){
       std::vector<const reco::GenParticle*> genTauDaughters;                                                                                          
       findDaughters(genTau, genTauDaughters);
       reco::Candidate::LorentzVector p4=GetVisibleP4(genTauDaughters);
       if (reco::deltaR(tau.eta(), tau.phi(), p4.eta(), p4.phi())<=0.4)
	 genTaumatched = 1;
       if (genTaumatched != 1)
	 genTaumatched = 0;
     }
     truth_genTau_recoTau_matched.push_back(genTaumatched);
	    
     

     std::vector<pat::PackedCandidate const*> packedCHIsoTauCands;
     for(auto cand : tau.isolationChargedHadrCands() ){
       pat::PackedCandidate const* tempIsoCand = dynamic_cast<pat::PackedCandidate const*>(cand.get());
       packedCHIsoTauCands.push_back(tempIsoCand);
     }
     std::vector<pat::PackedCandidate const*> packedCHSigTauCands;
     for(auto cand : tau.signalChargedHadrCands() ){
       pat::PackedCandidate const* tempIsoCand = dynamic_cast<pat::PackedCandidate const*>(cand.get());
       packedCHSigTauCands.push_back(tempIsoCand);
     }
       
     for( auto cand : packedCHIsoTauCands){
       if (reco::deltaR(cand->eta(),cand->phi(),packedLeadTauCand->eta(),packedLeadTauCand->phi())<0.4){
	 dz.push_back(cand->dz()-packedLeadTauCand->dz());
	 pt.push_back(cand->pt());
	 eta.push_back(cand->eta());
	 phi.push_back(cand->phi());
	 if (cand->dtime(0)) dt.push_back(cand->dtime(0)-packedLeadTauCand->dtime(0));
	 if (!cand->dtime(0)) dt.push_back(0);
	 int where;
	 where= truth_genEle_recoTau_matched.size()-1;
	 if (truth_genEle_recoTau_matched[where]==0 && truth_genMuon_recoTau_matched[where]==0 && truth_genTau_recoTau_matched[where]==1 )
	   matched_to_tau.push_back(1);
	 if (truth_genEle_recoTau_matched[where]==1 || truth_genMuon_recoTau_matched[where]==1 || truth_genTau_recoTau_matched[where]==0 )
	   matched_to_tau.push_back(0);
	 if (truth_genEle_recoTau_matched[where]==0 && truth_genMuon_recoTau_matched[where]==0 && truth_genJet_recoTau_matched[where]==1 )
	   matched_to_jet.push_back(1);
	 if (truth_genEle_recoTau_matched[where]==1 || truth_genMuon_recoTau_matched[where]==1 || truth_genJet_recoTau_matched[where]==0 )
	   matched_to_jet.push_back(0);
	 identifier.push_back(counter);
	 sig_cand.push_back(0);
       }
     }
     for( auto cand :packedCHSigTauCands){
       if (reco::deltaR(cand->eta(),cand->phi(),packedLeadTauCand->eta(),packedLeadTauCand->phi())<0.4){
	 dz.push_back(cand->dz()-packedLeadTauCand->dz());
	 pt.push_back(cand->pt());
	 eta.push_back(cand->eta());
	 phi.push_back(cand->phi());
	 if (cand->dtime(0)) dt.push_back(packedLeadTauCand->dtime(0) - cand->dtime(0));
	 if (!cand->dtime(0)) dt.push_back(0);
	 
	 int where;
	 where= truth_genEle_recoTau_matched.size()-1;
	 if (truth_genEle_recoTau_matched[where]==0 && truth_genMuon_recoTau_matched[where]==0 && truth_genTau_recoTau_matched[where]==1 )
	   matched_to_tau.push_back(1);
	 if (truth_genEle_recoTau_matched[where]==1 || truth_genMuon_recoTau_matched[where]==1 || truth_genTau_recoTau_matched[where]==0 )
	   matched_to_tau.push_back(0);
	 if (truth_genEle_recoTau_matched[where]==0 && truth_genMuon_recoTau_matched[where]==0 && truth_genJet_recoTau_matched[where]==1 )
	   matched_to_jet.push_back(1);
	 if (truth_genEle_recoTau_matched[where]==1 || truth_genMuon_recoTau_matched[where]==1 || truth_genJet_recoTau_matched[where]==0 )
	   matched_to_jet.push_back(0);
	 identifier.push_back(counter);
	 sig_cand.push_back(1);
       }
     }
     
     counter=counter+1;
   }

   
   for (unsigned int iJet = 0; iJet < JetObjects->size() ; ++iJet){
     pat::Jet jetCand = JetObjects->at(iJet);
     jet_identifier.push_back(iJet);
     jet_pt.push_back(jetCand.pt());
     jet_eta.push_back(jetCand.eta());
     jet_phi.push_back(jetCand.phi());
     jet_partonFlavour.push_back(jetCand.partonFlavour());
     int multpl=0;


     const reco::Candidate* jet_taken = &JetObjects->at(iJet);
     for (int jj=0; jj<(int)jet_taken->numberOfDaughters(); ++jj) {
       pat::PackedCandidate const* packedLeadJetCand = dynamic_cast<pat::PackedCandidate const*>(jet_taken->daughter(jj));
       if (packedLeadJetCand->pt()>1.0)
	 multpl=multpl+1;
     }
     jet_multiplicity.push_back(multpl);
       
   } 
   


  
  event_number.push_back(iEvent.id().event());
  run_number.push_back(iEvent.run());

  truth_event_number.push_back(iEvent.id().event());
  truth_run_number.push_back(iEvent.run());

  
  tree->Fill();
  treemc->Fill();
 
}

bool tauAnalyzer::isNeutrino(const reco::Candidate* daughter)
{
  return (TMath::Abs(daughter->pdgId()) == 12 || TMath::Abs(daughter->pdgId()) == 14 || TMath::Abs(daughter->pdgId()) == 16 || TMath::Abs(daughter->pdgId()) == 18);
}

//Gets visible 4-momentum of a particle from list of daughters
reco::Candidate::LorentzVector tauAnalyzer::GetVisibleP4(std::vector<const reco::GenParticle*>& daughters){
  reco::Candidate::LorentzVector p4_vis(0,0,0,0);
  for(size_t i = 0; i < daughters.size(); ++i){
    if (!isNeutrino(daughters[i]) && daughters[i]->status() == 1){  //list should include intermediate daughters, so check for status = 1
      p4_vis += daughters[i]->p4();
    }
  }
  return p4_vis;
}


void tauAnalyzer::findDaughters(const reco::GenParticle* mother, std::vector<const reco::GenParticle*>& daughters)
{     
  unsigned numDaughters = mother->numberOfDaughters();
  if (numDaughters == 0) std::cout << " none ";
  for (unsigned iDaughter = 0; iDaughter < numDaughters; ++iDaughter ) {
    const reco::GenParticle* daughter = mother->daughterRef(iDaughter).get();
    if (daughter->status() == 1){  //status = 1 is a final state daughter
      daughters.push_back(daughter);
    } 
    if (daughter->status() == 2){  //status = 2 is an intermediate daughter; will decay further
      daughters.push_back(daughter); 
      findDaughters(daughter, daughters);
    }     
  }
}



//define this as a plug-in
DEFINE_FWK_MODULE(tauAnalyzer);
