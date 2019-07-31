import ROOT, os
from make_plot import plot1Dhist, plot1Dfit, plot1Dprof, plot2Dhist, plot2Ddensity

f = ROOT.TFile("GEM_30pt.root")

event = f.Get("SliceTestAnalysis/MuonData")

if os.path.exists("plots") == False:
  os.mkdir("plots/")


###################################################1D HIST###################################################
#plot1Dhist("data", "name", event, [bins, xmin, xmax], "xlabel", "ylabel", "cut", "plotdir")
#############################################################################################################

###################################################2D HIST###################################################
#size = [xbins, xmin, xmax, ybins, ymin, ymax]
#plot2Dhist("data_y:data_x", "name", event, size, "xlabel", "ylabel", "cut", "plotdir")
#############################################################################################################

###################################################1D PROF###################################################
#size = [xbins, xmin, xmax, EMPTY, ymin, ymax] 
#plot1Dprof("data(averaged):position", "name", event, size, "xlabel", "ylabel", "cut", "plotdir")
#############################################################################################################

###################################################DENSITY###################################################
#size = [xbins, xmin, xmax, ybins, ymin, ymax, densitymin, densitymax]
#plot2Ddensity("data:position_y:position_x", "name", event, size, "xlabel", "ylabel", "cut", "plotdir")
############################################################################################################
