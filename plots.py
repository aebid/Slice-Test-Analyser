import ROOT, os
from make_plot import plot1Dhist, plot1Dfit, plot2Dhist, plot2Ddensity

f = ROOT.TFile("GEM_test.root")

event = f.Get("SliceTestAnalysis/MuonData")

if os.path.exists("plots/") == False:
  os.mkdir("plots/")


###################################################1D HIST###################################################
#############################################################################################################
plot1Dhist("rechit_prop_dX_GE11", "Local_x_residual_dx", event, [100, -4, 4], "x(cm)", "", "", "residuals")
plot1Dhist("rechit_localx_GE11 - prop_localx_GE11", "Local_x_residual", event, [100, -4, 4], "x(cm)", "", "", "residuals")
plot1Dhist("rechit_phi_GE11 -  prop_phi_GE11", "Global_phi_residual", event, [100, -.04, .04], "phi", "", "", "residuals")
#############################################################################################################



###################################################2D HIST###################################################
#############################################################################################################
plot2Dhist("rechit_x_GE11:rechit_y_GE11", "Rec_Hits", event, [1000, -300, 300, 1000, -300, 300], "", "", "", "rec_rec_global_desnity")
plot2Dhist("prop_x_GE11:prop_y_GE11", "Prop_Hits", event, [1000, -300, 300, 1000, -300, 300], "", "", "", "prop_prop_global_density")
plot2Dhist("prop_x_GE11:rechit_x_GE11", "prop_rec_global", event, [100, -30, 30, 100, -30, 30], "", "", "", "prop_rec_global_density")
plot2Dhist("prop_phi_GE11:rechit_phi_GE11", "prop_rec_phi_global", event, [100, -4, 4, 100, -4, 4], "", "", "", "prop_rec_global_density")
plot2Dhist("prop_localx_GE11:rechit_localx_GE11", "prop_rec_local", event, [100, -30, 30, 100, -30, 30], "", "", "", "prop_rec_local_density")
#############################################################################################################



###################################################DENSITY###################################################
#############################################################################################################
plot2Ddensity("rechit_prop_dX_GE11:prop_localy_GE11:prop_localx_GE11", "prop_prop_res", event, [50, -30, 30, 50, -15, 15], "", "", "abs(rechit_prop_dX_GE11) < 10", "res_density")
for i in range(2):
  for j in range(1,37):
    plot2Ddensity("rechit_prop_dX_GE11[{}]:prop_localy_GE11[{}]:prop_localx_GE11[{}]".format(i,i,i), "prop_prop_res_layer{}_chamber{}".format(i,j), event, [50, -30, 30, 50, -15, 15], "local x(cm)", "local y(cm)", "abs(rechit_prop_dX_GE11) < 10 && chamber_GE11[{}] == {}".format(i, j), "res_density_LC")
############################################################################################################



############################################LAYER, CHAMBER, ROLL############################################
#############################################################################################################
for i in range(2):
  for j in range(1,37):
    for k in range(1,9):
      plot1Dhist("rechit_prop_dX_GE11[{}]".format(i), "dx_layer{}_chamber{}_roll{}".format(i,j,k), event, [100, -40, 40], "x(cm)", "", "chamber_GE11[{}] == {} && roll_GE11[{}] == {}".format(i,j,i,k), "dx_localx_LCR")
#############################################################################################################



###############################################LAYER, CHAMBER###############################################
#############################################################################################################
for i in range(2):
  for j in range(1,37):
    plot1Dhist("rechit_localx_GE11[{}]".format(i), "Rec_localx_layer{}_chamber{}".format(i,j), event, [100, -30, 30], "x(cm)", "", "chamber_GE11[{}] == {}".format(i, j), "rec_localx_LC")
    plot1Dhist("rechit_prop_dX_GE11[{}]".format(i), "Local_residual_layer{}_chamber{}".format(i, j), event, [100, -40, 40], "x(cm)", "", "chamber_GE11[{}] == {}".format(i, j), "dx_localx_LC")
    plot2Dhist("rechit_x_GE11:rechit_y_GE11", "Rec_xy_layer{}_chamber{}".format(i,j), event, [100, -300, 300, 100, -300, 300], "", "", "chamber_GE11[{}] == {}".format(i, j), "rec_density_LC")
    plot2Dhist("prop_x_GE11:prop_y_GE11", "Prop_xy_layer{}_chamber{}".format(i,j), event, [100, -300, 300, 100, -300, 300], "", "", "chamber_GE11[{}] == {}".format(i, j), "prop_density_LC")
#############################################################################################################



#################################################LAYER, ROLL#################################################
#############################################################################################################
for i in range(2);
  for j in range(1,9):
    plot1Dhist("rechit_prop_dX_GE11[{}]".format(i), "Local_res_layer{}_roll{}".format(i,k), event, [100, -4, 4], "x(cm)", "", "roll_GE11[{}] == {}".format(i,k), "dx_localx_LR")
    plot1Dhist("rechit_localx_GE11[{}] - prop_localx_center_GE11[{}]".format(i,i), "Local_res_center_layer{}_roll{}".format(i,k), event, [100, -4, 4], "x(cm)", "", "roll_GE11[{}] == {}".format(i,k), "dx_localx_LR_center")
#############################################################################################################



####################################################LAYER####################################################
#############################################################################################################
for i in range(2):
  plot1Dhist("rechit_localx_GE11[{}]".format(i), "Rec_localx_L{}_even".format(i), event, [100, -30, 30], "x(cm)", "", "chamber_GE11[{}]%2 == 0".format(i), "localx_even_odd")
  plot1Dhist("rechit_localx_GE11[{}]".format(i), "Rec_localx_L{}_odd".format(i), event, [100, -30, 30], "x(cm)", "", "chamber_GE11[{}]%2 == 1".format(i), "localx_even_odd")
  plot1Dhist("prop_localx_GE11[{}]".format(i), "Prop_localx_L{}_even".format(i), event, [100, -30, 30], "x(cm)", "", "chamber_GE11[{}]%2 == 0".format(i), "localx_even_odd")
  plot1Dhist("prop_localx_GE11[{}]".format(i), "Prop_localx_L{}_odd".format(i), event, [100, -30, 30], "x(cm)", "", "chamber_GE11[{}]%2 == 1".format(i), "localx_even_odd")
#############################################################################################################
