import ROOT, os
from make_plot import plot1Dhist, plot1Dfit, plot1Dprof, plot2Dhist, plot2Ddensity

f = ROOT.TFile("GEM_30pt.root")

event = f.Get("SliceTestAnalysis/MuonData")

if os.path.exists("plots") == False:
  os.mkdir("plots/")



###################################################1D HIST###################################################
#############################################################################################################
plot1Dhist("rechit_prop_RdPhi_GE11", "standalone_prop_res", event, [100, -4, 4], \
           "Rphi (cm)", "hits", "", "residuals")
plot1Dhist("rechit_propgt_RdPhi_GE11", "gt_prop_res", event, [100, -4, 4], \
           "Rphi (cm)", "hits", "", "residuals")
plot1Dhist("rechit_propinner_RdPhi_GE11", "inner_prop_res", event, [100, -4, 4], \
           "Rphi (cm)", "hits", "", "residuals")
#############################################################################################################



###################################################2D HIST###################################################
#############################################################################################################
plot2Dhist("rechit_x_GE11:rechit_y_GE11", "rec_rec", event, [1000, -300, 300, 1000, -300, 300], \
           "", "", "", "global_density")
plot2Dhist("prop_x_GE11:prop_y_GE11", "prop_prop", event, [1000, -300, 300, 1000, -300, 300], \
           "", "", "", "global_density")
#############################################################################################################



###################################################1D PROF###################################################
#############################################################################################################
plot1Dprof("rechit_prop_RdPhi_GE11:rechit_stripangle_GE11", "residual_by_angle_odd", event, \
           [400, -.1, .1, 200, -.1, .1], "", "", "chamber_GE11%2 == 1", "stand_even_odd_res")
plot1Dprof("rechit_prop_RdPhi_GE11:prop_strip_GE11", "residual_by_number_odd", event, \
           [400, -10, 390, 200, -.1, .1], "", "", "chamber_GE11%2 == 1", "stand_even_odd_res")
plot1Dprof("rechit_prop_RdPhi_GE11:rechit_stripangle_GE11", "residual_by_angle_even", event, \
           [400, -.1, .1, 200, -.1, .1], "", "", "chamber_GE11%2 == 0", "stand_even_odd_res")
plot1Dprof("rechit_prop_RdPhi_GE11:prop_strip_GE11", "residual_by_number_even", event, \
           [400, -10, 390, 200, -.1, .1], "", "", "chamber_GE11%2 == 0", "stand_even_odd_res")

plot1Dprof("rechit_prop_RdPhi_GE11:rechit_stripangle_GE11", "residual_by_angle_odd_high", event, \
           [400, -.1, .1, 200, -15, 15], "", "", "chamber_GE11%2 == 1", "stand_even_odd_res")
plot1Dprof("rechit_prop_RdPhi_GE11:prop_strip_GE11", "residual_by_number_odd_high", event, \
           [400, -10, 390, 200, -15, 15], "", "", "chamber_GE11%2 == 1", "stand_even_odd_res")
plot1Dprof("rechit_prop_RdPhi_GE11:rechit_stripangle_GE11", "residual_by_angle_even_high", event, \
           [400, -.1, .1, 200, -15, 15], "", "", "chamber_GE11%2 == 0", "stand_even_odd_res")
plot1Dprof("rechit_prop_RdPhi_GE11:prop_strip_GE11", "residual_by_number_even_high", event, \
           [400, -10, 390, 200, -15, 15], "", "", "chamber_GE11%2 == 0", "stand_even_odd_res")

plot1Dprof("rechit_propgt_RdPhi_GE11:rechit_stripangle_GE11", "residual_by_angle_odd", event, \
           [400, -.1, .1, 200, -.1, .1], "", "", "chamber_GE11%2 == 1", "gt_even_odd_res")
plot1Dprof("rechit_propgt_RdPhi_GE11:prop_strip_GE11", "residual_by_number_odd", event, \
           [400, -10, 390, 200, -.1, .1], "", "", "chamber_GE11%2 == 1", "gt_even_odd_res")
plot1Dprof("rechit_propgt_RdPhi_GE11:rechit_stripangle_GE11", "residual_by_angle_even", event, \
           [400, -.1, .1, 200, -.1, .1], "", "", "chamber_GE11%2 == 0", "gt_even_odd_res")
plot1Dprof("rechit_propgt_RdPhi_GE11:prop_strip_GE11", "residual_by_number_even", event, \
           [400, -10, 390, 200, -.1, .1], "", "", "chamber_GE11%2 == 0", "gt_even_odd_res")

plot1Dprof("rechit_propgt_RdPhi_GE11:rechit_stripangle_GE11", "residual_by_angle_odd_high", event, \
           [400, -.1, .1, 200, -15, 15], "", "", "chamber_GE11%2 == 1", "gt_even_odd_res")
plot1Dprof("rechit_propgt_RdPhi_GE11:prop_strip_GE11", "residual_by_number_odd_high", event, \
           [400, -10, 390, 200, -15, 15], "", "", "chamber_GE11%2 == 1", "gt_even_odd_res")
plot1Dprof("rechit_propgt_RdPhi_GE11:rechit_stripangle_GE11", "residual_by_angle_even_high", event, \
           [400, -.1, .1, 200, -15, 15], "", "", "chamber_GE11%2 == 0", "gt_even_odd_res")
