import os
import ROOT
import array
ROOT.gROOT.SetBatch(1)
ROOT.gStyle.SetOptFit(1011)


def plot1Dhist(name, title, event, size, xlabel, ylabel, cut, plotdir):
	if os.path.exists("plots/"+plotdir) == False:
		os.mkdir("plots/"+plotdir)
	c1 = ROOT.TCanvas("", "", 800, 600)
	hist = ROOT.TH1D(name, title, size[0], size[1], size[2])
	hist.GetXaxis().SetTitle(xlabel)
	hist.GetYaxis().SetTitle(ylabel)
	hist.Sumw2()
	event.Project(name, name, cut)
	hist.Draw("Hist")
	c1.SaveAs("plots/"+plotdir+"/"+title+".png")
	return hist


def plot1Dfit(name, title, event, size, xlabel, ylabel, cut, plotdir):
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
	c1.SaveAs("plots/"+plotdir+"/"+title+".png")
	return hist


def plot1Dprof(name, title, event, size, xlabel, ylabel, cut, plotdir):
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
        c1.SaveAs("plots/"+plotdir+"/"+title+".png")
        return hist


def plot2Dhist(name, title, event, size, xlabel, ylabel, cut, plotdir):
	if os.path.exists("plots/"+plotdir) == False:
                os.mkdir("plots/"+plotdir)
	c1 = ROOT.TCanvas("", "", 800, 800)
	hist = ROOT.TH2D(name, title, size[0], size[1], size[2], size[3], size[4], size[5])
	hist.GetXaxis().SetTitle(xlabel)
	hist.GetYaxis().SetTitle(ylabel)
	hist.Sumw2()
	event.Project(name, name, cut)
	hist.Draw("colz")
	c1.SaveAs("plots/"+plotdir+"/"+title+".png")
	return hist

def plot2Ddensity(name, title, event, size, xlabel, ylabel, cut, plotdir):
	if os.path.exists("plots/"+plotdir) == False:
		os.mkdir("plots/"+plotdir)
	c1 = ROOT.TCanvas("", "", 800, 800)
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
	c1.SaveAs("plots/"+plotdir+"/"+title+".png")
	return prof
