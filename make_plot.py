import os
import ROOT
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
	prof.Draw("colz")
	c1.SaveAs("plots/"+plotdir+"/"+title+".png")
	return prof
