import ROOT
from ROOT import *
from array import array
import sys
import re
import numbers
import numpy as np
import os
import array
import tdrstyle
path_conf = '/afs/cern.ch/user/r/rdelburg/new_dir/CMSSW_9_3_2/src/test/configuration/configurations/'
def firework(h,i):
    h.SetDirectory(0)
    h.SetLineWidth(2)

    h.SetLineColor(i)

def f_ratio(point, tg_low, tg_up, tg_ratio):
    ratio = 0
    x = point
    y1 = tg_low.Eval(x)
    y2 = tg_up.Eval(x)
    y3 = tg_ratio.Eval(x)

    if (y2-y1) != 0:
        ratio = (y3-y1)/ abs(y2-y1)
    if abs(ratio)>1.0:
        ratio = 0
    return ratio

def invert(tg_in, tg_out):
    for i in range(0, tg_in.GetN()):
       #  x = array.array( 'f', [0.])                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
       #  y = array.array( 'f', [0.])                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
        x = ROOT.Double()
        y = ROOT.Double()
        tg_in.GetPoint(i, x, y)
        tg_out.SetPoint (i, y, x )
    return tg_out
def match_name(root_file,conf_file):

    conf_n = re.findall(r'\d+',root_file)
    r_name = ''
    for item in conf_file:
        if conf_n[0] in re.findall(r'\d+', item):
            input_file_name = item
            input_file = open(path_conf + input_file_name, 'r')
            print 'opening ', path_conf + input_file_name
            r_name = input_file.readlines()[1]
    print 'r_name', r_name
    return r_name

if_name=sys.argv[1:]
print if_name


roc_tmg = TMultiGraph()
ratio_tmg = TMultiGraph()
ratio_y_tmg = TMultiGraph()
iso_plot = []
ratio_plot_x = []
ratio_plot_y = []
eff_h = []
fkr_h = []
eff=[]
fkr=[]

iso_for_tau_l = THStack()
iso_for_jet_l = THStack()

for i,item in enumerate(if_name):


    input_file = ROOT.TFile.Open(item)
#    print item                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
    if 'tau' in item:
#        print 'got eff_h'                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
        eff_h.append(input_file.Get('h21').Clone())
        firework(eff_h[-1],i+1)
        eff.append(0)
        iso_plot.append(TGraph())
        where = [f for f in os.listdir(path_conf) if f.endswith('.py')]
        iso_plot[-1].SetName(match_name(item,where))
        ratio_plot_x.append(TGraph())
        ratio_plot_y.append(TGraph())

    if 'qcd' in item:
#        print 'got fkr_h'                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
        fkr_h.append(input_file.Get('h22').Clone())
        firework(fkr_h[-1],i+1)
        fkr.append(0)

for i,item in enumerate(eff_h):
    item.SetLineColor(i+1)
    iso_for_tau_l.Add(item)
for i,item in enumerate(fkr_h):
    item.SetLineColor(i+1)
    iso_for_jet_l.Add(item)

for i in range(0, len(fkr_h)):
#    print if_name[i*2], '##############'                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
    for l in range(0, eff_h[i].GetNbinsX()):
        eff[i] = eff[i] + eff_h[i].GetBinContent(l)
        fkr[i] = fkr[i] + fkr_h[i].GetBinContent(l)
        iso_plot[i].SetPoint(l,eff[i],fkr[i])
#        print eff[i],fkr[i]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   

for i in range (1, len(iso_plot) -1):
    for l in range(0,100):
        point = 0.01 * l
        ratio = f_ratio(point, iso_plot[0], iso_plot[-1], iso_plot[i] )
        ratio_plot_x[i].SetPoint(l, point, ratio)


inverted_iso_plot = []
for item in iso_plot:
    inverted_iso_plot.append(TGraph())
    invert(item,inverted_iso_plot[-1])

for i in range (1, len(inverted_iso_plot) -1):
    for l in range(0,100):
        point = 0.01 * l
        ratio = f_ratio(point, inverted_iso_plot[0], inverted_iso_plot[-1], inverted_iso_plot[i] )
        ratio_plot_y[i].SetPoint(l, ratio, point)


for i in range(0,len(iso_plot)):

    iso_plot[i].SetLineColor(i+1)
    iso_plot[i].SetMarkerColor(i+1)
    iso_plot[i].SetMarkerStyle(8)
    iso_plot[i].SetMarkerSize(0.4)
    iso_plot[i].SetLineWidth(2)

    roc_tmg.Add(iso_plot[i], 'lp')


    ratio_plot_x[i].SetLineColor(i+1)
    ratio_plot_x[i].SetMarkerColor(i+1)
    ratio_plot_x[i].SetLineWidth(2)

    ratio_plot_y[i].SetLineColor(i+1)
    ratio_plot_y[i].SetMarkerColor(i+1)
    ratio_plot_y[i].SetLineWidth(2)

    ratio_tmg.Add(ratio_plot_x[i], 'lp')
    ratio_y_tmg.Add(ratio_plot_y[i], 'lp')

c2 = TCanvas('c2', 'c2' , 800 , 800)
c2.cd()
roc_tmg.Draw('ap')
c2.BuildLegend()


c4 = TCanvas('c4', 'c4' , 800 , 200)
c4.cd()
ratio_tmg.Draw('ap')

c5 = TCanvas('c5', 'c5' , 200 , 800)
c5.cd()
ratio_y_tmg.Draw('ap')

c4.Update()
c5.Update()
c2.Update()


c3 = TCanvas('c3', 'c3' , 800 , 800)
pad1 = TPad("pad1","pad1", 0.05,0.05,0.95,0.2)
pad2 = TPad("pad2","pad2", 0.8,0.2,0.95,0.95)
pad3 = TPad("pad3","pad3", 0.05,0.2,0.8,0.95)
c3.cd()
pad1.Draw()
pad1.cd()
ratio_tmg.Draw('ap')
c3.cd()
pad2.Draw()
pad2.cd()
ratio_y_tmg.Draw('ap')
c3.cd()
pad3.Draw()
pad3.cd()
roc_tmg.Draw('ap')


c3.Update()
raw_input('....')



