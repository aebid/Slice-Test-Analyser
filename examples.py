import ROOT, os
from make_plot import *

f = ROOT.TFile("out_run341343_rdphiFIX.root")

event = f.Get("analyser/MuonData")

if os.path.exists("plots") == False:
  os.mkdir("plots/")


######################################__Branch Legend__#############################################
#Muons:                                                                                            #
#muon_charge     muon_pt     muon_eta     muon_momentum                                            #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #  # # # #
#Propagations: (*** is either [inner, CSC, innerSeg, outerSeg])                                    #
#has_prop_***                                                        has successful *** propagation#
#prop_location[5]  prop_location[0] = region, [1] = station, [2] = chamber, [3] = layer, [4] = roll#
#prop_***_GP_GE11[3]                      Global propagation destination: [0] = x, [1] = y, [2] = z#
#prop_***_LP_GE11[3]                       Local propagation destination: [0] = x, [1] = y, [2] = z#
#prop_***_GP_startingPoint[3]                   Global starting position: [0] = x, [1] = y, [2] = z#
#prop_***_y_adjusted_GE11                                   fixed local y for full chamber plotting#
#prop_***_localphi_rad_GE11                              Propagated position's local phi in radians#
#prop_***_localphi_deg_GE11                               Propagated position's localphi in degrees#
#prop_***_chi2_GE11                                                              *** track's chi**2#
#prop_***_ndof_GE11                                                                *** track's ndof#
#has_fidcut_***_GE11          current fidcut is |phi| < 4degrees, 5cm off top and bottom of chamber#
#which_track_***_GE11                                                    1 = outgoing, 0 = incoming#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #  # # # #
#Rechit:                                                                                           #
#has_rechit_***_GE11                                                                               #
#rechit_location_***[5]         [0] = region, [1] = station, [2] = chamber, [3] = layer, [4] = roll#
#rechit_***_GP[3]                              Global position of rechit: [0] = x, [1] = y, [2] = z#
#rechit_***_LP[3]                               Local position of rechit: [0] = x, [1] = y, [2] = z#
#recHit_first_strip_***                                                   ***'s first cluster strip#
#recHit_CLS_***                                                                  ***'s cluster size#
#rechit_y_adjusted_***_GE11                                 fixed local y for full chamber plotting#
#rechit_localphi_rad_***_GE11                                Rechit position's local phi in radians#
#rechit_localphi_deg_***_GE11                                Rechit position's local phi in degrees#
#RdPhi_***_GE11                                                          ***'s best mached residual#
#RdPhi_***_Corrected                  Residuals flipped for short/long (flips R+1 odd and R-1 even)#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #  # # # #
#det_id                                   [Region*(station*100+chamber)] ex. R-1, St1, Ch28 -> -128#
#isGEMmuon                                                                        muon->isGEMMuon()#
#hasME11                                                                 Checks for an ME11 segment#
#hasME11RecHit                                                            Checks for an ME11 rechit#
#hasME11A                                                               Checks for an ME11A segment#
#hasME11ARecHit                                                          Checks for an ME11A rechit#
#evtNum                                                    Event number - mostly for event displays#
#lumiBlock                                                    Lumiblock - mostly for event displays#
#nCSCSeg                                                                     number of CSC segments#
#nDTSeg                                                                       number of DT segments#
#CSCSeg_region                                           Endcap of the CSC segment, unnecessary now#
#num_props                                Counts number of props from an event -- not a good branch#
#simDy                                 prop_global_y - sim_global_y !!!should be local, will change#
#nRecHits5                                                          Counts rechits with RdPhi < 5cm#
#nRecHits2                                                          Counts rechits with RdPhi < 2cm#
#nRecHitsTot                                         Counts rechits on same reg/sta/ch/lay/dRoll<=1#
#closest                                                                 int closest segment to GEM#
#closest_ME11                                                                         NEEDS REMOVAL#
#ME11_startingPoint                      Global position of ME11 segment: [0] = x, [1] = y, [2] = z#
#sim_GP[3]                                        Global simhit position: [0] = x, [1] = y, [2] = z#
#sim_LP[3]                                         local simhit position: [0] = x, [1] = y, [2] = z#
#sim_localy_adjusted                                        fixed local y for full chamber plotting#
#nSim                                                Counts simhits on same reg/sta/ch/lay/dRoll<=1#
####################################################################################################



#Example of 1D hist#
#plot1Dhist("branch", "Title of plot", event, [xbins, xlow, xhigh], "xaxis title", "yaxis title", "cuts1 && cuts2", "subdir", Save?, Logscale Y?)#
plot1Dhist("muon_pt", "Muon pt", event, [200, 0, 200], "muon pt [GeV]", "Entries", "", "pt", True, False)

#Example of 2D hist / chamber&region#
#plot2Dhist("ybranch:xbranch", "Title of plot", event, [xbins, xlow, xhigh, ybins, ylow, yhigh], "x title", "y title", "cuts1 && cuts2", "subdir", Save?)
for region in [-1, 1]:
  for chamber in range(1, 37):
    plot2Dhist("prop_CSC_GP_GE11[1]:prop_CSC_GP_GE11[0]", "GEM Propagation MWGR5 Global region {i} chamber {j}".format(i = region, j = chamber), event, [100, -300, 300, 100, -300, 300], "prop x [cm]", "prop y [cm]", "prop_CSC_GP_GE11[1] < 1000 && prop_CSC_GP_GE11[0] < 1000 && prop_location[0] == {i} && prop_location[2] == {j}".format(i = region, j = chamber), "prop_2D", True)

#Example of 2D profile#
#plot2Dprofile("zbranch:ybranch:xbranch", "Title of plot", event, [xbins, xlow, xhigh, ybins, ylow, yhigh], "x title", "y title", "cuts1 && cuts2", "subdir", Save?)
plot2Dprofile("RdPhi_CSC_GE11:prop_CSC_GP_GE11[1]:prop_CSC_GP_GE11[0]", "Profile Test", event, [300, -300, 300, 300, -300, 300, -4, 4], "Global x", "Global y", "has_prop_CSC && abs(RdPhi_CSC_GE11) < 100", "example", True)
