mport FWCore.ParameterSet.Config as cmsjet
process = cms.Process("analysis")
process.tauAnalyzer  = cms.EDAnalyzer("MinimaltauAnalyzer",
#   bits               = cms.InputTag("TriggerResults","", "HLT"),
#   objects            = cms.InputTag("selectedPatTrigger"),
#   genParticles       = cms.InputTag("prunedGenParticles"),
   vertexCollection   = cms.InputTag("offlineSlimmedPrimaryVertices"),
   pfCands            = cms.InputTag("packedPFCandidates"),
   taus               = cms.InputTag("slimmedTaus"),
#   jets               = cms.InputTag("slimmedJets"), #all pf jet candidates
#   pruned             = cms.InputTag("prunedGenParticles"),
#   genJets            = cms.InputTag("slimmedGenJets")
)

process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
        "file:/afs/cern.ch/work/r/rdelburg/noPu_93x/EEF7264F-CF44-E811-BE0A-002590E7E02E.root",
)
)
'''
process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string("/afs/cern.ch/work/r/rdelburg/ntuples/data/tau_out_nopu.root")

)
'''
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
