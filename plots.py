import ROOT
from make_plot import plot1Dhist, plot1Dfit, plot2Dhist

f = ROOT.TFile("GEM_test.root")

event = f.Get("SliceTestAnalysis/MuonData")

plot1Dhist("rechit_prop_dX_GE11", "Local_x_residual", event, [100, -40, 40], "x(cm)", "", "", "residuals")
plot1Dhist("rechit_localx_GE11 - prop_localx_GE11", "Local_x_residual", event, [100, -40, 40], "x(cm)", "", "", "residuals")
plot1Dhist("rechit_x_GE11 - prop_x_GE11", "Global_x_residual", event, [100, -40, 40], "x(cm)", "", "", "residuals")
plot1Dhist("rechit_localx_GE11 + prop_localx_GE11", "Local_x_residual_add", event, [100, -4, 4], "x(cm)", "", "", "residuals")
plot1Dhist("rechit_phi_GE11 -  prop_phi_GE11", "Global_phi_residual", event, [100, -4, 4], "phi", "", "", "residuals")

plot2Dhist("rechit_x_GE11:rechit_y_GE11", "Rec_Hits", event, [1000, -300, 300, 1000, -300, 300], "", "", "", "rec_rec_global_desnity")
plot2Dhist("prop_x_GE11:prop_y_GE11", "Prop_Hits", event, [1000, -300, 300, 1000, -300, 300], "", "", "", "prop_prop_global_density")
plot2Dhist("prop_x_GE11:rechit_x_GE11", "prop_rec_global", event, [100, -30, 30, 100, -30, 30], "", "", "", "prop_rec_global_density")
plot2Dhist("prop_phi_GE11:rechit_phi_GE11", "prop_rec_phi_global", event, [100, -4, 4, 100, -4, 4], "", "", "", "prop_rec_global_density")
plot2Dhist("prop_localx_GE11:rechit_localx_GE11", "prop_rec_local", event, [100, -30, 30, 100, -30, 30], "", "", "", "prop_rec_local_density")

for i in range(2):
	plot1Dhist("rechit_localx_GE11[{}]".format(i), "Rec_localx_L{}_even".format(i), event, [100, -30, 30], "x(cm)", "", "chamber_GE11[{}]%2 == 0".format(i), "rec_localx_even_odd")
	plot1Dhist("rechit_localx_GE11[{}]".format(i), "Rec_localx_L{}_odd".format(i), event, [100, -30, 30], "x(cm)", "", "chamber_GE11[{}]%2 == 1".format(i), "rec_localx_even_odd")
	plot1Dhist("prop_localx_GE11[{}]".format(i), "Prop_localx_L{}_even".format(i), event, [100, -30, 30], "x(cm)", "", "chamber_GE11[{}]%2 == 0".format(i), "prop_localx_even_odd")
        plot1Dhist("prop_localx_GE11[{}]".format(i), "Prop_localx_L{}_odd".format(i), event, [100, -30, 30], "x(cm)", "", "chamber_GE11[{}]%2 == 1".format(i), "prop_localx_even_odd")
	for j in range(1,37):
		plot1Dhist("rechit_localx_GE11[{}]".format(i), "Rec_localx_layer{}_chamber{}".format(i,j), event, [100, -30, 30], "x(cm)", "", "chamber_GE11[{}] == {}".format(i, j), "rec_localx_LC")
		plot1Dhist("rechit_prop_dX_GE11[{}]".format(i), "Local_residual_layer{}_chamber{}".format(i, j), event, [100, -40, 40], "x(cm)", "", "chamber_GE11[{}] == {}".format(i, j), "local_res_LC")
		plot2Dhist("rechit_x_GE11:rechit_y_GE11", "Rec_xy_layer{}_chamber{}".format(i,j), event, [100, -300, 300, 100, -300, 300], "", "", "chamber_GE11[{}] == {}".format(i, j), "rec_xy")
		plot2Dhist("prop_x_GE11:prop_y_GE11", "Prop_xy_layer{}_chamber{}".format(i,j), event, [100, -300, 300, 100, -300, 300], "", "", "chamber_GE11[{}] == {}".format(i, j), "prop_xy")
		for k in range(1, 9):
			plot1Dhist("rechit_prop_dX_GE11[%d]"%i, "dx_layer%d_chamber%d_roll%d"%(i,j,k), event, [100, -40, 40], "x(cm)", "", "chamber_GE11[%d] == %d && roll_GE11[%d] == %d"%(i, j, i, k), "rec_dx_LCR")
			plot1Dhist("prop_r_GE11[{}]".format(i, i, i), "dx_layer{}_chamber{}_roll{}_test".format(i, j, k), event, [100, -300, 300], "phi", "", "chamber_GE11[{}] == {} &&  roll_GE11[{}]  == {}".format(i, j, i, k), "rec_dx_LCR_test")
