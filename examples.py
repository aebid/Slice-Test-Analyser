import ROOT, os
from make_plot import *

f = ROOT.TFile("out_pp_apr9_TSOS_Segment_wrongError.root")

event = f.Get("analyser/MuonData")

if os.path.exists("plots") == False:
  os.mkdir("plots/")

#Example of 1D hist#
#plot1Dhist("branch", "Title of plot", event, [xbins, xlow, xhigh], "xaxis title", "yaxis title", "cuts1 && cuts2", "subdir", Save?, Logscale Y?)#
plot1Dhist("muon_pt", "Muon pt", event, [200, 0, 200], "muon pt [GeV]", "Entries", "", "pt", True, False)

#Example of 2D hist / chamber&region#
#plot2Dhist("ybranch:xbranch", "Title of plot", event, [xbins, xlow, xhigh, ybins, ylow, yhigh], "x title", "y title", "cuts1 && cuts2", "subdir", Save?)
for region in [-1, 1]:
  for chamber in range(1, 37):
    plot2Dhist("prop_CSC_y_GE11:prop_CSC_x_GE11", "GEM Propagation MWGR5 Global region {i} chamber {j}".format(i = region, j = chamber), event, [100, -300, 300, 100, -300, 300], "prop x [cm]", "prop y [cm]", "prop_CSC_y_GE11 < 1000 && prop_CSC_x_GE11 < 1000 && prop_region_GE11 == {i} && prop_chamber_GE11 == {j}".format(i = region, j = chamber), "prop_2D", True)

#Example of 2D profile#
#plot2Dprofile("zbranch:ybranch:xbranch", "Title of plot", event, [xbins, xlow, xhigh, ybins, ylow, yhigh], "x title", "y title", "cuts1 && cuts2", "subdir", Save?)
plot2Dprofile("RdPhi_inner_GE11:prop_innerSeg_y_GE11:prop_innerSeg_x_GE11", "Profile Test", event, [300, -300, 300, 300, -300, 300, -.1, .1], "Global x", "Global y", "has_prop_inner && abs(RdPhi_inner_GE11) < 100", "example", True)
