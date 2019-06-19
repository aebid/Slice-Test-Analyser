import ROOT
import os

plotdir = "GEM_residuals"
os.system("mkdir -p "+plotdir)
chain = ROOT.TChain("SliceTestAnalysis/MuonData")
chain.Add("/uscms/home/daebi/nobackup/CMSSW_10_3_0_pre4/src/GEMCSCBendingAnalyzer/MuonAnalyser/data/0000/GEM_test.root")


def plot_tree_1D(tree, branch_name, cut, xtitle, nbins, xmin, xmax, text, plotname):


    c1=ROOT.TCanvas("c1","New Graph",0,0, 800,600);
    c1.SetGridx()
    c1.SetGridy()
    #c1.SetTickx()
    #c1.SetTicky()
    #h=F.Get("SliceTestAnalysis/MuonData");
    hist = ROOT.TH1F("hist","hist_title", nbins, xmin, xmax)

    tree.Draw(branch_name + ">> hist", cut);## plot hist with cut
    hist.SetTitle( " #scale[1.4]{#font[61]{CMS}} #font[42]{Internal} "+"  "*16+"GEM MC Sim")
    hist.GetXaxis().SetTitle(xtitle)
    #hist.GetYaxis().SetTitle("Normalized to unity")
    hist.SetStats(0)
    print "todraw ", branch_name, " cut ",cut
    #hist.Scale(1.0/hist.Integral())
    hist.Draw("hist")
#    outplot = os.path.join(plotname, str(branch_name))
    txt = ROOT.TLatex(.15, .8, text)
    txt.SetNDC()
    txt.SetTextFont(42)
    txt.SetTextFont(42)
    txt.SetTextSize(.04)
    txt.Draw("same")

    #outplot = os.path.join(os.getcwd(), str(plotname))
    outplot = plotname
    c1.SaveAs(outplot + ".png")
    c1.SaveAs(outplot + ".pdf")


def plotdPhiGEMMuon(chain, cut, text, plotdir):
    todraw = "rechit_prop_dphi_GE11"
    for i in range(0, 2):#2layers for GEM
        todrawX = todraw+"[%d]"%i
	print todrawX
        thiscut = cut + "&& has_GE11[%d]>0 && abs(%s)<4"%(i, todrawX)
        plotname = os.path.join(plotdir, "2018D_Zmu_GEMCSCbending_rechit_prop_dphi_GE11_GEMlayer%d"%(i))
        plot_tree_1D(chain, todraw, thiscut, "Residual [rad]", 80, -0.020, 0.020, text,plotname)
#plotdPhiGEMMuon(chain, "has_MediumID && muonpt>20", "RecoMuon: Medium ID, p_{T}>20 GeV", plotdir)


def plot_GEM_local_x_res(chain, cut, text, plotdir):
    #todraw = "prop_localx_GE11[%d] - rechit_localx_GE11[%d]"
    for i in range(0, 2):
        #todrawX = todraw%(i,i)
	todrawX = "prop_localx_GE11[%d] - rechit_localx_GE11[%d]"%(i,i)
        print todrawX
	print i
        thiscut = cut + "&& has_GE11[%d]>0 && abs(%s)<4"%(i, todrawX)
        plotname = os.path.join(plotdir, "GEM_local_x_res_layer%d"%i)
        plot_tree_1D(chain, todrawX, thiscut, "Residual [cm]", 120, -6, 6, text, plotname)

plot_GEM_local_x_res(chain, "has_MediumID && muonpt>20", "MC 50 GeV", plotdir)
