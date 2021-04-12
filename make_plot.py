import os
import ROOT
import array
ROOT.gROOT.SetBatch(1)
ROOT.gStyle.SetOptFit(1011)


def plot1Dhist(name, title, event, size, xlabel, ylabel, cut, plotdir, save, logy):
	if os.path.exists("plots/"+plotdir) == False:
		os.mkdir("plots/"+plotdir)
	c1 = ROOT.TCanvas("", "", 800, 600)
	hist = ROOT.TH1D(name, title, size[0], size[1], size[2])
	hist.GetXaxis().SetTitle(xlabel)
	hist.GetYaxis().SetTitle(ylabel)
	hist.Sumw2()
	event.Project(name, name, cut)
	hist.Draw("Hist")
        if logy:
                c1.SetLogy()
        if save:
	        c1.SaveAs("plots/"+plotdir+"/"+title+".png")
	return hist


def plot1Dfit(name, title, event, size, xlabel, ylabel, cut, plotdir, save):
	if os.path.exists("plots/"+plotdir) == False:
                os.mkdir("plots/"+plotdir)	
	c1 = ROOT.TCanvas("", "", 800, 600)
	hist = ROOT.TH1D(name, title, size[0], size[1], size[2])
	hist.GetXaxis().SetTitle(xlabel)
	hist.GetYaxis().SetTitle(ylabel)
	hist.Sumw2()
	event.Project(name, name, cut)
	hist.Draw()
	hist.Fit("gaus")
        if save:
	        c1.SaveAs("plots/"+plotdir+"/"+title+".png")
	return hist


def plot1Dprofile(name, title, event, size, xlabel, ylabel, cut, plotdir, save):
        if os.path.exists("plots/"+plotdir) == False:
                os.mkdir("plots/"+plotdir)
        c1 = ROOT.TCanvas("", "", 800, 600)
        hist = ROOT.TProfile(name, title, size[0], size[1], size[2], size[4], size[5])
        hist.GetXaxis().SetTitle(xlabel)
        hist.GetYaxis().SetTitle(ylabel)
	hist.GetYaxis().SetRangeUser(size[4], size[5])
        hist.Sumw2()
        event.Project(name, name, cut)
        hist.Draw("Hist")
        if save:
                c1.SaveAs("plots/"+plotdir+"/"+title+".png")
        return hist


def plot2Dhist(name, title, event, size, xlabel, ylabel, cut, plotdir, save):
	if os.path.exists("plots/"+plotdir) == False:
                os.mkdir("plots/"+plotdir)
	c1 = ROOT.TCanvas("", "", 800, 800)
	hist = ROOT.TH2D(name, title, size[0], size[1], size[2], size[3], size[4], size[5])
	hist.GetXaxis().SetTitle(xlabel)
	hist.GetYaxis().SetTitle(ylabel)
	hist.Sumw2()
	event.Project(name, name, cut)
	hist.Draw("colz")
        if save:
	        c1.SaveAs("plots/"+plotdir+"/"+title+".png")
	return hist

def plot2Dprofile(name, title, event, size, xlabel, ylabel, cut, plotdir, save):
	if os.path.exists("plots/"+plotdir) == False:
		os.mkdir("plots/"+plotdir)
	c1 = ROOT.TCanvas("", "", 1280, 800)
	prof = ROOT.TProfile2D(name, title, size[0], size[1], size[2], size[3], size[4], size[5])
	prof.GetXaxis().SetTitle(xlabel)
	prof.GetYaxis().SetTitle(ylabel)
	prof.Sumw2()
	event.Project(name, name, cut)
	
	ablue = array.array("d", [1,1,0])
	ared = array.array("d", [0,1,1])
	agreen = array.array("d", [0,1,0])
	astop = array.array("d", [0,.5,1])
	myPalette = []
	fi = ROOT.TColor.CreateGradientColorTable(3, astop, ared, agreen, ablue, 100)
	for x in range(100):
	  myPalette.append(fi+x)
	ROOT.gStyle.SetPalette(100, array.array("i", myPalette))
	prof.GetZaxis().SetRangeUser(size[6], size[7])
	prof.Draw("colz")
	c1.SetRightMargin(0.35)
        if save:
	        c1.SaveAs("plots/"+plotdir+"/"+title+".png")
	return prof

