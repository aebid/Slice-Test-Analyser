import ROOT, os
from make_plot import plot1Dhist, plot1Dfit, plot2Dhist, plot2Ddensity

f = ROOT.TFile("GEM_100pt.root")

event = f.Get("SliceTestAnalysis/MuonData")

if os.path.exists("plots/") == False:
  os.mkdir("plots/")


###################################################1D HIST###################################################
#############################################################################################################

plot1Dhist("rechit_prop_dX_GE11", "local_x_dx", event, [100, -4, 4], "x(cm)", "", "", "residuals")
plot1Dhist("rechit_localx_GE11 - prop_localx_GE11", "local_x_sub", event, [100, -4, 4], "x(cm)", "", \
           "", "residuals")
plot1Dhist("rechit_phi_GE11 -  prop_phi_GE11", "global_phi", event, [100, -.04, .04], "phi", "", \
           "", "residuals")
plot1Dhist("rechit_localx_GE11 - prop_localx_center_GE11", "local_x_centered", event, [100, -2, 2], "", \
           "", "", "residuals")


plot1Dhist("rechit_prop_dX_GE11_foralignment", "standalone_prop_res", event, [100, -4, 4], "x(cm)", "hits", \
           "", "residuals")
plot1Dhist("rechit_propgt_dX_GE11_foralignment", "gt_prop_res", event, [100, -4, 4], "x(cm)", "hits", \
           "", "residuals")
plot1Dhist("rechit_propinner_dX_GE11_foralignment", "inner_prop_res", event, [100, -4, 4], "x(cm)", "hits", \
           "", "residuals")
#############################################################################################################



###################################################2D HIST###################################################
#############################################################################################################

plot2Dhist("rechit_x_GE11:rechit_y_GE11", "rec_rec", event, [1000, -300, 300, 1000, -300, 300], "", "", \
           "", "global_desnity")
plot2Dhist("prop_x_GE11:prop_y_GE11", "prop_prop", event, [1000, -300, 300, 1000, -300, 300], "", "", \
           "", "global_density")
plot2Dhist("prop_x_GE11:rechit_x_GE11", "prop_rec", event, [100, -30, 30, 100, -30, 30], "", "", \
           "", "global_density")
plot2Dhist("prop_phi_GE11:rechit_phi_GE11", "prop_rec_phi", event, [100, -4, 4, 100, -4, 4], "", \
           "", "", "global_density")
plot2Dhist("prop_localx_GE11:rechit_localx_GE11", "prop_rec", event, [100, -30, 30, 100, -30, 30], \
           "", "", "", "local_density")

#############################################################################################################



###################################################DENSITY###################################################
#############################################################################################################

plot2Ddensity("rechit_prop_dX_GE11_foralignment:prop_localy_GE11:prop_localx_GE11", "standalone_prop_residual", \
              event, [50, -30, 30, 50, -15, 15], "", "", "abs(rechit_prop_dX_GE11_foralignment) < 10", \
              "res_density")
plot2Ddensity("rechit_propgt_dX_GE11_foralignment:prop_localy_GE11:prop_localx_GE11", "gt_prop_residual", \
              event, [50, -30, 30, 50, -15, 15], "", "", "abs(rechit_propgt_dX_GE11_foralignment) < 10", \
              "res_density")
plot2Ddensity("rechit_propinner_dX_GE11_foralignment:prop_localy_GE11:prop_localx_GE11", \
              "inner_prop_residual", event, [50, -30, 30, 50, -15, 15], "", "", \
              "abs(rechit_propinner_dX_GE11_foralignment) < 10", "res_density")

############################################################################################################



############################################LAYER, CHAMBER, ROLL############################################
#############################################################################################################
for i in range(2):
  for j in range(1,37):
    for k in range(1,9):
      cut = "chamber_GE11[{}] == {} && roll_GE11[{}] == {}".format(i,j,i,k)
      plot1Dhist("rechit_prop_dX_GE11[{}]".format(i), "dx_layer{}_chamber{}_roll{}".format(i,j,k), event, \
                 [100, -40, 40], "x(cm)", "", cut, "dx_localx_LCR")
#############################################################################################################



###############################################LAYER, CHAMBER###############################################
#############################################################################################################
for i in range(2):
  for j in range(1,37):
    cut = "chamber_GE11[{}] == {}".format(i,j)
    plot1Dhist("rechit_localx_GE11[{}]".format(i), "Rec_localx_layer{}_chamber{}".format(i,j), event, \
               [100, -30, 30], "x(cm)", "", cut, "rec_localx_LC")
    plot1Dhist("rechit_prop_dX_GE11[{}]".format(i), "Local_residual_layer{}_chamber{}".format(i, j), \
               event, [100, -40, 40], "x(cm)", "", cut, "dx_localx_LC")
    plot2Dhist("rechit_x_GE11:rechit_y_GE11", "Rec_xy_layer{}_chamber{}".format(i,j), event, \
               [100, -300, 300, 100, -300, 300], "", "", cut, "rec_density_LC")
    plot2Dhist("prop_x_GE11:prop_y_GE11", "Prop_xy_layer{}_chamber{}".format(i,j), event, \
               [100, -300, 300, 100, -300, 300], "", "", cut, "prop_density_LC")
#############################################################################################################



#################################################LAYER, ROLL#################################################
#############################################################################################################
for i in range(2):
  for j in range(1,9):
    cut = "roll_GE11[{}] == {}".format(i,k)
    plot1Dhist("rechit_prop_dX_GE11[{}]".format(i), "Local_res_layer{}_roll{}".format(i,k), event, \
               [100, -4, 4], "x(cm)", "", cut, "dx_localx_LR")
    plot1Dhist("rechit_localx_GE11[{}] - prop_localx_center_GE11[{}]".format(i,i), \
               "Local_res_center_layer{}_roll{}".format(i,j), event, [100, -4, 4], "x(cm)", "", \
               cut, "dx_localx_LR_center")
#############################################################################################################



####################################################LAYER####################################################
#############################################################################################################
for i in range(2):
  plot1Dhist("rechit_localx_GE11[{}]".format(i), "Rec_localx_L{}_even".format(i), event, [100, -30, 30], \
             "x(cm)", "", "chamber_GE11[{}]%2 == 0".format(i), "localx_even_odd")
  plot1Dhist("rechit_localx_GE11[{}]".format(i), "Rec_localx_L{}_odd".format(i), event, [100, -30, 30], \
             "x(cm)", "", "chamber_GE11[{}]%2 == 1".format(i), "localx_even_odd")
  plot1Dhist("prop_localx_GE11[{}]".format(i), "Prop_localx_L{}_even".format(i), event, [100, -30, 30], \
             "x(cm)", "", "chamber_GE11[{}]%2 == 0".format(i), "localx_even_odd")
  plot1Dhist("prop_localx_GE11[{}]".format(i), "Prop_localx_L{}_odd".format(i), event, [100, -30, 30], \
             "x(cm)", "", "chamber_GE11[{}]%2 == 1".format(i), "localx_even_odd")
#############################################################################################################
"""
