[
    ["rank(liabilities/assets)", 1.51, 1.26, 1.56, "PASS"], #Submitted
    ["rank(debt_lt/assets)", 1.37, 1.14, 1.90, "PASS"], #failed
    ["rank(liabilities/assets)+group_rank(revenue/equity,industry)", 1.49, 1.32, 1.88, "PASS"],
    ["0.6*rank(liabilities/assets)+0.4*group_rank(revenue/equity,industry)", 1.52, 1.36, 1.81, "PASS"],
    ["0.7*group_rank(sales/equity,industry)+0.3*rank(liabilities/assets)", 1.47, 1.24, 1.97, "PASS"],
    ["rank(anl4_ptp_flag)", 1.42, 1.39, 1.39, "PASS"],
    ["0.5*rank(anl4_ptp_flag)+0.5*rank(anl4_gric_flag)", 1.33, 1.01, 3.04, "PASS"],
    ["ts_mean(0.5*rank(anl4_ptp_flag)+0.5*rank(anl4_gric_flag),20)", 1.44, 1.13, 2.50, "PASS"],
    ["rank(ts_mean(rank(anl4_ptp_flag),20))", 1.38, 1.15, 11.04, "PASS"],
    ["rank(max_adjusted_net_income_guidance)", 1.49, 1.10, 1.00, "PASS"],
    ["rank(min_adjusted_net_income_guidance)", 1.51, 1.12, 1.00, "PASS"],
    ["0.5*rank(max_adjusted_net_income_guidance)+0.5*rank(min_adjusted_net_income_guidance)", 1.50, 1.11, 1.00, "PASS"],
    ["-rank(max_adjusted_net_income_guidance-min_adjusted_net_income_guidance)", 1.70, 1.32, 1.13, "PASS"],
    ["-rank(max_adjusted_net_income_guidance-min_adjusted_net_income_guidance)+0.2*rank(anl4_ptp_flag)", 1.83, 1.51, 1.64, "PASS"],#GOOD,
    ["rank(ts_mean(-rank(max_adjusted_net_income_guidance-min_adjusted_net_income_guidance),20))", 1.36, 1.06, 7.51, "PASS"],
    ["ts_mean(-rank(max_adjusted_net_income_guidance- min_adjusted_net_income_guidance),30)", 1.58, 1.19, 1.00, "PASS"],
    ["ts_mean(-rank(max_adjusted_net_income_guidance- min_adjusted_net_income_guidance),10)", 1.63, 1.25, 1.06, "PASS"],
    ["rank(max_adjusted_net_income_guidance/min_adjusted_net_income_guidance)", 1.63, 1.25, 1.07, "PASS"],
    ["-ts_mean(rank(max_adjusted_net_income_guidance/min_adjusted_net_income_guidance),10)", 1.56, 1.17, 1.02, "PASS"],
     ["0.7*(-rank(max_adjusted_net_income_guidance-min_adjusted_net_income_guidance))+0.3*rank(liabilities/assets)", 1.83, 1.60, 1.55, "PASS"], #GOOD # SUBMITTED
    ["rank(mdl177_garpanalystmodel_qgp_relgrowth)", 1.51, 1.28, 3.35, "PASS"],

]