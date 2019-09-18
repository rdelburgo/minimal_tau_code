import numpy as np

def firework(h,i):
    h.SetDirectory(0)
    h.SetLineWidth(2)
    h.SetLineColor(i)
    h.SetMinimum(0.)
    h.SetMaximum(1.0)
if_name=sys.argv[1:]


'''                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
hh00 = TH1F('hh00', 'gen tau vs pt',len(pt_bin_size)-1,array('d',pt_bin_size))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
hh01 = TH1F('hh01', 'gen tau vs eta',40,-5,5)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
hh02 = TH1F('hh02', 'gen jet vs pt',len(pt_bin_size)-1,array('d',pt_bin_size))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
hh03 = TH1F('hh03', 'gen jet vs eta',40,-5,5)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
h01 = TH1F('h01', 'Iso eff vs pt  no Iso cut',len(pt_bin_size)-1,array('d',pt_bin_size))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
h02 = TH1F('h02', 'Iso eff vs eta no Iso cut',40,-5,5)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
h03 = TH1F('h03', 'Iso eff vs pt  Iso cut: < 0.5',len(pt_bin_size)-1,array('d',pt_bin_size))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
h04 = TH1F('h04', 'Iso eff vs eta Iso cut: < 0.5',40,-5,5)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
h05 = TH1F('h05', 'Iso eff vs pt  Iso cut: < 1.0',len(pt_bin_size)-1,array('d',pt_bin_size))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
h06 = TH1F('h06', 'Iso eff vs eta Iso cut: < 1.0',40,-5,5)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
h07 = TH1F('h07', 'Iso eff vs pt  Iso cut: < 1.5',len(pt_bin_size)-1,array('d',pt_bin_size))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
h08 = TH1F('h08', 'Iso eff vs eta Iso cut: < 1.5',40,-5,5)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
h09 = TH1F('h09', 'Iso eff vs pt  Iso cut: < 2.0',len(pt_bin_size)-1,array('d',pt_bin_size))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
h10 = TH1F('h10', 'Iso eff vs eta Iso cut: < 2.0',40,-5,5)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
h11 = TH1F('h11', 'Iso fkr vs pt  no Iso cut',len(pt_bin_size)-1,array('d',pt_bin_size))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
h12 = TH1F('h12', 'Iso fkr vs eta no Iso cut',40,-5,5)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
h13 = TH1F('h13', 'Iso fkr vs pt  Iso cut: < 0.5',len(pt_bin_size)-1,array('d',pt_bin_size))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
h14 = TH1F('h14', 'Iso fkr vs eta Iso cut: < 0.5',40,-5,5)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
h15 = TH1F('h15', 'Iso fkr vs pt  Iso cut: < 1.0',len(pt_bin_size)-1,array('d',pt_bin_size))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
h16 = TH1F('h16', 'Iso fkr vs eta Iso cut: < 1.0',40,-5,5)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
h17 = TH1F('h17', 'Iso fkr vs pt  Iso cut: < 1.5',len(pt_bin_size)-1,array('d',pt_bin_size))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
h18 = TH1F('h18', 'Iso fkr vs eta Iso cut: < 1.5',40,-5,5)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
h19 = TH1F('h19', 'Iso fkr vs pt  Iso cut: < 2.0',len(pt_bin_size)-1,array('d',pt_bin_size))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
h20 = TH1F('h20', 'Iso fkr vs eta Iso cut: < 2.0',40,-5,5)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
list_of_histo=output_file.GetListOfKeys()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
'''
eff_vs_pt_iso_cut_05 = []
fkr_vs_pt_iso_cut_05 = []
eff_vs_pt_iso_cut_10 = []
fkr_vs_pt_iso_cut_10 = []
eff_vs_pt_iso_cut_15 = []
fkr_vs_pt_iso_cut_15 = []

eff_vs_eta_iso_cut_05 = []
fkr_vs_eta_iso_cut_05 = []
eff_vs_eta_iso_cut_10 = []
fkr_vs_eta_iso_cut_10 = []
eff_vs_eta_iso_cut_15 = []
fkr_vs_eta_iso_cut_15 = []


eff_vs_pt_iso_cut_05_ths = THStack()
fkr_vs_pt_iso_cut_05_ths = THStack()
eff_vs_pt_iso_cut_10_ths = THStack()
fkr_vs_pt_iso_cut_10_ths = THStack()
eff_vs_pt_iso_cut_15_ths = THStack()
fkr_vs_pt_iso_cut_15_ths = THStack()

eff_vs_eta_iso_cut_05_ths = THStack()
fkr_vs_eta_iso_cut_05_ths = THStack()
eff_vs_eta_iso_cut_10_ths = THStack()
fkr_vs_eta_iso_cut_10_ths = THStack()
eff_vs_eta_iso_cut_15_ths = THStack()
fkr_vs_eta_iso_cut_15_ths = THStack()

