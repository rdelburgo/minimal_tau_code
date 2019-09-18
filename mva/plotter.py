import ROOT
from ROOT import *
from array import array
import sys
sys.path.append('../')
import re
import numbers
import numpy as np
import tdrstyle
import padstyle
import ratio
#import CMS_lumi
#CMS_lumi.cmsText = "CMS"
#CMS_lumi.extraText = "Phase 2 Simulation"
#CMS_lumi.cmsTextSize = 0.65
#CMS_lumi.outOfFrame = True
c1=TCanvas("c1","c1",800,800)
c2=TCanvas("c2","c2",800,800)
roc=[]
input_file_name=sys.argv[1:]
print input_file_name
for kk,file_name in enumerate(input_file_name):
    input_file=ROOT.TFile.Open(file_name)
    input_file.cd()
    input_file.ls()
    name="dataset/Method_LikelihoodD/LikelihoodD/MVA_LikelihoodD_effBvsS"
    name="dataset/Method_BDT/BDT/MVA_BDT_effBvsS"
    roc.append(input_file.Get(name).Clone())
    roc[-1].SetDirectory(0)
    name=filter(str.isdigit, file_name)
    add=""
    linestyle=1
    if "nocut" in file_name:
        add=" nocut"
        linestyle=2
    print name
    if name== "20025":
        roc[-1].SetName("200PU 25ns"+add)
        roc[-1].SetTitle("200PU 25ns"+add)
        roc[-1].SetLineColor(2)
        roc[-1].SetLineWidth(2)
        roc[-1].SetLineStyle(linestyle)
    if name== "20030":
        roc[-1].SetName("200PU 30ps"+add)
        roc[-1].SetTitle("200PU 30ps"+add)
        roc[-1].SetLineWidth(2)
        roc[-1].SetLineStyle(linestyle)
    if name== "030":
        roc[-1].SetName("0PU 30ps"+add)
        roc[-1].SetTitle("0PU 30ps"+add)
        roc[-1].SetLineWidth(2)
        roc[-1].SetLineColor(3)
        roc[-1].SetLineStyle(linestyle)
    input_file.Close()
    
ratio0=ratio.ratio(roc[-1],roc[-1],"ratio"+roc[-1].GetName()).Clone()
ratio1=ratio.ratio(roc[0],roc[-1],"ratio"+roc[0].GetName()).Clone()
ratio2=ratio.ratio(roc[1],roc[-1],"ratio"+roc[1].GetName()).Clone()
ratio3=ratio.ratio(ratio.ratioy(roc[-1],"ratioy"+roc[-1].GetName()),ratio.ratioy(roc[-1],"ratioy"+roc[-1].GetName())).Clone()
ratio4=ratio.ratio(ratio.ratioy(roc[-1],"ratioy"+roc[-1].GetName()),ratio.ratioy(roc[0],"ratioy"+roc[0].GetName())).Clone()
ratio5=ratio.ratio(ratio.ratioy(roc[-1],"ratioy"+roc[-1].GetName()),ratio.ratioy(roc[1],"ratioy"+roc[1].GetName())).Clone()

multiratiox=THStack()
multiratiox.Add(ratio0)
multiratiox.Add(ratio1)
multiratiox.Add(ratio2)
multiratioy=THStack()
multiratioy.Add(ratio3,"hist")
multiratioy.Add(ratio4,"hist")
multiratioy.Add(ratio5,"hist")
c1.cd()
gStyle.SetOptStat(0000)
if len(roc)>0:
    roc[0].Draw()
for item in roc[1:]:
    print item
    item.Draw("same")
c1.BuildLegend()
c1.Update()

c2.cd()
gStyle.SetOptStat(0000)
c2.Divide(1,2)
c2.cd(1)
multiratiox.Draw("nostack")
c2.cd(2)
multiratioy.Draw("nostack")
c2.Update()
raw_input("lol")
