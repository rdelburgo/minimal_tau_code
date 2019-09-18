import FWCore.ParameterSet.Config as cmsjet
process = cms.Process("analysis")
process.tauAnalyzer  = cms.EDAnalyzer("tauAnalyzer",
   muonCollection     = cms.InputTag("slimmedMuons"),
   electronCollection = cms.InputTag("slimmedElectrons"),
   bits               = cms.InputTag("TriggerResults","", "HLT"),
   objects            = cms.InputTag("selectedPatTrigger"),
   genParticles       = cms.InputTag("prunedGenParticles"),
   vertexCollection   = cms.InputTag("offlineSlimmedPrimaryVertices"),
   pfCands            = cms.InputTag("packedPFCandidates"),
   taus               = cms.InputTag("slimmedTaus"),
   jets               = cms.InputTag("slimmedJets"), #all pf jet candidates                                                                                                                                                                                                                  
   pruned             = cms.InputTag("prunedGenParticles"),
   genJets            = cms.InputTag("slimmedGenJets")
)

process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(

#        "file:/afs/cern.ch/work/r/rdelburg/data_tau/2E76047B-A844-E811-9207-008CFAC93B74.root",                                                                                                                                                                                             
#        "file:/afs/cern.ch/work/r/rdelburg/data_tau/6EB3A85A-9344-E811-A83F-008CFAC91B48.root",                                                                                                                                                                                             
#        "file:/afs/cern.ch/work/r/rdelburg/data_tau/FCAD1769-9744-E811-8F7E-008CFAC91B78.root",                                                                                                                                                                                             
#        "file:/afs/cern.ch/work/r/rdelburg/data_tau/4AF6AE4E-C044-E811-BBAC-008CFA11121C.root",                                                                                                                                                                                             
#        "file:/afs/cern.ch/work/r/rdelburg/data_tau/C20FEC3F-B044-E811-B154-008CFAE453AC.root",                                                                                                                                                                                             
        "file:/afs/cern.ch/work/r/rdelburg/noPu_93x/EEF7264F-CF44-E811-BE0A-002590E7E02E.root",
)
)

process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string("/afs/cern.ch/work/r/rdelburg/ntuples/data/tau_out_nopu.root")

)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(20000)
)

process.options = cms.untracked.PSet(
   wantSummary = cms.untracked.bool(True),
)

process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 100

process.p = cms.Path(
   process.tauAnalyzer
)

process.load("RecoBTag.Configuration.RecoBTag_cff") # this loads all available b-taggers                                                                                                                                                                                                     
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.load("TrackingTools/TransientTrack/TransientTrackBuilder_cfi")
process.load("Configuration.Geometry.GeometryIdeal_cff")
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.GlobalTag.globaltag = '93X_upgrade2023_realistic_v2'