iso_plot = TGraph()
for i,item in enumerate(if_name):


    input_file = ROOT.TFile.Open(item)
    eff_vs_pt_iso_cut_05.append(input_file.Get('h03').Clone())
    fkr_vs_pt_iso_cut_05.append(input_file.Get('h13').Clone())
    eff_vs_pt_iso_cut_10.append(input_file.Get('h05').Clone())
    fkr_vs_pt_iso_cut_10.append(input_file.Get('h15').Clone())
    eff_vs_pt_iso_cut_15.append(input_file.Get('h07').Clone())
    fkr_vs_pt_iso_cut_15.append(input_file.Get('h17').Clone())

    eff_vs_eta_iso_cut_05.append(input_file.Get('h04').Clone())
    fkr_vs_eta_iso_cut_05.append(input_file.Get('h14').Clone())
    eff_vs_eta_iso_cut_10.append(input_file.Get('h06').Clone())
    fkr_vs_eta_iso_cut_10.append(input_file.Get('h16').Clone())
    eff_vs_eta_iso_cut_15.append(input_file.Get('h08').Clone())
    fkr_vs_eta_iso_cut_15.append(input_file.Get('h18').Clone())


    firework(eff_vs_pt_iso_cut_05[-1] ,i+1)
    firework(fkr_vs_pt_iso_cut_05[-1] ,i+1)
    firework(eff_vs_pt_iso_cut_10[-1] ,i+1)
    firework(fkr_vs_pt_iso_cut_10[-1] ,i+1)
    firework(eff_vs_pt_iso_cut_15[-1] ,i+1)
    firework(fkr_vs_pt_iso_cut_15[-1] ,i+1)

    firework(eff_vs_eta_iso_cut_05[-1] ,i+1)
    firework(fkr_vs_eta_iso_cut_05[-1] ,i+1)
    firework(eff_vs_eta_iso_cut_10[-1] ,i+1)
    firework(fkr_vs_eta_iso_cut_10[-1] ,i+1)
    firework(eff_vs_eta_iso_cut_15[-1] ,i+1)
    firework(fkr_vs_eta_iso_cut_15[-1] ,i+1)

    eff_vs_pt_iso_cut_05_ths.Add(eff_vs_pt_iso_cut_05[-1],'E1')
    fkr_vs_pt_iso_cut_05_ths.Add(fkr_vs_pt_iso_cut_05[-1],'E1')
    eff_vs_pt_iso_cut_10_ths.Add(eff_vs_pt_iso_cut_10[-1],'E1')
    fkr_vs_pt_iso_cut_10_ths.Add(fkr_vs_pt_iso_cut_10[-1],'E1')
    eff_vs_pt_iso_cut_15_ths.Add(eff_vs_pt_iso_cut_15[-1],'E1')
    fkr_vs_pt_iso_cut_15_ths.Add(fkr_vs_pt_iso_cut_15[-1],'E1')

    eff_vs_eta_iso_cut_05_ths.Add(eff_vs_eta_iso_cut_05[-1],'E1')
    fkr_vs_eta_iso_cut_05_ths.Add(fkr_vs_eta_iso_cut_05[-1],'E1')
    eff_vs_eta_iso_cut_10_ths.Add(eff_vs_eta_iso_cut_10[-1],'E1')
    fkr_vs_eta_iso_cut_10_ths.Add(fkr_vs_eta_iso_cut_10[-1],'E1')
    eff_vs_eta_iso_cut_15_ths.Add(eff_vs_eta_iso_cut_15[-1],'E1')
    fkr_vs_eta_iso_cut_15_ths.Add(fkr_vs_eta_iso_cut_15[-1],'E1')



c1= TCanvas()
c1.cd()
eff_vs_pt_iso_cut_05_ths.Draw('nostack')
c1.SetTitle('efficiency vs pt, iso cut < 0.5')
c2= TCanvas()
c2.cd()
eff_vs_pt_iso_cut_10_ths.Draw('nostack')
c2.SetTitle('efficiency vs pt, iso cut < 1.0')
c3= TCanvas()
c3.cd()
eff_vs_pt_iso_cut_15_ths.Draw('nostack')
c3.SetTitle('efficiency vs pt, iso cut < 1.5')
c4= TCanvas()
c4.cd()
fkr_vs_pt_iso_cut_05_ths.Draw('nostack')
c4.SetTitle('fake rate vs pt, iso cut < 0.5')
c5= TCanvas()
c5.cd()
fkr_vs_pt_iso_cut_10_ths.Draw('nostack')
c5.SetTitle('fake rate vs pt, iso cut < 1.0')
c6= TCanvas()
c6.cd()
fkr_vs_pt_iso_cut_15_ths.Draw('nostack')
c6.SetTitle('fake rate vs pt, iso cut < 1.5')
c7= TCanvas()
c7.cd()
eff_vs_eta_iso_cut_05_ths.Draw('nostack')
c7.SetTitle('efficiency vs eta, iso cut < 0.5')
c8= TCanvas()
c8.cd()
eff_vs_eta_iso_cut_10_ths.Draw('nostack')
c8.SetTitle('efficiency vs eta, iso cut < 1.0')
c9= TCanvas()
c9.cd()
eff_vs_eta_iso_cut_15_ths.Draw('nostack')
c9.SetTitle('efficiency vs eta, iso cut < 1.5')
c10= TCanvas()
c10.cd()
fkr_vs_eta_iso_cut_05_ths.Draw('nostack')
c10.SetTitle('fake rate vs eta, iso cut < 0.5')
c11= TCanvas()
c11.cd()
fkr_vs_eta_iso_cut_10_ths.Draw('nostack')
c11.SetTitle('fake rate vs eta, iso cut < 1.0')
c12= TCanvas()
c12.cd()
fkr_vs_eta_iso_cut_15_ths.Draw('nostack')
c12.SetTitle('fake rate vs eta, iso cut < 1.5')

raw_input('....')