def plot2Dratio(name, title, event, size, xlabel, ylabel, cut, plotdir, save):
        if os.path.exists("plots/"+plotdir) == False:
                os.mkdir("plots/"+plotdir)
        hist1 = plot2Dhist(name, title[0], event, size, xlabel, ylabel, cut[0], plotdir, False)
        hist2 = plot2Dhist(name, title[1], event, size, xlabel, ylabel, cut[1], plotdir, False)
        c2 = ROOT.TCanvas("", "", 2400, 800)
        c2.Divide(3,1)
        c2.cd(1)
        hist1.Draw("colz")
        c2.cd(2)
        hist2.Draw("colz")
        c2.cd(3)
        hist3 = hist1.Clone(title[2])
        hist3.Divide(hist2)
        hist3.SetTitle(title[2])
        hist3.Draw("colz")
        ROOT.gStyle.SetStatX(0.2);                 
        if save:
                c2.SaveAs("plots/"+plotdir+"/"+title[2]+".png")
        return hist3


def plot1Defficiency(name, title, event, size, xlabel, ylabel, cut, plotdir, save):
	if os.path.exists("plots/"+plotdir) == False:
		os.mkdir("plots/"+plotdir)
	c1 = ROOT.TCanvas("", "", 1200, 800)
	hist = ROOT.TEfficiency("eff", "{title};#eta partition;#epsilon".format(title = title), size[0], size[1], size[2])
	num = 0
	den = 0
	for i in event:
		eta = i.prop_roll_GE11
		if i.has_prop_GE11 == 1 and i.prop_chamber_GE11%2 == 0 and i.prop_roll_GE11 < 10 and i.region_mismatch == 1 and i.hasME11 == 1:
			if i.has_rechit_GE11 == 1 and i.RdPhi_CSC_GE11 < 5:
				num += 1
				den += 1
				hist.Fill(True, eta)
			else:
				den += 1
				hist.Fill(False, eta)

	hist.Draw()
	legend = ROOT.TLegend()
	legend.AddEntry(hist, "{num} passed, {den} total".format(num = num, den = den))
	legend.Draw("same")
        if save:
		c1.SaveAs("plots/"+plotdir+"/"+title+".png")
	return hist

def plotratio(name, title, event, size, xlabel, ylabel, cut, plotdir, save):
        if os.path.exists("plots/"+plotdir) == False:
                os.mkdir("plots/"+plotdir)
        c1 = ROOT.TCanvas("", "", 1600, 600)
        c1.Divide(2,1)
        c1.cd(1)
        hist = ROOT.TH1D(name, title[1], size[0], size[1], size[2])
        hist.GetXaxis().SetTitle(xlabel)
        hist.GetYaxis().SetTitle(ylabel)
        hist.Sumw2()
        event.Project(name, name, cut[0])
        hist.SetLineColor(4)
        hist.Draw("Hist")
        hist.Scale(1.0/hist.Integral())
        print hist.Integral()

        hist2 = ROOT.TH1D(name, title[1], size[0], size[1], size[2])
        hist2.GetXaxis().SetTitle(xlabel)
        hist2.GetYaxis().SetTitle(ylabel)
        hist2.Sumw2()
        event.Project(name, name, cut[1])
        hist2.SetLineColor(2)
        hist2.Draw("same Hist")
        hist2.Scale(1.0/hist2.Integral())

        legend = ROOT.TLegend()
        legend.AddEntry(hist, title[0])
        legend.AddEntry(hist2, title[1])
        legend.Draw("same")

        c1.cd(2)
        hist3 = hist.Clone(title[2])
        hist3.SetTitle(title[2])
        hist3.Divide(hist2)
	hist3.GetYaxis().SetTitle("ratio")
        hist3.Draw("Hist")

        if save:
                c1.SaveAs("plots/"+plotdir+"/"+title[2]+".png")
        return hist3
