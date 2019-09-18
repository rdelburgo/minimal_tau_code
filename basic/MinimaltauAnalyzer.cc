#include <memory>
#include "DataFormats/Candidate/interface/Candidate.h"
#include "DataFormats/Common/interface/Handle.h" 
#include "DataFormats/PatCandidates/interface/PackedCandidate.h"
#include "DataFormats/PatCandidates/interface/PackedGenParticle.h"
#include "DataFormats/PatCandidates/interface/Tau.h"                         
#include "DataFormats/VertexReco/interface/Vertex.h"                         
#include "DataFormats/VertexReco/interface/VertexFwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"                           
#include "FWCore/Framework/interface/ESHandle.h"                             
#include "FWCore/Framework/interface/Event.h"                                
#include "FWCore/Framework/interface/MakerMacros.h"                          
#include "FWCore/Framework/interface/one/EDAnalyzer.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ServiceRegistry/interface/Service.h"                        
#include "RecoTauTag/RecoTau/interface/TauDiscriminationProducerBase.h"
#include "TrackingTools/Records/interface/TransientTrackRecord.h"
#include "TrackingTools/TransientTrack/interface/TransientTrack.h"           
#include "TrackingTools/TransientTrack/interface/TransientTrackBuilder.h"

#include <TLorentzVector.h>
#include <algorithm>  // std::sort, std::swap
#include <iostream>  // std::cout, std::endl
#include <string>

class MinimaltauAnalyzer : public edm::EDAnalyzer 
{
public:
  explicit MinimaltauAnalyzer(const edm::ParameterSet&);
private:
  virtual void analyze(const edm::Event&, const edm::EventSetup&);
  edm::EDGetTokenT<std::vector<reco::Vertex>> token_vertices;
  edm::EDGetTokenT<pat::PackedCandidateCollection> pfToken_;
  edm::EDGetTokenT<pat::TauCollection> tauToken_;
};


MinimaltauAnalyzer::MinimaltauAnalyzer(const edm::ParameterSet& iConfig)
{
   token_vertices     = consumes<std::vector<reco::Vertex>>(iConfig.getParameter<edm::InputTag>("vertexCollection"));
   pfToken_           = consumes<pat::PackedCandidateCollection>(iConfig.getParameter<edm::InputTag>("pfCands"));
   tauToken_          = consumes<pat::TauCollection>(iConfig.getParameter<edm::InputTag>("taus"));

   //   edm::Service<TFileService> fs;
}

void MinimaltauAnalyzer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{

   edm::ESHandle<TransientTrackBuilder> builder;
   iSetup.get<TransientTrackRecord>().get("TransientTrackBuilder", builder);

   edm::Handle<pat::PackedCandidateCollection> pfs;
   iEvent.getByToken(pfToken_, pfs);

   edm::Handle<pat::TauCollection> taus;
   iEvent.getByToken(tauToken_, taus);

   // vertex
   edm::Handle<std::vector<reco::Vertex>> reco_vertices;
   iEvent.getByToken(token_vertices, reco_vertices);
   bool first_vertex = true;
   reco::Vertex primary_vertex;
   for (unsigned int vertex=0; vertex < reco_vertices->size(); ++vertex) {
     if (    
         !((*reco_vertices)[vertex].isFake())
         && ((*reco_vertices)[vertex].ndof() > 4)
         && (fabs((*reco_vertices)[vertex].z()) <= 24.0)
         && ((*reco_vertices)[vertex].position().Rho() <= 2.0)
        ) {
         if (first_vertex) {
           first_vertex = false;
           primary_vertex=(*reco_vertices)[vertex];
         }
     }
   }

   int counter;
   counter=0;
   for (unsigned int iTau=0;iTau!=taus->size();++iTau) {
     pat::Tau tau = taus->at(iTau);
     std::cout << "Tau number: " << counter << std::endl;
     counter= counter + 1;
     pat::PackedCandidate const* packedLeadTauCand = dynamic_cast<pat::PackedCandidate const*>(tau.leadChargedHadrCand().get());
     std::cout << "Leading Hadron pt, eta, phi, time:  " << packedLeadTauCand->pt() << " " << packedLeadTauCand->eta() << " " << packedLeadTauCand->phi() << "" << packedLeadTauCand->time() << std::endl;
     std::cout << "pt, eta, phi:  " << tau.pt() << " " << tau.eta() << " " << tau.phi() << std::endl;
     std::cout << "decay mode: " << tau.decayMode() << std::endl;
     std::cout << "starting loop in packed candidate \n" << std::endl;
     
     std::vector<pat::PackedCandidate const*> packedCHIsoTauCands;
     std::cout <<"there are " << tau.signalChargedHadrCands().size() << " signal candidates" << std::endl;

     for(auto cand : tau.signalChargedHadrCands() ){
       pat::PackedCandidate const* tempIsoCand = dynamic_cast<pat::PackedCandidate const*>(cand.get());
       std::cout << "pt, eta, phi, dz, time: " << tempIsoCand->pt() << " " << tempIsoCand->eta() << " " << tempIsoCand->phi() << " " << tempIsoCand->dz() << " " << tempIsoCand->dtime(0) << std::endl;  
     }
     std::cout <<"there are " << tau.isolationChargedHadrCands().size() << " isolation candidates" << std::endl;

     for(auto cand : tau.isolationChargedHadrCands() ){
       pat::PackedCandidate const* tempIsoCand = dynamic_cast<pat::PackedCandidate const*>(cand.get());
       std::cout << "pt, eta, phi, dz, time: " << tempIsoCand->pt() << " " << tempIsoCand->eta() << " " << tempIsoCand->phi() << " " << tempIsoCand->dz() << " " << tempIsoCand->dtime(0) << std::endl;
     }
     
   }
}
     



//define this as a plug-in
DEFINE_FWK_MODULE(MinimaltauAnalyzer);
