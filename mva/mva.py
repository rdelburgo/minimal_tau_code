import ROOT
from ROOT import *
from array import array
import sys
import numpy as np
from parameter import variable_list,variable_type, cut_sig,cut_bkg

sigFile = TFile(sys.argv[1],'r')
bkgFile = TFile(sys.argv[2],'r')
sigTree  = sigFile.Get( "sig_tree")
bkgTree  = bkgFile.Get( "bkg_tree")
outputFile= TFile("out_"+sys.argv[3]+"_"+sys.argv[-1]+".root",'recreate')

factory = ROOT.TMVA.Factory( "first mva", outputFile, "Color:DrawProgressBar" )
dataloader = TMVA.DataLoader("dataset")
(TMVA.gConfig().GetVariablePlotting()).fNbinsXOfROCCurve = 1000

for i in range(0, len(variable_list)):
    dataloader.AddVariable( variable_list[i], variable_list[i], variable_type[i] )

dataloader.AddSignalTree(sigTree, 1.0 )
dataloader.AddBackgroundTree(bkgTree, 1.0 )

dataloader.PrepareTrainingAndTestTree( cut_sig,cut_bkg,  "nTrain_Signal=0:nTrain_Background=0:SplitMode=Random:NormMode=NumEvents:!V" )
#preselectionCut = TCut("<YourSelectionString>")
#factory.PrepareTrainingAndTestTree( preselectionCut, "<options>" )

factory.BookMethod( dataloader,TMVA.Types.kLikelihood, "LikelihoodD",
                        "!H:!V:!TransformOutput:PDFInterpol=Spline2:NSmoothSig[0]=20:NSmoothBkg[0]=20:NSmooth=5:NAvEvtPerBin=50:VarTransform=Decorrelate" )

factory.BookMethod(dataloader, TMVA.Types.kBDT, "BDT", "!H:!V:NTrees=800:MinNodeSize=0.05:BoostType=AdaBoost:SeparationType=GiniIndex:PruneMethod=CostComplexity:MaxDepth=3:PruningValFraction=0.5:PruneStrength=-1")

#factory.PrintHelpMessage("LikelihoodD")

factory.TrainAllMethods()
factory.TestAllMethods()
factory.EvaluateAllMethods()
