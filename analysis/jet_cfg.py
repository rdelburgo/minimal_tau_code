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
#6E074772-6DBB-E711-A572-0242AC1C0501.root  FE7D7847-96C6-E711-9993-549F3525B220.root                                                                                                                               
process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
                                #        "file:/afs/cern.ch/work/r/rdelburg/QCD_Flat_Pt-15to7000_TuneCUETP8M1_14TeV_pythia8_PhaseIITDRFall17MiniAOD-PU200_93X_upgrade2023_realistic_v2-v2/6E074772-6DBB-E711-A572-0\
242AC1C0501.root",                                                                                                                                                                                                  
                                #        "file:/afs/cern.ch/work/r/rdelburg/QCD_Flat_Pt-15to7000_TuneCUETP8M1_14TeV_pythia8_PhaseIITDRFall17MiniAOD-PU200_93X_upgrade2023_realistic_v2-v2/FE7D7847-96C6-E711-9993-5\
49F3525B220.root",                                                                                                                                                                                                  
                                "file:/afs/cern.ch/work/r/rdelburg/noPu_93x/06A2FA64-BD56-E711-9BEC-D4AE52E90A48.root",

        )
                            )

process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string("/afs/cern.ch/work/r/rdelburg/ntuples/data/qcd_out_nopu.root")

)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(30000)
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