plot1Dprof("rechit_propgt_RdPhi_GE11:prop_strip_GE11", "residual_by_number_even_high", event, \
           [400, -10, 390, 200, -15, 15], "", "", "chamber_GE11%2 == 0", "gt_even_odd_res")

plot1Dprof("rechit_propinner_RdPhi_GE11:rechit_stripangle_GE11", "residual_by_angle_odd", event, \
           [400, -.1, .1, 200, -.1, .1], "", "", "chamber_GE11%2 == 1", "inner_even_odd_res")
plot1Dprof("rechit_propinner_RdPhi_GE11:prop_strip_GE11", "residual_by_number_odd", event, \
           [400, -10, 390, 200, -.1, .1], "", "", "chamber_GE11%2 == 1", "inner_even_odd_res")
plot1Dprof("rechit_propinner_RdPhi_GE11:rechit_stripangle_GE11", "residual_by_angle_even", event, \
           [400, -.1, .1, 200, -.1, .1], "", "", "chamber_GE11%2 == 0", "inner_even_odd_res")
plot1Dprof("rechit_propinner_RdPhi_GE11:prop_strip_GE11", "residual_by_number_even", event, \
           [400, -10, 390, 200, -.1, .1], "", "", "chamber_GE11%2 == 0", "inner_even_odd_res")

plot1Dprof("rechit_propinner_RdPhi_GE11:rechit_stripangle_GE11", "residual_by_angle_odd_high", event, \
           [400, -.1, .1, 200, -15, 15], "", "", "chamber_GE11%2 == 1", "inner_even_odd_res")
plot1Dprof("rechit_propinner_RdPhi_GE11:prop_strip_GE11", "residual_by_number_odd_high", event, \
           [400, -10, 390, 200, -15, 15], "", "", "chamber_GE11%2 == 1", "inner_even_odd_res")
plot1Dprof("rechit_propinner_RdPhi_GE11:rechit_stripangle_GE11", "residual_by_angle_even_high", event, \
           [400, -.1, .1, 200, -15, 15], "", "", "chamber_GE11%2 == 0", "inner_even_odd_res")
plot1Dprof("rechit_propinner_RdPhi_GE11:prop_strip_GE11", "residual_by_number_even_high", event, \
           [400, -10, 390, 200, -15, 15], "", "", "chamber_GE11%2 == 0", "inner_even_odd_res")
#############################################################################################################



###################################################DENSITY###################################################
#############################################################################################################
cut = "abs(middle_perp_propGE11) < 1000"
plot2Ddensity("rechit_prop_RdPhi_GE11:prop_localy_GE11+middle_perp_propGE11:prop_localx_GE11", \
              "standalone_prop_residual", event, [50, -25, 25, 100, 120, 250, -.5, .5], \
              "", "", cut+"&& abs(rechit_prop_RdPhi_GE11) < 10", "res_density_GE11")
plot2Ddensity("rechit_propgt_RdPhi_GE11:prop_localy_GE11+middle_perp_propGE11:prop_localx_GE11", \
              "gt_prop_residual", event, [50, -25, 25, 100, 120, 250, -.5, .5], \
              "", "", cut+"&& abs(rechit_propgt_RdPhi_GE11) < 10", "res_density_GE11")
plot2Ddensity("rechit_propinner_RdPhi_GE11:prop_localy_GE11+middle_perp_propGE11:prop_localx_GE11", \
              "inner_prop_residual", event, [50, -25, 25, 100, 120, 250, -.5, .5], \
              "", "", cut+"&& abs(rechit_propinner_RdPhi_GE11) < 10", "res_density_GE11")

plot2Ddensity("rechit_prop_RdPhi_ME11:prop_localy_ME11:prop_localx_ME11", \
              "standalone_prop_residual_ME11", event, [100, -40, 40, 100, -100, 100, -2, 2], \
              "", "", "abs(rechit_prop_RdPhi_ME11) < 10 && abs(prop_localy_ME11) < 70", "res_density_ME11")
plot2Ddensity("rechit_propgt_RdPhi_ME11:prop_localy_ME11:prop_localx_ME11", \
              "gt_prop_residual_ME11", event, [100, -40, 40, 100, -100, 100, -2, 2], \
              "", "", "abs(rechit_propgt_RdPhi_ME11) < 10", "res_density_ME11")
plot2Ddensity("rechit_propinner_RdPhi_ME11:prop_localy_ME11:prop_localx_ME11", \
              "inner_prop_residual_ME11", event, [100, -40, 40, 100, -100, 100, -2, 2], \
              "", "", "abs(rechit_propinner_RdPhi_ME11) < 10", "res_density_ME11")
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
    plot1Dhist("rechit_prop_RdPhi_GE11[{}]".format(i), "rdphi_layer{}_roll{}".format(i,k), event, \
               [100, -3, 3], "Rphi(cm)", "", cut, "rdphi_LR")
#############################################################################################################



####################################################LAYER####################################################
#############################################################################################################
for i in range(2):
  plot1Dhist("rechit_prop_RdPhi_GE11[{}]".format(i), "rphi_res_L{}_even".format(i), event, [100, -3, 3], \
             "Rphi (cm)", "", "chamber_GE11[{}]%2 == 0".format(i), "rdphi_even_odd")
  plot1Dhist("rechit_prop_RdPhi_GE11[{}]".format(i), "rphi_res_L{}_odd".format(i), event, [100, -3, 3], \
             "Rphi (cm)", "", "chamber_GE11[{}]%2 == 1".format(i), "rdphi_even_odd")
#############################################################################################################

