[
    ["rank(liabilities/assets)", 1.51, 1.26, 1.56, "PASS"], @@@@@@@@@@@@@@@@@@@@
    ["rank(debt/equity)", 1.02, 0.72, 2.68, "FAIL"],
    ["rank(debt_lt/assets)", 1.37, 1.14, 1.90, "PASS"],@@@@@@@@@@@@@@@@@@@@
    ["rank(debt_st/assets)", 0.81, 0.41, 3.05, "FAIL"]
]


[
    ["rank(cash/assets)", -0.28, -0.14, 2.03, "FAIL"],
    ["rank(cash/liabilities)", -0.57, -0.37, 2.34, "FAIL"],
    ["rank(cash/debt)", -0.73, -0.52, 2.95, "FAIL"],
    ["rank(cash_st/liabilities)", -0.65, -0.42, 2.12, "FAIL"],
    ["rank(cashflow_op/debt", 0.22, 0.10, 2.93, "FAIL")]
]

[
    ["rank(return_equity)", 0.47, 0.27, 2.79, "FAIL"],
    ["rank(ebitda/assets)", 0.22, 0.11, 1.76, "FAIL"],
    ["rank(ebit/assets)", 0.17, 0.07, 1.59, "FAIL"],
    ["rank(income/assets)", 0.20, 0.09, 2.65, "FAIL"],
    ["rank(cashflow_op/assets)", 0.31, 0.17, 1.84, "FAIL"]
]

[
    ["rank(cashflow_op/income)", 0.30, 0.11, 3.05, "FAIL"],
    ["rank(cashflow_op/revenue)", 0.21, 0.09, 1.73, "FAIL"],
    ["rank(cashflow_op/ebitda)", 0.48, 0.17, 1.63, "FAIL"],
    ["rank(working_capital/assets)", -0.37, -0.19, 1.91, "FAIL"],
    ["rank(bookvalue_ps/assets)", -0.60, -0.28, 2.23, "FAIL"]
]

[
    ["rank(revenue/assets)", 0.91, 0.69, 1.89, "FAIL"],
    ["rank(sales/assets)", 0.91, 0.70, 1.90, "FAIL"],
    ["rank(inventory_turnover), 0.53, 0.26, 2.45, "FAIL"],
    ["rank(sales/equity)", 1.12, 0.90, 1.91, "FAIL"],
    ["rank(revenue/equity)", 1.12, 0.90, 1.90, "FAIL"]
]

########################################################################################################################


[
    ["rank(liabilities/sales)", 0.12, 0.03, 1.89, "FAIL"],
    ["rank(liabilities/revenue)", 0.11, 0.02, 1.87, "FAIL"],
    ["rank(liabilities/equity)", 1.29, 1.00, 1.75, "FAIL"] ************* failed because of Sub-universe Sharpe of 0.48 is below cutoff of 0.56.
    ["rank(debt_lt/equity)", 1.18, 0.89, 1.97, "FAIL"],
    ["rank(debt_lt/revenue)", 0.79, 0.45, 1.97, "FAIL"],
    ["rank(debt_lt/sales)", 0.74, 0.40, 2.07, "FAIL"],
    ["rank(liabilities/assets)-rank(cash/assets)", 0.87, 0.69, 2.26, "FAIL"],
    ["rank(debt_lt/assets)-rank(cash/assets)", 0.76, 0.57, 0.57, "FAIL"],
    ["ts_rank(debt_lt/assets,252)", -0.25, -0.25, -0.25, "FAIL"],
    ["ts_rank(liabilities/assets,252)", 0.06, 0.01, 3.28, "FAIL"],
    ["ts_rank(liabilities/equity,252)", -0.11, -0.02, -0.02, "FAIL"],
    ["rank(liabilities/assets)-rank(cash/assets)", 0.87, 0.69, 2.26, "FAIL"],
    ["rank(debt_lt/assets)-rank(cash/assets)", -0.56, -0.28, 2.08, "FAIL"]
    ["ts_rank(debt_lt/equity,252)", -0.22, -0.06, 3.68, "FAIL"]
]

########################################################################################################################

[
    ["rank(liabilities/assets)+group_rank(revenue/equity,industry)", 1.49, 1.32, 1.88, "PASS"], @@@@@@@@@@@@@@@@@@@@
    ["0.6*rank(liabilities/assets)+0.4*group_rank(revenue/equity,industry)", 1.52, 1.36, 1.81, "PASS"], @@@@@@@@@@@@@@@@@@@@
    ["group_rank(revenue/equity,industry)", 1.27, 0.97, 2.05, "FAIL"],
    ["group_rank(revenue/assets,industry)", 0.90, 0.59, 2.06, "FAIL"],
    ["group_rank(inventory_turnover,industry)", 0.55, 0.26, 2.69, "FAIL"],
    ["group_rank(sales/equity,industry)", 1.34, 1.03, 2.04, "FAIL"], ******* failed because of Sub-universe Sharpe of 0.57 is below cutoff of 0.58.
    ["group_rank(revenue/equity,industry)", 1.27, 0.97, 2.05, "FAIL"]
]

########################################################################################################################

[
    ["0.7*group_rank(sales/equity,industry)+0.3*rank(liabilities/assets)", 1.47, 1.24, 1.97, "PASS"],@@@@@@@@@@@@@@@@@@@@
    ["0.8*group_rank(sales/equity,industry)+0.2*rank(liabilities/assets)", 1.43, 1.17, 2.01, "FAIL"], ******* failed because of Self-correlation 0.7267 is above cutoff of 0.7 and Sharpe not better by 10.0% or more.
    ["0.5*group_rank(sales/equity,industry)+0.5*group_rank(revenue/equity,industry)", 1.27, 0.98, 2.05, "FAIL"],
    ["group_rank(ts_rank(revenue/equity,252),industry)", 0.56, 0.20, 4.56, "FAIL"],
    ["group_rank(ts_rank(sales/equity,252),industry)", 0.56, 0.20, 4.62, "FAIL"],
    ["0.5*group_rank(sales/equity,industry)+0.5*group_rank(revenue/assets,industry)", 1.11, 0.84, 2.11, "FAIL"]
]

########################################################################################################################

[
    ["0.5*group_rank(ts_rank(est_eps/close,252),industry)+0.5*rank(liabilities/assets)", 2.08, 1.97, 8.21, "FAIL"], #GOOD , failed because  of Self-correlation 0.7901 is above cutoff of 0.7 and Sharpe not better by 10.0% or more.

    ["0.6*group_rank(ts_rank(est_eps/close,252),industry)+0.4*rank(liabilities/assets)", 2.11, 1.95, 9.01, "FAIL"] #GOOD, failed because of Self-correlation 0.8723 is above cutoff of 0.7 and Sharpe not better by 10.0% or more.

    ["0.7*group_rank(ts_rank(est_eps/close,252),industry)+0.3*rank(liabilities/assets)", 2.08, 1.86, 9.48, "FAIL"] #GOOD, failed because of Self-correlation 0.9321 is above cutoff of 0.7 and Sharpe not better by 10.0% or more.

    ["0.5*group_rank(ts_rank(est_eps/close,252),industry)+0.5*group_rank(sales/equity,industry)", 2.07, 1.95, 7.88, "FAIL"] #GOOD, failed because of Self-correlation 0.8143 is above cutoff of 0.7 and Sharpe not better by 10.0% or more.

    ["0.6*group_rank(ts_rank(est_eps/close,252),industry)+0.4*group_rank(sales/equity,industry)", 2.14, 1.99, 8.86, "FAIL"] #GOOD, failed because of Self-correlation 0.8144 is above cutoff of 0.7 and Sharpe not better by 10.0% or more.
]

########################################################################################################################

[
    ["ts_rank(volume/adv20,20)", 0.34, 0.06, 51.35, "FAIL"],
    ["rank(volume/adv20)", 0.75, 0.20, 49.42, "FAIL"],
    ["-rank(ts_std_dev(returns,20))", 0.07, 0.02, 8.27, "FAIL"],
    ["rank(close/vwap)", -1.89, -0.79, 83.18, "FAIL"],
    ["group_rank(rank(volume/adv20),industry)", 0.71, 0.18, 49.69, "FAIL"],
    ["-rank(cap)", -0.13, -0.05, 1.72, "FAIL"],
    ["group_rank(rank(close/vwap),industry)", -1.93, -0.79, 83.76, "FAIL"],
    ["group_rank(-rank(cap),industry)", -0.13, 0.04, 2.11, "FAIL"]
]

########################################################################################################################

[
    ["-group_rank(rank(close/vwap),industry)", 1.93, 0.79, 83.76, "FAIL"],
    ["-rank(close/vwap)", 1.89, 0.79, 83.18, "FAIL"],
    ["-rank(returns)", 1.72, 0.83, 84.39, "FAIL"],
    ["group_rank(-rank(returns),industry)", 1.73, 0.81, 85.32, "FAIL"],
    ["rank((high-low)/close)", -0.04, -0.01, 33.52, "FAIL"],
    ["-group_rank(rank((high-low)/close),industry)", 0.01, 0.00, 35.68, "FAIL"],
    ["-rank((open-close)/close)", -1.88, -0.90, 83.34, "FAIL"],
    ["group_rank(-rank((open-close)/close),industry)", -1.88, -0.87, 84.03, "FAIL"]
]

########################################################################################################################

[
    ["ts_mean(-rank(returns),5)", 1.28, 0.78, 40.02, "FAIL"],
    ["ts_mean(-rank(close/vwap),5)", 1.02, 0.46, 38.73, "FAIL"],
    ["ts_mean(-group_rank(rank(close/vwap),industry),5)", 1.10, 0.50, 38.71, "FAIL"],
    ["ts_mean(group_rank(-rank(returns),industry),5)", 1.28, 0.76, 39.98, "FAIL"],
    ["ts_mean(-rank(returns),10)", 0.88, 0.54, 27.24, "FAIL"],
    ["ts_mean(-rank(close/vwap),10)", 1.06, 0.59, 26.17, "FAIL"],
    ["ts_mean(-group_rank(rank(close/vwap),industry),10)", 1.10, 0.60, 26.11, "FAIL"],
    ["ts_mean(group_rank(-rank(returns),industry),10)", 0.88, 0.52, 27.17, "FAIL"],
    ["0.5*(-rank(returns))+0.5*(-rank(close/vwap))", 1.90, 0.91, 84.31, "FAIL"],
    ["ts_mean(0.5*(-rank(returns))+0.5*(-rank(close/vwap)),5)", 1.25, 0.71, 39.64, "FAIL"],
    ["ts_mean(0.5*(-rank(returns))+0.5*(-rank(close/vwap)),10)", 1.00, 0.62, 26.92, "FAIL"]
]

########################################################################################################################

[
    ["rank(snt1_d1_earningsrevision)", 0.39, 0.13, 8.84, "FAIL"],
    ["rank(snt1_d1_netearningsrevision)", -0.26, -0.05, 23.25, "FAIL"],
    ["rank(snt1_d1_earningssurprise)", 0.34, 0.10, 2.49, "FAIL"],
    ["rank(snt1_d1_netrecpercent)", -0.08, -0.01, 1.12, "FAIL"],
    ["rank(snt1_d1_nettargetpercent)", -0.65, -0.36, 5.13, "FAIL"],
    ["rank(snt1_cored1_score)", -0.46, -0.20, 10.17, "FAIL"],
    ["rank(snt1_d1_uptargetpercent)", -0.45, -0.20, 5.39, "FAIL"],
    ["-rank(snt1_d1_sellrecpercent)", -0.38, -0.12, 0.98, "FAIL"],
    ["rank(snt1_cored1_score)", -0.46, -0.20, 10.17, "FAIL"],
    ["-rank(snt1_d1_downtargetpercent)", -0.79, -0.43, 4.85, "FAIL"],
    ["rank(snt1_d1_dynamicfocusrank)", -0.11, -0.03, 8.54, "FAIL"],
    ["rank(snt1_d1_stockrank)", -0.36, -0.19, 4.09, "FAIL"],
    ["rank(daily_equity_mood_indicator)", -1.11, -0.26, 41.41, "FAIL"],
    ["rank(weekly_equity_mood_index)", -0.46, -0.20, 10.17, "FAIL"],
    ["rank(snt1_d1_longtermepsgrowthest)", -0.11, -0.02, 1.15, "FAIL"],
    ["rank(snt1_d1_fundamentalfocusrank)", -0.13, -0.04, 2.20, "FAIL"]
]

########################################################################################################################

[
    ["rank(news_ratio_vol)", -0.38, -0.05, 118.41, "FAIL"],
    ["rank(news_tot_ticks)", -0.43, -0.07, 105.50, "FAIL"],
    ["rank(news_curr_vol)", -0.23, -0.03, 97.28, "FAIL"],
    ["rank(news_close_vol)", -0.06, -0.00, 143.30, "FAIL"],
    ["rank(news_eod_vwap/news_ton_last)", -0.28, -0.03, 126.10, "FAIL"],
    ["rank(news_all_vwap/news_ton_last)", -0.49, -0.07, 117.10, "FAIL"],
    ["rank(news_mins_20_pct_dn)", 0.09, 0.03, 80.38, "FAIL"],
    ["-rank(news_mins_10_pct_up)", -0.12, -0.03, 164.39, "FAIL"],
    ["rank(news_mins_5_chg)", 0.86, 0.25, 155.63, "FAIL"],
    ["rank(news_ratio_vol)", -0.38, -0.05, 118.41, "FAIL"],
    ["rank(news_tot_ticks)", -0.43, -0.07, 105.50, "FAIL"],
    ["rank(news_close_vol)", -0.06, -0.00, 143.30, "FAIL"],
    ["rank(news_curr_vol)", -0.23, -0.03, 97.28, "FAIL"],
    ["rank(news_eod_vwap/news_ton_last)", -0.28, -0.03, 126.10, "FAIL"],
    ["rank(news_all_vwap/news_ton_last)", -0.49, -0.07, 117.10, "FAIL"],
    ["rank(news_mins_20_pct_dn)", 0.09, 0.03, 80.38, "FAIL"],
    ["-rank(news_mins_10_pct_up)", -0.12, -0.03, 164.39, "FAIL"],
    ["rank(news_mins_5_chg)", 0.86, 0.25, 155.63, "FAIL"],
    ["group_rank(rank(news_ratio_vol),industry)", -0.40, -0.05, 118.42, "FAIL"]
]

########################################################################################################################

[
    ["rank(anl4_qfd1_az_dts_spe)", 1.20, 0.75, 4.79, "FAIL"],
    ["-group_rank(rank(anl4_qfd1_az_dts_spe),industry)", -1.29, -0.79, 5.17, "FAIL"],
    ["rank(anl4_qf_az_dts_spe)", 1.20, 0.75, 4.79, "FAIL"],
    ["rank(anl4_totassets_std)", 0.48, 0.23, 4.81, "FAIL"],
    ["rank(anl4_netprofit_number)", 1.20, 0.59, 3.26, "FAIL"],
    ["-group_rank(rank(anl4_totassets_std),industry)", -0.45, -0.20, 5.18, "FAIL"],
    ["rank(anl4_ptp_number)", 0.90, 0.39, 3.15, "FAIL"],
    ["rank(anl4_gric_number)", 0.64, 0.26, 2.95, "FAIL"],
    ["group_rank(anl4_netprofit_number,industry)", 1.22, 0.60, 3.37, "FAIL"],
    ["rank(anl4_totassets_number)", 0.72, 0.29, 2.70, "FAIL"],
    ["rank(anl4_epsr_flag)", -0.59, -0.30, 3.04, "FAIL"],
    ["rank(anl4_netprofit_flag)", 0.38, 0.17, 5.32, "FAIL"],
    ["rank(anl4_ptp_flag)", 1.42, 1.39, 1.39, "PASS"], @@@@@@@@@@@@@@@@@@@@
    ["0.5*rank(anl4_totassets_std)+0.5*rank(anl4_ptp_flag)", 0.52, 0.26, 4.90, "FAIL"],
    ["0.5*rank(anl4_qfd1_az_dts_spe)+0.5*rank(anl4_netprofit_number)", 1.34, 0.84, 5.13, "FAIL"]
]

########################################################################################################################

[
    ["rank(anl4_ebitda_flag)", 0.36, 0.13, 1.83, "FAIL"],
    ["rank(anl4_gric_flag)", 0.82, 0.43, 2.34, "FAIL"],
    ["rank(anl4_cfo_flag)", 1.11, 0.85, 2.60, "FAIL"],
    ["rank(anl4_cff_flag)", 1.13, 0.98, 2.89, "FAIL"],
    ["0.5*rank(anl4_ptp_flag)+0.5*rank(anl4_netprofit_flag)", 1.05, 0.80, 5.19, "FAIL"],
    ["0.5*rank(anl4_ptp_flag)+0.5*rank(anl4_gric_flag)", 1.33, 1.01, 3.04, "PASS"], @@@@@@@@@@@@@@@@@@@@
    ["rank(anl4_capex_flag)", 1.06, 0.68, 2.69, "FAIL"],
    ["rank(anl4_cfi_flag)", 1.18, 1.07, 2.88, "FAIL"],  ******** failde because of Sharpe of 1.18 is below cutoff of 1.25.
]

########################################################################################################################

[
    ["0.5*rank(anl4_ptp_flag)+0.5*rank(anl4_cfo_flag)", 1.27, 1.10, 3.37, "FAIL"], ****** failed because of Self-correlation 0.8377 is above cutoff of 0.7 and Sharpe not better by 10.0% or more

    ["0.5*rank(anl4_ptp_flag)+0.5*rank(anl4_cff_flag), 1.27, 1.23, 3.86, "FAIL"], ****** failed becaue of Self-correlation 0.887 is above cutoff of 0.7 and Sharpe not better by 10.0% or more.

    ["0.5*rank(anl4_ptp_flag)+0.5*rank(anl4_cfi_flag)", 1.31, 1.30, 3.83, "FAIL"], ****** failed because of Self-correlation 0.8868 is above cutoff of 0.7 and Sharpe not better by 10.0% or more.

    ["0.33*rank(anl4_ptp_flag)+0.33*rank(anl4_cfi_flag)+0.34*rank(anl4_cff_flag)", 1.20, 1.12, 3.76, "FAIL"], ****** failed because of Sharpe of 1.20 is below cutoff of 1.25.

    ["group_rank(0.5*rank(anl4_ptp_flag)+0.5*rank(anl4_gric_flag),industry)", 0.93, 0.50, 2.54, "FAIL"],

    ["ts_mean(rank(anl4_ptp_flag),20)", 1.55, 1.58, 3.12, "FAIL"], #GOOD failed because of Self-correlation 0.7161 is above cutoff of 0.7 and Sharpe not better by 10.0% or more.

    ["ts_mean(rank(anl4_cfi_flag),20)", 1.21, 1.10, 2.45, "FAIL"], ******* failed because of Sharpe of 1.21 is below cutoff of 1.25.

    ["ts_mean(0.5*rank(anl4_ptp_flag)+0.5*rank(anl4_gric_flag),20)", 1.44, 1.13, 2.50, "PASS"], @@@@@@@@@@@@@

    ["rank(anl4_ptp_flag)*rank(anl4_cfi_flag)", 1.11, 0.97, 3.47, "FAIL"],
    ["rank(anl4_ptp_flag)*rank(anl4_cff_flag)", 1.09, 0.93, 3.53, "FAIL"],
    ["rank(anl4_ptp_flag)*rank(anl4_cfo_flag)", 1.06, 0.78, 3.03, "FAIL"]
]

########################################################################################################################

[
    ["group_rank(ts_mean(rank(anl4_ptp_flag),20),industry)", 1.25, 0.98, 11.18, "FAIL"],

    ["group_neutralize(ts_mean(rank(anl4_ptp_flag),20),industry)", 1.51, 1.51, 3.10, "FAIL"], #GOOD , failed because of Self-correlation 0.7153 is above cutoff of 0.7 and Sharpe not better by 10.0% or more.

    ["rank(ts_mean(rank(anl4_ptp_flag),20))", 1.38, 1.15, 11.04, "PASS"], @@@@@@@@@@@@@@@@@@

    ["ts_mean(rank(anl4_ptp_flag),10)", 1.52, 1.53, 3.27, "FAIL"], #GOOD , failed because of Self-correlation 0.7044 is above cutoff of 0.7 and Sharpe not better by 10.0% or more.

    ["ts_mean(rank(anl4_ptp_flag),15)", 1.53, 1.55, 3.18, "FAIL"], #GOOD, failed because of Self-correlation 0.7098 is above cutoff of 0.7 and Sharpe not better by 10.0% or more.

    ["ts_mean(rank(anl4_ptp_flag),30), 1.56, 1.59, 3.02, "FAIL"], #GOOD, failed because of Self-correlation 0.7246 is above cutoff of 0.7 and Sharpe not better by 10.0% or more.

    ["ts_delta(rank(anl4_ptp_flag),5)", -0.65, -0.46, 42.53, "FAIL"],
    ["rank(anl4_ptp_flag)-ts_mean(rank(anl4_ptp_flag),20)", -0.80, -0.80, 18.65, "FAIL"],
    ["rank(anl4_gric_std)", 0.87, 0.64, 4.52, "FAIL"],
    ["rank(anl4_totassets_std)", 0.48, 0.23, 4.81, "FAIL"],
    ["rank(anl4_capex_std)", 0.41, 0.19, 4.62, "FAIL"]
]

########################################################################################################################

[
    ["rank(ts_mean(rank(anl4_ptp_flag),20))+0.1*rank(anl4_netprofit_number)", 0.60, 0.29, 11.20, "FAIL"],
    ["rank(ts_mean(rank(anl4_ptp_flag),20))+0.1*rank(anl4_ptp_number)", 0.54, 0.26, 11.93, "FAIL"],
    ["rank(ts_mean(rank(anl4_ptp_flag),20))+0.1*rank(anl4_gric_number)", 0.58, 0.31, 10.87, "FAIL"],
    ["rank(ts_mean(rank(anl4_ptp_flag),20))+0.1*rank(anl4_gric_std)", 0.60, 0.37, 11.89, "FAIL"],
    ["rank(ts_mean(rank(anl4_ptp_flag),20))+0.1*rank(anl4_totassets_std)", 0.23, 0.09, 12.15, "FAIL"],
    ["0.9*rank(ts_mean(rank(anl4_ptp_flag),20))+0.1*rank(anl4_netprofit_number)", 0.62, 0.31, 10.97, "FAIL"],
    ["0.8*rank(ts_mean(rank(anl4_ptp_flag),20))+0.2*rank(anl4_netprofit_number)", 0.79, 0.39, 8.65, "FAIL"],
    ["rank(max_adjusted_net_income_guidance)", 1.49, 1.10, 1.00, "PASS"], @@@@@@@@@@@@@@@@@@
    ["rank(min_adjusted_net_income_guidance)", 1.51, 1.12, 1.00, "PASS"], @@@@@@@@@@@@@@@@@@
    ["rank(anl4_ptp_high-anl4_ptp_low)", 0.84, 0.38, 3.16, "FAIL"],
    ["rank(anl4_netprofit_high-anl4_netprofit_low)", 1.10, 0.55, 3.27, "FAIL"],
    ["rank(anl4_capex_high-anl4_capex_low)", 0.13, 0.02, 2.73, "FAIL"]
]

########################################################################################################################

[
    ["0.5*rank(max_adjusted_net_income_guidance)+0.5*rank(min_adjusted_net_income_guidance)", 1.50, 1.11, 1.00, "PASS"], @@@@@@@@@@@@@@@@
    ["rank(max_adjusted_net_income_guidance-min_adjusted_net_income_guidance)", -1.70, -1.32, 1.13, "FAIL"], #DKFJSKJF

    ["ts_mean(rank(max_adjusted_net_income_guidance),20)", 1.46, 1.06, 0.90, "FAIL"],  ******** failed because of Turnover of 0.90% is below cutoff of 1%.

    ["ts_mean(rank(min_adjusted_net_income_guidance),20)", 1.47, 1.07, 0.90, "FAIL"], ******** failed because of Turnover of 0.90% is below cutoff of 1%.

    ["rank(ts_mean(rank(max_adjusted_net_income_guidance),20))", 0.64, 0.34, 7.31, "FAIL"],

    ["0.5*rank(anl4_ptp_flag)+0.5*rank(max_adjusted_net_income_guidance)", 1.76, 1.63, 2.41, "FAIL"], ******* failed because of Self-correlation 0.707 is above cutoff of 0.7 and Sharpe not better by 10.0% or more.

    ["0.5*rank(anl4_ptp_flag)+0.5*rank(min_adjusted_net_income_guidance)", 1.77, 1.64, 2.41, "FAIL"], #GOOD , failed because of Self-correlation 0.7066 is above cutoff of 0.7 and Sharpe not better by 10.0% or more.

    ["rank(ts_mean(rank(min_adjusted_net_income_guidance),20))", 0.64, 0.34, 7.31, "FAIL"],
    ["rank(max_adjusted_net_income_guidance)-rank(min_adjusted_net_income_guidance)", -0.88, -0.76, 2.35, "FAIL"],
]

########################################################################################################################

[
    ["-rank(max_adjusted_net_income_guidance-min_adjusted_net_income_guidance)", 1.70, 1.32, 1.13, "PASS"], @@@@@@@@@@@@@@@@@@@@@
    ["-rank(max_adjusted_net_income_guidance-min_adjusted_net_income_guidance)+0.2*rank(anl4_ptp_flag)", 1.83, 1.51, 1.64, "PASS"], #GOOD, @@@@@@@@@@@@@@@@@@@@@
]

########################################################################################################################

[
    ["-rank(anl4_netprofit_high-anl4_netprofit_low)", -1.10, -0.55, 3.27, "FAIL"],
    ["-rank(anl4_ebit_high-anl4_ebit_low)", -0.71, -0.29, 3.13, "FAIL"],
    ["-rank(anl4_epsr_high-anl4_epsr_low)", -1.03, -0.49, 3.12, "FAIL"],
    ["rank(ts_mean(-rank(max_adjusted_net_income_guidance-min_adjusted_net_income_guidance),20))", 1.36, 1.06, 7.51, "PASS"], @@@@@@@@@@@
    ["-rank(anl4_cfo_high-anl4_cfo_low)", -0.66, -0.28, 2.66, "FAIL"],
    ["rank(anl4_netprofit_value)", 0.25, 0.13, 1.91, "FAIL"],
    ["rank(anl4_gric_value)", 0.41, 0.28, 1.68, "FAIL"],
    ["rank(anl4_ptp_value)", 0.23, 0.12, 2.13, "FAIL"],
    ["rank(anl4_ebitda_value)", 0.35, 0.22, 1.66, "FAIL"],
    ["rank(anl4_ebit_value)", 0.30, 0.17, 1.97, "FAIL"],
    ["rank(anl4_ptp_high)", 0.43, 0.28, 1.23, "FAIL"],
    ["rank(anl4_netprofita_high)", 0.29, 0.15, 1.16, "FAIL"],
    ["rank(anl4_cfo_high)", 0.49, 0.34, 1.56, "FAIL"],
    ["rank(anl4_ebit_high)", 0.43, 0.28, 1.20, "FAIL"],
    ["rank(anl4_epsr_high)", 0.40, 0.25, 1.29, "FAIL"],
    ["rank(anl4_netprofit_low)", 0.33, 0.19, 1.31, "FAIL"],
    ["rank(anl4_ptp_low)", 0.34, 0.20, 1.29, "FAIL"],
    ["rank(anl4_ebit_low)", 0.37, 0.22, 1.26, "FAIL"],
    ["rank(anl4_epsr_low)", 0.33, 0.19, 1.35, "FAIL"],
    ["rank(anl4_cfo_low)", 0.41, 0.26, 1.63, "FAIL"]
    ["rank(anl4_ebit_median)", 0.40, 0.25, 1.19, "FAIL"],
    ["rank(anl4_gric_median)", 0.47, 0.32, 1.10, "FAIL"],
    ["rank(anl4_netprofit_median)", 0.39, 0.24, 1.24, "FAIL"],
    ["rank(anl4_cfo_median)", 0.46, 0.31, 1.56, "FAIL"],
    ["rank(anl4_median_epsreported)", 0.36, 0.22, 1.27, "FAIL"]
]

########################################################################################################################

[
    ["rank(anl4_ptp_number)", 0.90, 0.39, 3.15, "FAIL"],
    ["rank(sales_estimate_count_quarterly)", 1.62, 0.91, 3.15, "FAIL"],
    ["rank(sales_estimate_count)", 1.62, 0.91, 3.15, "FAIL"],
    ["rank(anl4_ebit_number)", 0.64, 0.23, 3.11, "FAIL"],
    ["rank(anl4_netprofit_number)", 1.20, 0.59, 3.26, "FAIL"],
    ["rank(anl4_ptp_number)/rank(anl4_ptp_high-anl4_ptp_low)", -0.14, -0.03, 4.51, "FAIL"],
    ["rank(anl4_netprofit_number)/ rank(anl4_netprofit_high-anl4_netprofit_low)", -0.07, -0.01, 4.58, "FAIL"],
    ["rank(anl4_ebit_number)/ rank(anl4_ebit_high-anl4_ebit_low)", -0.36, -0.12, 4.46, "FAIL"],
    ["rank(anl4_ptp_flag)*rank(anl4_ptp_number)", 0.73, 0.28, 3.39, "FAIL"],
    ["rank(anl4_ptp_flag)*rank(sales_estimate_count)", 1.40, 0.73, 3.42, "FAIL"],
    ["rank(anl4_ptp_flag)*-rank(anl4_ptp_high-anl4_ptp_low)", -0.78, -0.33, 3.41, "FAIL"]
]

########################################################################################################################

[
    ["ts_rank(-rank(max_adjusted_net_income_guidance- min_adjusted_net_income_guidance),20)", 0.13, 0.03, 38.88, "FAIL"],
    ["ts_mean(-rank(max_adjusted_net_income_guidance- min_adjusted_net_income_guidance),30)", 1.58, 1.19, 1.00, "PASS"], @@@@@@@@@@@@@
    ["ts_mean(-rank(max_adjusted_net_income_guidance- min_adjusted_net_income_guidance),10)", 1.63, 1.25, 1.06, "PASS"], @@@@@@@@@@@@@
    ["ts_zscore(-rank(max_adjusted_net_income_guidance- min_adjusted_net_income_guidance),20)", 0.98, 0.90, 28.01, "FAIL"],
    ["rank(ts_mean(-rank(max_adjusted_net_income_guidance- min_adjusted_net_income_guidance),10))", 0.86, 0.50, 8.30, "FAIL"],
    ["rank(min_adjusted_net_income_guidance/max_adjusted_net_income_guidance)", 0.49, 0.70, 4.65, "FAIL"],
    ["-rank((max_adjusted_net_income_guidance- min_adjusted_net_income_guidance)/abs(max_adjusted_net_income_guidance))", 0.49, 0.70, 4.65, "FAIL"],

    ["rank(max_adjusted_net_income_guidance/min_adjusted_net_income_guidance)", -1.63, -1.25, 1.07, "FAIL"],
    ["rank(max_adjusted_net_income_guidance/min_adjusted_net_income_guidance)", 1.63, 1.25, 1.07, "PASS"], @@@@@@@@@@@@@@@@@@
]

########################################################################################################################

[
    ["0.8*rank(max_adjusted_net_income_guidance/min_adjusted_net_income_guidance)+0.2*rank(anl4_ptp_flag)", -1.06, -0.61, 1.56, "FAIL"],
    ["rank(max_adjusted_net_income_guidance/min_adjusted_net_income_guidance)* rank(anl4_ptp_flag)", 0.32, 0.11, 2.23, "FAIL"],
    ["-ts_mean(rank(max_adjusted_net_income_guidance/min_adjusted_net_income_guidance),10)", 1.56, 1.17, 1.02, "PASS"], @@@@@@@@@@@@@@@@
    ["0.5*rank(max_adjusted_net_income_guidance/min_adjusted_net_income_guidance)+0.5*rank(anl4_ptp_flag)", 0.33, 0.11, 2.21, "FAIL"],
]

########################################################################################################################

[
    ["rank(actuals_value_currency_code)", 1.26, 1.04, 1.52, "FAIL"], ******* failed because of Sub-universe Sharpe of 0.46 is below cutoff of 0.55.

    ["rank(anl4_adjusted_netincome_ft)", 0.69, 0.34, 2.39, "FAIL"],
    ["rank(anl4_flag_erbfintax)", 0.42, 0.16, 2.02, "FAIL"],
    ["rank(anl4_ptpr_flag)", 1.30, 1.04, 2.01, "FAIL"], ******** failed because of Self-correlation 0.8616 is above cutoff of 0.7 and Sharpe not better by 10.0% or more.

    ["rank(anl4_tbve_ft)", 1.26, 1.05, 2.20, "FAIL"], ******** failed because of Self-correlation 0.715 is above cutoff of 0.7 and Sharpe not better by 10.0% or more.

    ["rank(anl4_ffo_flag)", 0.32, 0.16, 3.01, "FAIL"],
    ["rank(anl4_rd_exp_flag)", -0.06, -0.01, 1.75, "FAIL"],
    ["rank(actuals_value_currency_code)", 1.26, 1.04, 1.52, "FAIL"], ******** failed because of Sub-universe Sharpe of 0.46 is below cutoff of 0.55.

    ["rank(anl4_netdebt_flag)", 1.28, 1.11, 2.24, "FAIL"], ****** failed because of Sub-universe Sharpe of 0.54 is below cutoff of 0.55.
    
    ["rank(anl4_tot_gw_ft)", 1.04, 0.85, 2.45, "FAIL"], 
    ["rank(anl4_fcf_flag)", 1.04, 0.73, 2.39, "FAIL"],
    ["rank(anl4_qf_az_eps_number)", 1.36, 0.71, 3.08, "FAIL"],
    ["rank(anl4_qfd1_az_eps_number)", 1.36, 0.71, 3.08, "FAIL"],
    ["rank(est_eps)", 0.40, 0.25, 1.22, "FAIL"],
    ["rank(anl4_afv4_eps_mean)", 0.44, 0.28, 1.22, "FAIL"],
    ["rank(anl4_qfv4_eps_number)", 1.36, 0.71, 3.08, "FAIL"],
    ["rank(anl4_epsr_value)", 0.21, 0.09, 2.35, "FAIL"],
    ["rank(anl4_netprofita_low)", 0.26, 0.13, 1.22, "FAIL"],
    ["rank(reporting_currency_code_9)", 0.82, 0.77, 2.79, "FAIL"],
    ["rank(earnings_per_share_estimate_count)", 1.36, 0.71, 3.08, "FAIL"],
    ["rank(anl4_afv4_eps_high)", 0.48, 0.30, 1.25, "FAIL"],
    ["rank(actual_sales_value_quarterly)", 0.65, 0.51, 1.19, "FAIL"],
    ["rank(anl4_afv4_eps_number)", 0.73, 0.28, 2.65, "FAIL"],
    ["rank(sales_min_guidance_quarterly)", 1.00, 0.53, 1.02, "FAIL"],
    ["rank(actual_eps_value_quarterly)", 0.33, 0.19, 1.92, "FAIL"],
    ["rank(anl4_afv4_eps_low)", 0.38, 0.23, 1.28, "FAIL"],
]

########################################################################################################################

[
    ["rank(ts_mean(rank(anl4_netdebt_flag),20))", 1.38, 1.20, 4.58, "FAIL"], ******* failed because of Self-correlation 0.8555 is above cutoff of 0.7 and Sharpe not better by 10.0% or more.

    ["rank(ts_mean(rank(anl4_netdebt_flag),10))", 1.41, 1.26, 4.56, "FAIL"], ******* failed because of Sub-universe Sharpe of 0.55 is below cutoff of 0.61.

    ["ts_mean(rank(anl4_netdebt_flag),10)", 1.30, 1.14, 1.87, "FAIL"], ******** failed because of Sub-universe Sharpe of 0.54 is below cutoff of 0.56.

    ["0.8*(-rank(max_adjusted_net_income_guidance- min_adjusted_net_income_guidance))+0.2*rank(anl4_netdebt_flag)", 1.51, 1.30, 2.21, "FAIL"], ********** failed because of Self-correlation 0.7797 is above cutoff of 0.7 and Sharpe not better by 10.0% or more.

    ["ts_mean(rank(anl4_netdebt_flag),20)", 1.30, 1.14, 1.83, "FAIL"], ******* failed because of Sub-universe Sharpe of 0.53 is below cutoff of 0.56.
]

########################################################################################################################

[
    ["rank(debt/assets)*rank(working_capital)", 1.01, 0.75, 2.19, "FAIL"],
    ["zscore(rank(debt/assets)+rank(working_capital))", 0.87, 0.73, 1.90, "FAIL"],
    ["rank(debt/assets)+rank(working_capital)", 1.07, 0.86, 2.58, "FAIL"],
    ["rank(debt/assets)+rank(inventory_turnover)", 1.34, 1.07, 3.10, "FAIL"], ******* failed because of Self-correlation 0.7209 is above cutoff of 0.7 and Sharpe not better by 10.0% or more.

    ["rank(debt/assets)+rank(revenue)", 0.99, 0.93, 2.54, "FAIL"],
    ["group_rank(rank(debt/assets),industry)+group_rank(rank(revenue),industry)", 1.03, 0.91, 2.76, "FAIL"],
]


[
    ["quality = rank(ebit / assets);
efficiency = rank(sales / assets);
-ts_zscore(enterprise_value / ebitda, 63) + quality + efficiency", 1.07, 0.59, 25.56, "FAIL"],

    ["rank(ebit / sharesout / close)", 0.59, 0.45, 2.03, "FAIL"],

    ["eps_ratio = rank(ebit / sharesout / close);
trend = ts_av_diff(eps_ratio, 60);
rank(trend)", 1.00, 0.62, 10.16, "FAIL"],

    ["rank(ebit / capex)", 0.09, 0.03, 1.36, "FAIL"],

    ["rank(sales / assets)", 0.91, 0.70, 1.90, "FAIL"],
    ["rank(retained_earnings)", 0.04, 0.01, 2.86, "FAIL"],
    ["rank(cash_st / debt_st)", -0.47, -0.23, 3.21, "FAIL"],
    ["ts_zscore(enterprise_value / ebitda, 63)", -0.96, -0.59, 16.12, "FAIL"],
    
]

[
    ["value = -ts_zscore(enterprise_value / ebitda, 63);
    quality = rank(ebit / assets);
efficiency = rank(sales / assets);
rank(value + quality + efficiency)", 1.10, 0.84, 13.15, "FAIL"],

    ["base = rank(sales / assets) + rank(ebit / assets);
ts_av_diff(base, 40)", 0.70, 0.37, 11.34, "FAIL"],

    ["value = -rank(enterprise_value / ebitda);
reversal = -ts_zscore(close, 20);
rank(value + reversal)", 0.94, 0.55, 29.52, "FAIL"],

    ["high_vol = ts_rank(ts_std_dev(returns, 60), 126) > 0.5;
signal = rank(sales / assets);
trade_when(high_vol, signal, -signal)", 0.89, 0.67, 1.58, "FAIL"],
]



[
    ["rank(ts_rank(ebit / sharesout / close, 40))", 1.37, 1.05, 13.18, "FAIL"], ********* failed because of Self-correlation 0.7073 is above cutoff of 0.7 and Sharpe not better by 10.0% or more.

    ["-ts_zscore(close, 20)", 1.07, 0.69, 24.76, "FAIL"],
    ["event = volume > adv20;
alpha = -ts_delta(close, 5);
trade_when(event, alpha, -1)", 1.42, 0.94, 27.14, "FAIL"],

    ["-ts_rank(retained_earnings, 500)", 0.36, 0.20, 4.81, "FAIL"],
]

[    
    ["0.8*(-rank(max_adjusted_net_income_guidance-min_adjusted_net_income_guidance))+0.2*rank(liabilities/assets)", 1.90, 1.64, 1.52, "FAIL"], #GOOD ****** failed because of Self-correlation 0.831 is above cutoff of 0.7 and Sharpe not better by 10.0% or more.

    ["0.7*(-rank(max_adjusted_net_income_guidance-min_adjusted_net_income_guidance))+0.3*rank(liabilities/assets)", 1.83, 1.60, 1.55, "PASS"], #GOOD @@@@@@@@@@@@@@@@ # SUBMITTED

    ["0.8*(-rank(max_adjusted_net_income_guidance-min_adjusted_net_income_guidance))+0.2*group_rank(sales/equity,industry)", 1.03, 0.59, 1.63, "FAIL"], 
]
[
    ["rank(mean_news_impact_projection)", 0.00, 0.00, 85.78, "FAIL"], 
    ["rank(mean_merger_acquisition_sentiment)", 0.18, 0.02, 72.08, "FAIL"],
    ["-rank(mdl177_garpanalystmodel_qgp_vfpriceratio)", 1.09, 1.05, 3.07, "FAIL"], ******** failed because of Sharpe of 1.09 is below cutoff of 1.25. and Sub-universe Sharpe of 0.46 is below cutoff of 0.47.

    ["-rank(mdl177_fangma_gpam_usa_fangma_gpam11)", 1.10, 1.06, 3.06, "FAIL"], ****** failed because of Sharpe of 1.10 is below cutoff of 1.25. and Sub-universe Sharpe of 0.45 is below cutoff of 0.48.

    ["-rank(mdl177_garpanalystmodel_qgp_vfpriceratio)", 1.09, 1.05, 3.07, "FAIL"], ******* failed because of Sharpe of 1.09 is below cutoff of 1.25. and Sub-universe Sharpe of 0.46 is below cutoff of 0.47.

    ["],
    ["],
    ["],
    ["],
]

[
    ["0.7*(-rank(max_adjusted_net_income_guidance/min_adjusted_net_income_guidance))+ 0.3*rank(liabilities/assets)", 1.80, 1.57, 1.53, "FAIL"], ********** failed because of Self-correlation 0.9989 is above cutoff of 0.7 and Sharpe not better by 10.0% or more.

    ["0.7*rank(anl4_ptp_flag)+ 0.3*rank(liabilities/assets)", 1.73, 1.53, 2.08, "FAIL"], ******** failed because of Self-correlation 0.9021 is above cutoff of 0.7 and Sharpe not better by 10.0% or more.

    ["0.5*(-rank(max_adjusted_net_income_guidance-min_adjusted_net_income_guidance))+ 0.3*rank(liabilities/assets)+ 0.2*rank(anl4_ptp_flag)", 1.84, 1.67, 1.87, "FAIL"], ******** failed because of Self-correlation 0.9819 is above cutoff of 0.7 and Sharpe not better by 10.0% or more.
]


[
    ["0.6*rank(mdl177_5shortsentimentfactor_act_util)+ 0.4*rank(mdl177_garpanalystmodel_qgp_vfpriceratio)", 0.48, 0.16, 23.84, "FAIL"],

    ["-rank(mdl177_garpanalystmodel_qgp_vfpriceratio)", 1.09, 1.05, 3.07, "FAIL"], ******** failed because of Sharpe of 1.09 is below cutoff of 1.25. and Sub-universe Sharpe of 0.46 is below cutoff of 0.47.

    ["rank(mdl177_5shortsentimentfactor_act_util)", 1.03, 0.62, 26.43, "FAIL"],
]


[
    ["0.7*(-group_rank(mdl177_garpanalystmodel_qgp_vfpriceratio, industry))+ 0.3*rank(mdl177_5shortsentimentfactor_act_util)", 1.23, 1.23, 10.23, "FAIL"], ***** failed because of Sharpe of 1.23 is below cutoff of 1.25. and Sub-universe Sharpe of 0.48 is below cutoff of 0.53.

    ["rank(ts_rank(mdl177_5shortsentimentfactor_act_util, 20))", -0.75, -0.22, 51.70, "FAIL"],
    ["-0.5*rank(mdl177_garpanalystmodel_qgp_vfpriceratio)-0.5*group_rank(mdl177_garpanalystmodel_qgp_vfpriceratio, industry)", 1.14, 1.06, 3.30, "FAIL"], ******** failed because of Sharpe of 1.14 is below cutoff of 1.25. and Sub-universe Sharpe of 0.47 is below cutoff of 0.49.

    ["-group_rank(mdl177_garpanalystmodel_qgp_vfpriceratio, industry)", 1.18, 1.06, 3.63, "FAIL"], ******* failed because of Sharpe of 1.18 is below cutoff of 1.25. and Sub-universe Sharpe of 0.48 is below cutoff of 0.51.

    ["-rank(ts_mean(mdl177_garpanalystmodel_qgp_vfpriceratio, 5))", 1.07, 1.02, 2.41, "FAIL"], ******* failed because of Sharpe of 1.07 is below cutoff of 1.25.and Sub-universe Sharpe of 0.44 is below cutoff of 0.46.

]

[
    ["0.7*(-group_rank(mdl177_garpanalystmodel_qgp_vfpriceratio, sector))+ 0.3*rank(mdl177_5shortsentimentfactor_act_util)", 1.19, 1.25, 11.32, "FAIL"], ****** failed because of Sharpe of 1.19 is below cutoff of 1.25.and Sub-universe Sharpe of 0.5 is below cutoff of 0.52.

    ["0.5*(-group_rank(mdl177_garpanalystmodel_qgp_vfpriceratio, industry))+ 0.5*rank(mdl177_5shortsentimentfactor_act_util)", 1.19, 1.03, 17.95, "FAIL"], ********* failed because ofSharpe of 1.19 is below cutoff of 1.25. and Sub-universe Sharpe of 0.46 is below cutoff of 0.52. 

    ["0.7*(-group_rank(mdl177_garpanalystmodel_qgp_vfpriceratio, subindustry))+ 0.3*rank(mdl177_5shortsentimentfactor_act_util)", 1.24, 1.18, 9.18, "FAIL"], ******* failed because of Sharpe of 1.24 is below cutoff of 1.25. and Sub-universe Sharpe of 0.53 is below cutoff of 0.54.

    ["-rank(book_leverage_ratio_3)", 1.40, 1.12, 1.58, "FAIL"], ****** failed because of Sub-universe Sharpe of 0.57 is below cutoff of 0.61.

    ["rank(mdl177_garpanalystmodel_qgp_relgrowth)", 1.51, 1.28, 3.35, "PASS"], @@@@@@@@@@@@@
    ["-rank(mdl177_2_managementqualityfactor_saleicap)", 1.19, 1.01, 1.55, "FAIL"], ****** failed because of Sharpe of 1.19 is below cutoff of 1.25.

]

[
    ["rank(ts_mean(mdl177_garpanalystmodel_qgp_relgrowth, 5))", 1.52, 1.29, 2.57, "FAIL"],
    ["group_rank(mdl177_garpanalystmodel_qgp_relgrowth, sector)", 1.41, 1.13, 3.43, "FAIL"],
    ["0.7*rank(mdl177_garpanalystmodel_qgp_relgrowth)+ 0.3*(-rank(book_leverage_ratio_3))", 1.62, ,1.52, 3.39, "FAIL"],
    ["0.7*rank(mdl177_garpanalystmodel_qgp_relgrowth)+ 0.3*(-rank(max_adjusted_net_income_guidance - min_adjusted_net_income_guidance))", 1.60, 1.39, 3.33, "FAIL"],

    ["-group_rank(book_leverage_ratio_3, sector)", 1.39, 1.07, 1.67, "FAIL"], ******* failed because of Sub-universe Sharpe of 0.58 is below cutoff of 0.6.

    ["-group_rank(book_leverage_ratio_3, industry)", 1.46, 1.11, 1.78, "FAIL"], ****** failed because of Sub-universe Sharpe of 0.58 is below cutoff of 0.63.
]

[
    ["0.6*(-rank(book_leverage_ratio_3))+ 0.4*rank(mdl177_garpanalystmodel_qgp_relgrowth)", 1.66, 1.60, 2.77, "FAIL"], # GOOD ******* failed because of Self-correlation 0.8375 is above cutoff of 0.7 and Sharpe not better by 10.0% or more.

    ["0.6*(-rank(book_leverage_ratio_3))+ 0.4*rank(mdl177_garpanalystmodel_qgp_capeff)", 0.14, 0.03, 2.44, "FAIL"],
    ["0.6*(-rank(book_leverage_ratio_3))+ 0.4*rank(mdl177_garpanalystmodel_qgp_roefcf)", 1.02, 0.66, 2.17, "FAIL"],
    ["-rank(mdl177_2_earningsqualityfactor_ttmaccu)", -0.79, -0.42, 2.22, "FAIL"],
    ["-rank(mdl177_earningsqualityfactor_ttmaccu_alt)", -0.75, -0.39, 2.22, "FAIL"],
    ["rank(mdl177_v1_400_yoychgda)", -0.94, -0.52, 2.35, "FAIL"],
]

[
    ["rank(snt1_d1_earningsrevision)", 0.39, 0.13, 8.84, "FAIL"],
    ["rank(snt1_d1_netearningsrevision)", -0.26, -0.05, 23.25, "FAIL"],
    ["rank(snt1_d1_earningssurprise)", 0.34, 0.10, 2.49, "FAIL"],
    ["rank(snt1_d1_netrecpercent)", -0.08, -0.01, 1.12, "FAIL"],
    ["rank(snt1_d1_nettargetpercent)", -0.65, -0.36, 5.13, "FAIL"],
    ["rank(snt1_cored1_score)", -0.46, -0.20, 10.17, "FAIL"],
    ["rank(snt1_d1_uptargetpercent)", -0.45, -0.20, 5.39, "FAIL"],
    ["-rank(snt1_d1_sellrecpercent)", -0.38, -0.12, 0.98, "FAIL"],
    ["rank(snt1_cored1_score)", -0.46, -0.20, 10.17, "FAIL"],
    ["-rank(snt1_d1_downtargetpercent)", -0.79, -0.43, 4.85, "FAIL"],
    ["rank(snt1_d1_dynamicfocusrank)", -0.11, -0.03, 8.54, "FAIL"],
    ["rank(snt1_d1_stockrank)", -0.36, -0.19, 4.09, "FAIL"],
    ["rank(daily_equity_mood_indicator)", -1.11, -0.26, 41.41, "FAIL"],
    ["rank(weekly_equity_mood_index)", -0.46, -0.20, 10.17, "FAIL"],
    ["rank(snt1_d1_longtermepsgrowthest)", -0.11, -0.02, 1.15, "FAIL"],
    ["rank(snt1_d1_fundamentalfocusrank)", -0.13, -0.04, 2.20, "FAIL"]
    ["-rank(snt1_d1_dtstsespe)", -0.45, -0.25, 3.33, "FAIL"],
    ["-rank(implied_volatility_call_270)", -0.09, -0.04, 11.46, "FAIL"],
    ["-rank(historical_volatility_180)", -0.09, -0.03, 3.80, "FAIL"],
    ["-rank(parkinson_volatility_120)", 0.02, 0.00, 3.62, "FAIL"],
    
]

[
    ["rank(mdl177_2_vma2_vma2_va)", -0.71, -0.57, 4.99, "FAIL"],
    ["rank(mdl177_2_valuemomemtummodel_vma_composite)", -0.70, -0.49, 9.40, "FAIL"],
    ["-rank(mdl177_earningsqualityfactor_ttmaccu_alt)", -0.75, -0.39, 2.22, "FAIL"],
    ["rank(mdl177_5shortsentimentfactor_dmd_supply)", 1.12, 0.85, 2.98, "FAIL"],
    ["-rank(mdl177_5shortsentimentfactor_dmd_conc)", -0.63, -0.45, 14.64, "FAIL"],
    ["0.6*rank(mdl177_garpanalystmodel_qgp_relgrowth)+ 0.4*rank(mdl177_2_valuemomemtummodel_vma_composite)", 0.59, 0.32, 6.14, "FAIL"],
    ["-rank(snt1_d1_buyrecpercent)", -0.01, -0.00, 1.14, "FAIL"],
    ["-rank(snt1_d1_analystcoverage)", -0.22, -0.07, 1.59, "FAIL"]
]

[
    ["group_rank(mdl177_5shortsentimentfactor_dmd_supply, industry)", 1.12, 0.82, 3.50, "FAIL"],
    ["rank(ts_mean(mdl177_5shortsentimentfactor_dmd_supply, 10))", 1.13, 0.87, 1.91, "FAIL"],
    ["rank(ts_mean(mdl177_5shortsentimentfactor_dmd_supply, 5))", 1.11, 0.84, 2.25, "FAIL"],
    ["0.7*rank(mdl177_5shortsentimentfactor_dmd_supply)+ 0.3*rank(mdl177_garpanalystmodel_qgp_relgrowth)", 1.44, 1.26, 3.33, "FAIL"], ******* failed because of Self-correlation 0.8439 is above cutoff of 0.7 and Sharpe not better by 10.0% or more.
]

[
    ["rank(sales_growth)", -0.49, -0.21, 5.05, "FAIL"],
    ["rank(cashflow_op / income)", 0.30, 0.11, 3.05, "FAIL"],
    ["rank(operating_income / assets)", 0.37, 0.23, 2.45, "FAIL"],
    ["-rank(goodwill / assets)", -0.11, -0.03, 2.14, "FAIL"],
    ["rank(operating_income / invested_capital)", 0.41, 0.26, 2.68, "FAIL"],
    ["-rank(capex / assets)", -0.81, -0.42, 1.83, "FAIL"]
]

[
    ["group_rank(sales_growth, industry)", -0.34, -0.12, 5.34, "FAIL"],
    ["group_rank(operating_income / assets, industry)", 0.33, 0.17, 2.79, "FAIL"],
    ["group_rank(operating_income / assets, sector)", 0.36, 0.21, 2.67, "FAIL"],
    ["group_rank(return_equity, industry)", 0.37, 0.18, 3.01, "FAIL"],
    ["group_rank(return_assets, industry)", 0.14, 0.05, 2.90, "FAIL"],
    ["group_rank(cashflow_op / sales, industry)", 0.19, 0.07, 2.04, "FAIL"],
    ["rank(ts_delta(operating_income, 4))", -0.49, -0.12, 49.35, "FAIL"],
    ["rank(ts_delta(return_equity, 4))", -0.21, -0.03, 49.44, "FAIL"],
    ["rank(ts_delta(sales, 4))", -0.64, -0.18, 48.76,"FAIL"]
]

[
    ["rank(operating_income / assets) + rank(mdl177_garpanalystmodel_qgp_relgrowth)", 0.86, 0.74, 3.90, "FAIL"],
    ["rank(cashflow_op / (assets * mdl177_2_managementqualityfactor_saleicap))", 0.39, 0.24, 1.89, "FAIL"]
]
[
    ["0.7*(-group_rank(mdl177_garpanalystmodel_qgp_vfpriceratio, subindustry))+ 0.3*rank(mdl177_5shortsentimentfactor_act_util)", -0.43, -0.21, 11.55, "FAL"],

    ["rank(news_mins_10_pct_dn)", 0.73, 0.45, 167.26, "FAIL"],
    ["-rank(news_atr_ratio)", 0.42, 0.06, 104.88, "FAIL"],
    ["rank(news_indx_perf)", -0.36, -0.05, 122.99, "FAIL"],
    ["rank(news_mins_10_pct_up)", 0.12, 0.03, 164.39, "FAIL"],
    ["-rank(news_pe_ratio)", 0.09, 0.01, 75.50, "FAIL"],
    ["rank(news_tot_ticks)", -0.43, -0.07, 105.5, "FAIL"],
]

[
    ["rank(ts_mean(news_mins_10_pct_dn, 5))",  1.24, 0.85, 67.41, "FAIL"],
    ["rank(ts_mean(news_mins_10_pct_dn, 10))",  0.88, 0.53, 39.73, "FAIL"],
    ["rank(ts_mean(news_mins_10_pct_dn, 20))",  0.74, 0.42, 22.93, "FAIL"],
    ["-rank(ts_mean(news_atr_ratio, 5))", 0.14, 0.01, ],
    ["-rank(ts_mean(news_atr_ratio, 5))", | Sharpe: 0.14 | Fitness: 0.01],
    ["-rank(ts_mean(news_atr_ratio, 10))", | Sharpe: -0.20 | Fitness: -0.03],
    ["rank(ts_mean(news_indx_perf, 5))", | Sharpe: -0.58 | Fitness: -0.13],
    ["rank(ts_mean(news_indx_perf, 10))", | Sharpe: 0.03 | Fitness: 0.00  ]

]

[
    [❌ FAIL | roup_rank(ts_mean(news_mins_10_pct_dn, 5), industry) | Sharpe: 0.00 | Fitness: 0.00 | Turnover: 0.0%],
    [❌ FAIL | group_rank(ts_mean(news_mins_10_pct_dn, 5), sector) | Sharpe: 1.31 | Fitness: 0.91 | Turnover: 68.5%],
    [❌ FAIL | 0.7*rank(ts_mean(news_mins_10_pct_dn, 5))+ 0.3*rank(mdl177_garpanalystmodel_qgp_relgrowth) Sharpe: 1.71 | Fitness: 1.38 | Turnover: 67.8%] ********** failed because of Weight concentration 20.67% is above cutoff of 10% on 7/10/2019.
]

[
    [❌ FAIL | group_rank(ts_mean(news_mins_10_pct_dn, 10), sector) | Sharpe: 0.89 | Fitness: 0.53 | Turnover: 40.7%]
    [❌ FAIL | truncate(0.7*rank(ts_mean(news_mins_10_pct_dn, 5))+ 0.3*rank(mdl177_garpanalystmodel_qgp_relgrowth), 0.1) | Sharpe: 0.00 | Fitness: 0.00 | Turnover: 0.0%]

    [❌ FAIL | 0.5*rank(ts_mean(news_mins_10_pct_dn, 5))+ 0.5*rank(mdl177_garpanalystmodel_qgp_relgrowth) Sharpe: 2.03 | Fitness: 1.84 | Turnover: 66.9%], #GOOD , failed because of Weight concentration 20.77% is above cutoff of 10% on 7/10/2019.

    [❌ FAIL | rank(scl12_buzz) | Sharpe: -0.45 | Fitness: -0.05 | Turnover: 116.3%]
    [❌ FAIL | rank(snt_social_value) | Sharpe: 0.50 | Fitness: 0.10 | Turnover: 34.1%]
    [❌ FAIL | rank(snt_social_volume) | Sharpe: 0.40 | Fitness: 0.10 | Turnover: 30.5%]
    [❌ FAIL | rank(ts_mean(snt_buzz, 5)) | Sharpe: 0.29 | Fitness: 0.06 | Turnover: 31.8%]
]

[
    [❌ FAIL | rank(rel_ret_comp) | Sharpe: -0.36 | Fitness: -0.03 | Turnover: 135.6%],
    [❌ FAIL | rank(rel_ret_part) | Sharpe: -0.66 | Fitness: -0.08 | Turnover: 130.7%],
    [❌ FAIL | rank(rel_ret_all) | Sharpe: -0.63 | Fitness: -0.08 | Turnover: 138.3%],
    [❌ FAIL | -rank(rel_ret_comp) | Sharpe: 0.36 | Fitness: 0.03 | Turnover: 135.6%],
    [❌ FAIL | -rank(rel_ret_part) | Sharpe: 0.66 | Fitness: 0.08 | Turnover: 130.7%],
    [❌ FAIL | -rank(rel_ret_all) | Sharpe: 0.63 | Fitness: 0.08 | Turnover: 138.3%],
    [❌ FAIL | ts_mean(rank(rel_ret_comp),10) | Sharpe: 0.45 | Fitness: 0.08 | Turnover: 47.2%],
    [❌ FAIL | ts_mean(rank(rel_ret_part),10) | Sharpe: -0.03 | Fitness: -0.00 | Turnover: 47.3%],
    [❌ FAIL | ts_mean(rank(rel_ret_comp),20) | Sharpe: 0.53 | Fitness: 0.13 | Turnover: 33.2%],
    [❌ FAIL | ts_mean(rank(rel_ret_part),20) | Sharpe: -0.15 | Fitness: -0.02 | Turnover: 33.3%],
    [❌ FAIL | rank(rel_ret_comp)*rank(rel_num_comp) | Sharpe: 0.63 | Fitness: 0.09 | Turnover: 120.6%],
    [❌ FAIL | rank(rel_ret_part)*rank(rel_num_part) | Sharpe: 0.67 | Fitness: 0.09 | Turnover: 117.8%],
    [❌ FAIL | rank(rel_ret_all)*rank(rel_num_all) | Sharpe: 0.70 | Fitness: 0.11 | Turnover: 118.8%],
    [❌ FAIL | rank(implied_volatility_mean_10) | Sharpe: 0.10 | Fitness: 0.02 | Turnover: 33.1%],
    [❌ FAIL | rank(implied_volatility_mean_30) | Sharpe: 0.08 | Fitness: 0.02 | Turnover: 27.3%],
    [❌ FAIL | rank(implied_volatility_mean_90) | Sharpe: 0.07 | Fitness: 0.02 | Turnover: 20.3%],
    [❌ FAIL | -rank(implied_volatility_mean_10) | Sharpe: -0.10 | Fitness: -0.02 | Turnover: 33.1%],
    [❌ FAIL | rank(implied_volatility_call_30/implied_volatility_call_180) | Sharpe: -0.15 | Fitness: -0.01 | Turnover: 74.0%],
    [❌ FAIL | rank(implied_volatility_put_30/implied_volatility_put_180) | Sharpe: 0.07 | Fitness: 0.00 | Turnover: 74.2%],
    [❌ FAIL | rank(implied_volatility_mean_skew_30) | Sharpe: 0.44 | Fitness: 0.07 | Turnover: 100.3%],
    [❌ FAIL | rank(implied_volatility_mean_skew_90) | Sharpe: 0.43 | Fitness: 0.08 | Turnover: 91.7%],
    [❌ FAIL | -rank(implied_volatility_mean_skew_30) | Sharpe: -0.44 | Fitness: -0.07 | Turnover: 100.3%],
    [❌ FAIL | ts_mean(rank(implied_volatility_mean_skew_90),20)0.7*(-rank(max_adjusted_net_income_guidance-min_adjusted_net_income_guidance))+0.3*rank(rel_ret_comp) | Sharpe: 0.00 | Fitness: 0.00 | Turnover: 0.0%],

    [❌ FAIL | 0.7*(-rank(max_adjusted_net_income_guidance-min_adjusted_net_income_guidance))+0.3*(-rank(implied_volatility_mean_skew_90)) | Sharpe: 0.16 | Fitness: 0.02 | Turnover: 71.8%]
]

[
    [❌ FAIL | rank(growth_potential_rank_derivative) | Sharpe: -0.78 | Fitness: -0.51 | Turnover: 13.0%],
    [❌ FAIL | rank(multi_factor_acceleration_score_derivative) | Sharpe: -0.79 | Fitness: -0.51 | Turnover: 13.2%],
    [❌ FAIL | rank(relative_valuation_rank_derivative) | Sharpe: -0.78 | Fitness: -0.51 | Turnover: 13.0%],
    [❌ FAIL | rank(multi_factor_static_score_derivative) | Sharpe: -0.78 | Fitness: -0.50 | Turnover: 13.2%],
    [❌ FAIL | ts_mean(rank(growth_potential_rank_derivative),20) | Sharpe: -0.82 | Fitness: -0.56 | Turnover: 0.8%],
    [❌ FAIL | ts_mean(rank(multi_factor_acceleration_score_derivative),20) | Sharpe: -0.83 | Fitness: -0.57 | Turnover: 0.8%],
    [❌ FAIL | ts_mean(rank(relative_valuation_rank_derivative),20) | Sharpe: -0.81 | Fitness: -0.55 | Turnover: 0.8%],
    [❌ FAIL | rank(multi_factor_acceleration_score_derivative-multi_factor_static_score_derivative) | Sharpe: -0.44 | Fitness: -0.39 | Turnover: 6.7%],
    [❌ FAIL | rank(growth_potential_rank_derivative)*rank(relative_valuation_rank_derivative) | Sharpe: -0.76 | Fitness: -0.49 | Turnover: 13.4%,]
]
[
    [❌ FAIL | rank(ts_delta(est_eps_fy1,20)) | Sharpe: 0.00 | Fitness: 0.00 | Turnover: 0.0%] -> not supported 
    [❌ FAIL | rank(ts_delta(est_eps_fy2,20)) | Sharpe: 0.00 | Fitness: 0.00 | Turnover: 0.0%] -> not suported 
    [❌ FAIL | rank(ts_delta(earnings_per_share_estimate_count,20)) | Sharpe: 0.43 | Fitness: 0.13 | Turnover: 14.9%],
    [❌ FAIL | rank(ts_delta(sales_estimate_count,20)) | Sharpe: 0.51 | Fitness: 0.16 | Turnover: 15.0%],
    [❌ FAIL | -rank(debt/assets) | Sharpe: -1.20 | Fitness: -0.96 | Turnover: 2.7%],
    [❌ FAIL | -rank(total_liabilities/total_assets) | Sharpe: 0.00 | Fitness: 0.00 | Turnover: 0.0%] -> not supooeted
    [❌ FAIL | rank(cash/total_assets) | Sharpe: 0.00 | Fitness: 0.00 | Turnover: 0.0%] -> not suppoeted 
    [❌ FAIL | rank(current_ratio) | Sharpe: -0.69 | Fitness: -0.45 | Turnover: 2.2%],
    [❌ FAIL | rank(asset_turnover) | Sharpe: 0.00 | Fitness: 0.00 | Turnover: 0.0%] -> not supported
    [✅ PASS | 0.5*rank(ts_mean(news_mins_10_pct_dn, 5))+ 0.5*rank(mdl177_garpanalystmodel_qgp_relgrowth) Sharpe: 2.03 | Fitness: 1.84 | Turnover: 66.9%] ****** failed because of Weight concentration 18.33% is above cutoff of 10% on 7/10/2019.
    [✅ PASS | 0.4*rank(ts_mean(news_mins_10_pct_dn, 5))+ 0.6*rank(mdl177_garpanalystmodel_qgp_relgrowth) Sharpe: 2.02 | Fitness: 1.87 | Turnover: 65.9%] ****** failed because of Weight concentration 18.33% is above cutoff of 10% on 7/10/2019.
]

[
    [❌ FAIL | group_rank(ts_mean(news_mins_10_pct_dn, 10), sector) | Sharpe: 0.89 | Fitness: 0.53 | Turnover: 40.7%],
    [❌ FAIL | ts_mean(rank(anl4_fcf_flag),20) | Sharpe: 1.09 | Fitness: 0.89 | Turnover: 2.2%],
    [❌ FAIL | ts_mean(rank(anl4_ffo_flag),20) | Sharpe: 0.10 | Fitness: 0.03 | Turnover: 2.8%],
    [ERROR | rank(anl4_qf_az_eps_number)/ rank(earnings_per_share_estimate_count) | unsupported format string passed to NoneType.__format__],
    [ERROR | rank(anl4_qfv4_eps_number)/ rank(earnings_per_share_estimate_count) | unsupported format string passed to NoneType.__format__],
    [ERROR | rank(anl4_qf_az_eps_number)- rank(anl4_qfv4_eps_number) | unsupported format string passed to NoneType.__format__]

]

[
    [❌ FAIL | ts_mean(rank(anl4_fcf_flag),10) | Sharpe: 1.08 | Fitness: 0.88 | Turnover: 2.2%],
    [❌ FAIL | rank(ts_mean(rank(anl4_fcf_flag),20)) | Sharpe: 1.06 | Fitness: 0.84 | Turnover: 3.0%],
    [❌ FAIL | ts_mean(rank(anl4_fcf_flag),30) | Sharpe: 1.09 | Fitness: 0.89 | Turnover: 2.1%],
    [❌ FAIL | ts_mean(rank(anl4_fcf_flag),60) | Sharpe: 1.08 | Fitness: 0.88 | Turnover: 1.8%],
    [❌ FAIL | group_rank(news_mins_10_pct_dn, sector) | Sharpe: 0.71 | Fitness: 0.40 | Turnover: 169.3%,]
    [❌ FAIL | group_rank(ts_mean(news_mins_10_pct_dn,20), sector) | Sharpe: 0.78 | Fitness: 0.44 | Turnover: 23.6%],
    [❌ FAIL | -group_rank(ts_mean(news_mins_10_pct_up,10), sector) | Sharpe: -0.22 | Fitness: -0.06 | Turnover: 39.7%],
    [❌ FAIL | group_rank(ts_mean(news_mins_10_pct_dn,10)-ts_mean(news_mins_10_pct_up,10),sector) | Sharpe: -0.35 | Fitness: -0.16 | Turnover: 52.1%],
    [✅ PASS | 0.7*(-rank(max_adjusted_net_income_guidance-min_adjusted_net_income_guidance))+0.3*ts_mean(rank(anl4_fcf_flag),20) Sharpe: 1.48 | Fitness: 1.29 | Turnover: 2.0%]  ❌ FAIL because of Self-correlation 0.778 is above cutoff of 0.7 and Sharpe not better by 10.0% or more.
    [❌ FAIL | 0.7*(-rank(max_adjusted_net_income_guidance-min_adjusted_net_income_guidance))+0.3*group_rank(ts_mean(news_mins_10_pct_dn,10), sector) | Sharpe: 1.07 | Fitness: 0.71 | Turnover: 40.4%]
]

[
    [✅ PASS | 0.5*zscore(ts_mean(news_mins_10_pct_dn, 5))+ 0.5*rank(mdl177_garpanalystmodel_qgp_relgrowth) Sharpe: 1.47 | Fitness: 1.11 | Turnover: 68.9%] ❌ FAIL because of Weight concentration 18.01% is above cutoff of 10% on 4/9/2019.
    [✅ PASS | 0.5*rank(ts_mean(news_mins_10_pct_dn, 10))+ 0.5*rank(mdl177_garpanalystmodel_qgp_relgrowth) Sharpe: 1.67 | Fitness: 1.50 | Turnover: 39.6%] ❌ FAIL because of Sub-universe Sharpe of 0.23 is below cutoff of 0.72.
    [✅ PASS | 0.5*rank(ts_mean(news_mins_10_pct_dn, 15))+ 0.5*rank(mdl177_garpanalystmodel_qgp_relgrowth) Sharpe: 2.02 | Fitness: 2.04 | Turnover: 29.0%] ❌ FAIL becasue of Sub-universe Sharpe of 0.33 is below cutoff of 0.87.
    [✅ PASS | 0.3*rank(ts_mean(news_mins_10_pct_dn, 5))+ 0.7*rank(mdl177_garpanalystmodel_qgp_relgrowth) Sharpe: 1.91 | Fitness: 1.75 | Turnover: 64.8%] ❌ FAIL because of Weight concentration 16.67% is above cutoff of 10% on 7/10/2019.
]

[
    [✅ PASS | 0.5*group_rank(ts_mean(news_mins_10_pct_dn, 5), sector)+ 0.5*rank(mdl177_garpanalystmodel_qgp_relgrowth) Sharpe: 2.02 | Fitness: 1.81 | Turnover: 68.0%] #GOOD ❌ FAIL  because of Weight concentration 19.57% is above cutoff of 10% on 7/10/2019.

    [✅ PASS | 0.5*group_rank(ts_mean(news_mins_10_pct_dn, 5), industry)+ 0.5*rank(mdl177_garpanalystmodel_qgp_relgrowth) Sharpe: 1.95 | Fitness: 1.68 | Turnover: 69.6%] #GOOD ❌ FAIL because of Weight concentration 19.23% is above cutoff of 10% on 7/10/2019.

    [✅ PASS | 0.3*rank(ts_mean(news_mins_10_pct_dn, 10))+ 0.7*rank(mdl177_garpanalystmodel_qgp_relgrowth) Sharpe: 1.71 | Fitness: 1.64 | Turnover: 38.1%] #GOOD ❌ FAIL because of Sub-universe Sharpe of 0.45 is below cutoff of 0.74.

    [✅ PASS | 0.2*rank(ts_mean(news_mins_10_pct_dn, 10))+ 0.8*rank(mdl177_garpanalystmodel_qgp_relgrowth) Sharpe: 1.63 | Fitness: 1.55 | Turnover: 37.3%] #GOOD ❌ FAIL because of Sub-universe Sharpe of 0.53 is below cutoff of 0.71.

    [✅ PASS | 0.3*rank(ts_mean(news_mins_10_pct_dn, 15))+ 0.7*rank(mdl177_garpanalystmodel_qgp_relgrowth) Sharpe: 2.24 | Fitness: 2.55 | Turnover: 27.6%] ##Spectacular ❌ FAIL because of Sub-universe Sharpe of 0.61 is below cutoff of 0.97.
]

[
    [✅ PASS | 0.3*rank(ts_mean(news_mins_10_pct_dn, 15))+ 0.7*rank(mdl177_garpanalystmodel_qgp_relgrowth) Sharpe: 2.24 | Fitness: 2.55 | Turnover: 27.6%] ##Spectacular  ❌ FAIL because of Sub-universe Sharpe of 0.61 is below cutoff of 0.97.
    [✅ PASS | 0.3*rank(ts_backfill(ts_mean(news_mins_10_pct_dn, 15), 2))+ 0.7*rank(mdl177_garpanalystmodel_qgp_relgrowth) Sharpe: 2.25 | Fitness: 2.58 | Turnover: 26.4%]##Spectacular  ❌ FAIL because of Sub-universe Sharpe of 0.62 is below cutoff of 0.97.
]

[
    ["0.3*(ts_decay_linear(ts_mean(news_mins_10_pct_dn,15),5)*rank(volume*close)+ ts_decay_linear(ts_mean(news_mins_10_pct_dn,15),10)*(1-rank(volume*close)))+ 0.7*rank(mdl177_garpanalystmodel_qgp_relgrowth)", 1.06, 0.81, 27.39] ❌ FAIL

    [✅ PASS | 0.3*group_rank(ts_mean(news_mins_10_pct_dn,15), sector)+ 0.7*rank(mdl177_garpanalystmodel_qgp_relgrowth) Sharpe: 2.23 | Fitness: 2.52 | Turnover: 27.9%] ❌ FAIL because of Sub-universe Sharpe of 0.62 is below cutoff of 0.97.
    [✅ PASS | 0.2*rank(ts_backfill(ts_mean(news_mins_10_pct_dn,15),2))+ 0.8*rank(mdl177_garpanalystmodel_qgp_relgrowth) Sharpe: 2.20 | Fitness: 2.57 | Turnover: 25.6%] ❌ FAIL because of Sub-universe Sharpe of 0.71 is below cutoff of 0.95.
    [✅ PASS | 0.15*rank(ts_backfill(ts_mean(news_mins_10_pct_dn,15),2))+ 0.85*rank(mdl177_garpanalystmodel_qgp_relgrowth) Sharpe: 2.16 | Fitness: 2.53 | Turnover: 25.2%] ❌ FAIL because of Sub-universe Sharpe of 0.75 is below cutoff of 0.94.
    [✅ PASS | 0.3*rank(ts_backfill(ts_mean(news_mins_10_pct_dn,15),2))+ 0.7*rank(mdl177_garpanalystmodel_qgp_relgrowth) Sharpe: 2.25 | Fitness: 2.58 | Turnover: 26.4%]
    [✅ PASS | 0.3*rank(ts_decay_linear(ts_mean(news_mins_10_pct_dn,15),5))+ 0.7*rank(mdl177_garpanalystmodel_qgp_relgrowth) Sharpe: 2.28 | Fitness: 2.65 | Turnover: 26.9%] ## Spectacular ❌ FAIL because of Sub-universe Sharpe of 0.63 is below cutoff of 0.99.
    [✅ PASS | 0.3*rank(ts_decay_linear(ts_mean(news_mins_10_pct_dn,15),10))+ 0.7*rank(mdl177_garpanalystmodel_qgp_relgrowth) Sharpe: 2.31 | Fitness: 2.71 | Turnover: 26.7%] ## Spectacular ❌ FAIL because of Sub-universe Sharpe of 0.72 is below cutoff of 1.
]

[
    [✅ PASS | 0.3*rank(ts_decay_linear(ts_mean(news_mins_10_pct_dn,15),5)*rank(volume*close)+ts_decay_linear(ts_mean(news_mins_10_pct_dn,15),15)*(1-rank(volume*close)))+0.7*rank(mdl177_garpanalystmodel_qgp_relgrowth) Sharpe: 2.77 | Fitness: 3.56 | Turnover: 25.1%] ❌ FAIL because of Sub-universe Sharpe of 1.17 is below cutoff of 1.2.

    [✅ PASS | 0.3*group_rank(ts_decay_linear(ts_mean(news_mins_10_pct_dn,15),10),sector)+0.7*rank(mdl177_garpanalystmodel_qgp_relgrowth) Sharpe: 2.78 | Fitness: 3.55 | Turnover: 25.4%] ❌ FAIL because of Sub-universe Sharpe of 1.16 is below cutoff of 1.2.

    [✅ PASS | 0.3*group_zscore(ts_decay_linear(ts_mean(news_mins_10_pct_dn,15),10),sector)+0.7*rank(mdl177_garpanalystmodel_qgp_relgrowth) Sharpe: 2.31 | Fitness: 2.51 | Turnover: 26.6%] ❌ FAIL because of Sub-universe Sharpe of 0.4 is below cutoff of 1.

    [✅ PASS | 0.3*rank(ts_decay_linear(ts_mean(news_mins_10_pct_dn,15),10))*rank(volume*close)+0.7*rank(mdl177_garpanalystmodel_qgp_relgrowth) Sharpe: 2.72 | Fitness: 3.42 | Turnover: 26.7%]❌ FAIL because of Sub-universe Sharpe of 1.15 is below cutoff of 1.18.

    [✅ PASS | 0.3*rank(0.5*ts_mean(news_mins_10_pct_dn,10)+0.5*ts_mean(news_mins_10_pct_dn,40))+0.7*rank(mdl177_garpanalystmodel_qgp_relgrowth) Sharpe: 2.52 | Fitness: 2.86 | Turnover: 35.6%] ##Spectacular ✅ PASS 

    [✅ PASS | 0.3*rank(ts_decay_linear(ts_mean(news_mins_10_pct_dn,5),5)*rank(volume*close)+ts_decay_linear(ts_mean(news_mins_10_pct_dn,20),15)*(1-rank(volume*close)))+0.7*rank(mdl177_garpanalystmodel_qgp_relgrowth) Sharpe: 2.22 | Fitness: 2.16 | Turnover: 60.5%] ❌ FAIL because of Weight concentration 12.03% is above cutoff of 10% on 7/10/2019.

]

[
    [❌ FAIL | 0.3*rank(0.5*ts_mean(news_atr14,10)+0.5*ts_mean(news_atr14,40))+0.7*rank(mdl177_garpanalystmodel_qgp_relgrowth) | Sharpe: 1.08 | Fitness: 0.96 | Turnover: 8.4%]
    [❌ FAIL | 0.3*rank(0.5*ts_mean(news_indx_perf,10)+0.5*ts_mean(news_indx_perf,40))+0.7*rank(mdl177_garpanalystmodel_qgp_relgrowth) | Sharpe: 1.28 | Fitness: 0.93 | Turnover: 21.2%]
    [✅ PASS | 0.3*rank(0.5*ts_mean(news_max_up_ret,10)+0.5*ts_mean(news_max_up_ret,40))+0.7*rank(mdl177_garpanalystmodel_qgp_relgrowth) Sharpe: 1.27 | Fitness: 1.04 | Turnover: 16.8%] ❌ FAIL because of Self-correlation 0.7139 is above cutoff of 0.7 and Sharpe not better by 10.0% or more.
    [✅ PASS | 0.4*rank(0.5*ts_mean(news_mins_10_pct_dn,10)+0.5*ts_mean(news_mins_10_pct_dn,40))+0.6*rank(mdl177_garpanalystmodel_qgp_relgrowth) Sharpe: 2.52 | Fitness: 2.77 | Turnover: 36.2%] ## Spectacular ❌ FAIL because of Self-correlation 0.9847 is above cutoff of 0.7 and Sharpe not better by 10.0% or more.
    [✅ PASS | 0.3*rank(0.4*ts_mean(news_mins_10_pct_dn,10)+0.6*ts_mean(news_mins_10_pct_dn,60))+0.7*rank(mdl177_garpanalystmodel_qgp_relgrowth) Sharpe: 2.38 | Fitness: 2.64 | Turnover: 35.4%] ## Spectacular ❌ FAIL because of Self-correlation 0.9925 is above cutoff of 0.7 and Sharpe not better by 10.0% or more.
]
    

[
    [❌ FAIL | rank(abs_avg_pct_move_announcements_12) | Sharpe: 0.39 | Fitness: 0.21 | Turnover: 7.4%],
    [❌ FAIL | rank(absolute_average_announcement_percent_move) | Sharpe: 0.33 | Fitness: 0.17 | Turnover: 2.5%],
    [❌ FAIL | rank(announcement_effect_10) | Sharpe: 0.87 | Fitness: 0.65 | Turnover: 8.5%],
    [❌ FAIL | rank(announcement_effect_9) | Sharpe: 0.90 | Fitness: 0.66 | Turnover: 8.5%],
    [❌ FAIL | rank(announcement_effect_8) | Sharpe: 0.95 | Fitness: 0.71 | Turnover: 8.6%],
    [❌ FAIL | rank(announcement_effect_7) | Sharpe: 1.13 | Fitness: 0.89 | Turnover: 8.8%],
    [❌ FAIL | rank(best_fit_implied_announcement_effect) | Sharpe: 0.98 | Fitness: 0.20 | Turnover: 88.5%],
    [❌ FAIL | rank(eighth_event_option_effect) | Sharpe: 1.04 | Fitness: 0.82 | Turnover: 3.7%],
    [✅ PASS | rank(eighth_event_straddle_price_percent_of_equity) Sharpe: 1.77 | Fitness: 1.55 | Turnover: 7.9%], ❌ FAIL 
    [❌ FAIL | rank(eighth_historical_announcement_percent_move) | Sharpe: 0.65 | Fitness: 0.22 | Turnover: 4.4%],
    [❌ FAIL | ts_mean(rank(announcement_effect_10),10) | Sharpe: 0.97 | Fitness: 0.78 | Turnover: 2.4%],
    [❌ FAIL | ts_mean(rank(announcement_effect_10),20) | Sharpe: 0.97 | Fitness: 0.79 | Turnover: 2.3%],
    [❌ FAIL | ts_mean(rank(announcement_effect_9),10) | Sharpe: 0.97 | Fitness: 0.76 | Turnover: 2.5%],
    [❌ FAIL | ts_mean(rank(announcement_effect_9),20) | Sharpe: 0.94 | Fitness: 0.73 | Turnover: 2.3%],
    [❌ FAIL | ts_mean(rank(announcement_effect_8),10) | Sharpe: 1.05 | Fitness: 0.84 | Turnover: 2.6%],
    [❌ FAIL | ts_mean(rank(announcement_effect_8),20) | Sharpe: 1.04 | Fitness: 0.84 | Turnover: 2.4%],
    [❌ FAIL | ts_mean(rank(best_fit_implied_announcement_effect),10) | Sharpe: 0.69 | Fitness: 0.32 | Turnover: 19.2%],
    [❌ FAIL | ts_mean(rank(best_fit_implied_announcement_effect),20) | Sharpe: 0.69 | Fitness: 0.42 | Turnover: 12.0%],
    [❌ FAIL | ts_mean(rank(eighth_event_option_effect),10) | Sharpe: 1.05 | Fitness: 0.84 | Turnover: 2.6%],
    [❌ FAIL | ts_mean(rank(eighth_historical_announcement_percent_move),20) | Sharpe: 0.08 | Fitness: 0.01 | Turnover: 3.2%],
    [❌ FAIL | rank(best_fit_implied_announcement_effect-abs_avg_pct_move_announcements_12) | Sharpe: -0.24 | Fitness: -0.05 | Turnover: 48.6%],
    [❌ FAIL | rank(best_fit_implied_announcement_effect-absolute_average_announcement_percent_move) | Sharpe: -0.18 | Fitness: -0.04 | Turnover: 45.8%],
    [❌ FAIL | rank(eighth_event_option_effect-eighth_historical_announcement_percent_move) | Sharpe: -0.26 | Fitness: -0.06 | Turnover: 4.4%],
    [❌ FAIL | rank(announcement_effect_10-announcement_effect_8) | Sharpe: 0.24 | Fitness: 0.06 | Turnover: 9.3%],
    [❌ FAIL | rank(announcement_effect_10-announcement_effect_7) | Sharpe: 0.28 | Fitness: 0.08 | Turnover: 9.2%],
    [❌ FAIL | rank(announcement_effect_9-announcement_effect_7) | Sharpe: 0.05 | Fitness: 0.00 | Turnover: 9.3%],
    [❌ FAIL | rank(announcement_effect_8-announcement_effect_7) | Sharpe: -0.27 | Fitness: -0.06 | Turnover: 10.2%],
    [❌ FAIL | rank(abs_avg_pct_move_announcements_12-best_fit_implied_announcement_effect) | Sharpe: 0.24 | Fitness: 0.05 | Turnover: 48.6%],
    [❌ FAIL | rank(absolute_average_announcement_percent_move-best_fit_implied_announcement_effect) | Sharpe: 0.18 | Fitness: 0.04 | Turnover: 45.8%],
    [❌ FAIL | rank(eighth_historical_announcement_percent_move-eighth_event_option_effect) | Sharpe: 0.26 | Fitness: 0.06 | Turnover: 4.4%],
    [❌ FAIL | rank(ts_mean(best_fit_implied_announcement_effect,20)) | Sharpe: 0.68 | Fitness: 0.40 | Turnover: 11.8%],
    [❌ FAIL | rank(ts_mean(announcement_effect_10,20)) | Sharpe: 0.96 | Fitness: 0.78 | Turnover: 2.3%],
    [❌ FAIL | rank(ts_mean(announcement_effect_9,20)) | Sharpe: 0.94 | Fitness: 0.72 | Turnover: 2.4%],
    [❌ FAIL | rank(best_fit_implied_announcement_effect)*rank(atm_volatility_month2) | Sharpe: 0.51 | Fitness: 0.13 | Turnover: 78.3%],
    [❌ FAIL | rank(best_fit_implied_announcement_effect)*rank(avg_option_volume_20d) | Sharpe: 0.94 | Fitness: 0.24 | Turnover: 60.0%],
    [❌ FAIL | 0.5*rank(ts_mean(best_fit_implied_announcement_effect,20))+0.5*rank(atm_volatility_month2) | Sharpe: 0.39 | Fitness: 0.15 | Turnover: 29.3%],
    [✅ PASS | 0.5*rank(ts_mean(announcement_effect_10,20))+0.5*rank(avg_option_volume_20d) Sharpe: 1.57 | Fitness: 1.16 | Turnover: 9.5%], ❌ FAIL because of Weight is too strongly concentrated or too few instruments are assigned weight. Sub-universe Sharpe of 0.28 is below cutoff of 0.68.
]

[

    [✅ PASS | 0.3*rank(0.5*ts_mean(best_fit_implied_announcement_effect,10)+0.5*ts_mean(best_fit_implied_announcement_effect,40))+0.7*rank(mdl177_garpanalystmodel_qgp_relgrowth) Sharpe: 1.33 | Fitness: 1.25 | Turnover: 11.3%]

    [❌ FAIL | 0.3*rank(0.5*ts_mean(fscore_quality,10)+0.5*ts_mean(fscore_quality,40))+0.7*rank(mdl177_garpanalystmodel_qgp_relgrowth) | Sharpe: -0.45 | Fitness: -0.17 | Turnover: 12.9%],
    [❌ FAIL | 0.3*rank(0.5*ts_mean(fscore_total,10)+0.5*ts_mean(fscore_total,40))+0.7*rank(mdl177_garpanalystmodel_qgp_relgrowth) | Sharpe: -0.71 | Fitness: -0.30 | Turnover: 13.5%],
    [✅ PASS | 0.3*rank(0.5*ts_mean(announcement_effect_10,10)+0.5*ts_mean(announcement_effect_10,40))+0.7*rank(mdl177_garpanalystmodel_qgp_relgrowth) Sharpe: 1.31 | Fitness: 1.28 | Turnover: 5.5%]
    [✅ PASS | 0.3*rank(0.5*ts_mean(atm_volatility_month2,10)+0.5*ts_mean(atm_volatility_month2,40))+0.7*rank(mdl177_garpanalystmodel_qgp_relgrowth) Sharpe: 1.26 | Fitness: 1.24 | Turnover: 6.5%]
    [✅ PASS | 0.3*rank(0.5*ts_mean(atm_volatility_month2,10)+0.5*ts_mean(atm_volatility_month2,40))+0.7*rank(mdl177_garpanalystmodel_qgp_relgrowth) Sharpe: 1.26 | Fitness: 1.24 | Turnover: 6.5%]
    [❌ FAIL | 0.3*rank(ts_mean(fscore_momentum,20))+0.7*rank(mdl177_garpanalystmodel_qgp_relgrowth) | Sharpe: -0.37 | Fitness: -0.14 | Turnover: 12.9%],
    [❌ FAIL | 0.3*rank(ts_mean(fscore_growth,20))+0.7*rank(mdl177_garpanalystmodel_qgp_relgrowth) | Sharpe: -0.21 | Fitness: -0.06 | Turnover: 12.3%],
    [❌ FAIL | 0.3*rank(ts_mean(fscore_value,20))+0.7*rank(mdl177_garpanalystmodel_qgp_relgrowth) | Sharpe: 0.48 | Fitness: 0.27 | Turnover: 13.3%],
    [❌ FAIL | 0.3*rank(ts_mean(fscore_total,20))+0.7*rank(mdl177_garpanalystmodel_qgp_relgrowth) | Sharpe: -0.29 | Fitness: -0.09 | Turnover: 13.6%],
    [✅ PASS | 0.3*rank(ts_mean(best_fit_implied_announcement_effect,20))+0.7*rank(mdl177_garpanalystmodel_qgp_relgrowth) Sharpe: 1.34 | Fitness: 1.25 | Turnover: 10.2%],
    [❌ FAIL | 0.3*rank(best_fit_implied_announcement_effect-abs_avg_pct_move_announcements_12)+0.7*rank(mdl177_garpanalystmodel_qgp_relgrowth) | Sharpe: 0.78 | Fitness: 0.37 | Turnover: 33.9%],
    [✅ PASS | 0.3*rank(announcement_effect_10-announcement_effect_8)+0.7*rank(mdl177_garpanalystmodel_qgp_relgrowth) Sharpe: 1.32 | Fitness: 1.07 | Turnover: 11.8%],
    [✅ PASS | 0.3*rank(ts_mean(announcement_effect_10,20))+0.7*rank(mdl177_garpanalystmodel_qgp_relgrowth) Sharpe: 1.31 | Fitness: 1.28 | Turnover: 5.5%],
    [❌ FAIL | 0.3*rank(best_fit_implied_announcement_effect-eighth_historical_announcement_percent_move)+0.7*rank(mdl177_garpanalystmodel_qgp_relgrowth) | Sharpe: 1.38 | Fitness: 0.86 | Turnover: 19.9%],
    [✅ PASS | 0.3*rank(ts_mean(rel_num_part,20))+0.7*rank(mdl177_garpanalystmodel_qgp_relgrowth) Sharpe: 1.65 | Fitness: 1.71 | Turnover: 4.9%],
    [✅ PASS | 0.3*rank(ts_mean(rel_num_cust,20))+0.7*rank(mdl177_garpanalystmodel_qgp_relgrowth) Sharpe: 1.51 | Fitness: 1.45 | Turnover: 4.9%],
    [✅ PASS | 0.3*rank(rel_num_part)+0.7*rank(mdl177_garpanalystmodel_qgp_relgrowth) Sharpe: 1.65 | Fitness: 1.71 | Turnover: 4.9%],
    [✅ PASS | 0.3*rank(rel_num_cust)+0.7*rank(mdl177_garpanalystmodel_qgp_relgrowth) Sharpe: 1.52 | Fitness: 1.46 | Turnover: 5.0%],
    [✅ PASS | 0.3*rank(rel_num_all)+0.7*rank(mdl177_garpanalystmodel_qgp_relgrowth) Sharpe: 1.60 | Fitness: 1.70 | Turnover: 5.1%],
    [❌ FAIL | 0.3*rank(ts_mean(implied_volatility_mean_30,20))+0.7*rank(mdl177_garpanalystmodel_qgp_relgrowth) | Sharpe: 1.19 | Fitness: 1.14 | Turnover: 6.4%],
    [❌ FAIL | 0.3*rank(implied_volatility_mean_skew_90)+0.7*rank(mdl177_garpanalystmodel_qgp_relgrowth) | Sharpe: 1.11 | Fitness: 0.44 | Turnover: 61.5%],
    [❌ FAIL | 0.3*rank(implied_volatility_call_30/implied_volatility_call_180)+0.7*rank(mdl177_garpanalystmodel_qgp_relgrowth) | Sharpe: 1.53 | Fitness: 0.64 | Turnover: 52.6%],
    [❌ FAIL | 0.3*rank(atm_volatility_month2)+0.7*rank(mdl177_garpanalystmodel_qgp_relgrowth) | Sharpe: 1.36 | Fitness: 1.00 | Turnover: 23.5%],
    [❌ FAIL | 0.3*rank(atm_volatility_month1/atm_volatility_month3)+0.7*rank(mdl177_garpanalystmodel_qgp_relgrowth) | Sharpe: 1.48 | Fitness: 0.62 | Turnover: 54.1%],
    [❌ FAIL | rank(best_fit_implied_announcement_effect-absolute_average_announcement_percent_move) | Sharpe: -0.18 | Fitness: -0.04 | Turnover: 45.8%],
    [❌ FAIL | rank(best_fit_implied_announcement_effect-abs_avg_pct_move_announcements_12) | Sharpe: -0.24 | Fitness: -0.05 | Turnover: 48.6%],
    [❌ FAIL | rank(ts_mean(best_fit_implied_announcement_effect,20))*rank(avg_option_volume_20d) | Sharpe: 0.83 | Fitness: 0.44 | Turnover: 13.6%]
]




[
    ["multiply(rank(-returns),rank(volume/adv20),filter=true)", 2.00, 0.99, 62.83, ❌ FAIL] because of Fitness of 0.99 is below cutoff of 1.

    ["implied_volatility_call_120/parkinson_volatility_120", 1.78, 1.72, 16.37, ❌ FAIL] ## GOOD becuause of Weight is too strongly concentrated or too few instruments are assigned weight. (Universe - TOP1000, )

    ["implied_volatility_call_120/parkinson_volatility_120", 1.52, 0.94, 26.04 ❌ FAIL] ## GOOD becuause of Weight is too strongly concentrated or too few instruments are assigned weight. (Universe - TOP3000) because of Fitness of 0.94 is below cutoff of 1. Weight concentration 50% is above cutoff of 10% on 9/5/2019.

    ["multiply(rank(-returns),rank(volume/adv20),filter=true)", 1.80, 1.18, 38.41, ✅ PASS] (performance is -125 which is not good) (Nertralization - Sector, Decay- 10)

    ["multiply(rank(-returns),rank(volume/adv20),filter=true)", 0.75, 0.43, 33.32, ❌ FAIL] (performance is +613 which is not good) (Nertralization - Market, Decay- 10, trancation-0.04) because of Sharpe of 0.75 is below cutoff of 2. Fitness of 0.43 is below cutoff of 1.30. (USA/d0/TOP3000)

]

[
    ["vector_neut(-scl12_buzz,150)", 1.69, 0.92, 68.31, ❌ FAIL] because of Fitness of 0.92 is below cutoff of 1. Weight concentration 18.23% is above cutoff of 10% on 9/26/2022. Sub-universe Sharpe of 0.51 is below cutoff of 0.73.

    ["-ts_rank(fn_liab_fair_val_l1_a,129)", 1.36, 1.10, 4.34, ✅ PASS] #Submitted

    ["ts_rank(fnd6_fopo/debt_lt,345)", 0.86, 0.33, 3.41, ❌ FAIL] because of Sharpe of 0.86 is below cutoff of 1.25. Fitness of 0.33 is below cutoff of 1. Sub-universe Sharpe of 0.27 is below cutoff of 0.37.

    ["ts_backfill(vec_avg(nws12_prez_4l),800)", 1.09, 0.56, 4.25,❌ FAIL] because of Sharpe of 1.09 is below cutoff of 1.25. Fitness of 0.56 is below cutoff of 1.

    ["multiply(rank(returns), rank(volume/adv20), filter=true)", -1.27, -0.49, 63.23, ❌ FAIL] because of Sharpe of -1.27 is below cutoff of 1.25. Fitness of -0.49 is below cutoff of 1. Sub-universe Sharpe of -0.87 is below cutoff of -0.55.

    ["multiply(ts_rank(-returns,5), ts_rank(volume/adv20,5), filter=true)", 1.85, 0.65, 80.52, ❌ FAIL] because of Fitness of 0.65 is below cutoff of 1. Turnover of 80.52% is above cutoff of 70%.

    ["0.6*multiply(rank(-returns),rank(volume/adv20),filter=true)+0.4*rank(mdl177_garpanalystmodel_qgp_relgrowth)", 2.61, 1.71, 39.23, ✅ PASS] (performace is -285 so not possible to submit)

    ["0.5*multiply(rank(-returns),rank(volume/adv20),filter=true)+0.5*rank(0.5*ts_mean(news_mins_10_pct_dn,10)+0.5*ts_mean(news_mins_10_pct_dn,40))", 1.09, 0.60, 61.95, ❌ FAIL] because of Sharpe of 1.09 is below cutoff of 1.25. Fitness of 0.60 is below cutoff of 1.

    ["multiply(group_rank(-returns,sector),rank(volume/adv20),filter=true)", 2.02, 1.00, 63.38, ❌ FAIL] because of Self-correlation 0.7319 is above cutoff of 0.7 and Sharpe not better by 10.0% or more. (Performance is -358)

    ["rank(implied_volatility_call_120/parkinson_volatility_120)", 1.83, 1.22, 21.52, ❌ FAIL] because of Weight is too strongly concentrated or too few instruments are assigned weight. (performance is -161)

    ["group_rank(implied_volatility_call_120/parkinson_volatility_120, sector)", 1.80, 1.17, 21.46, ❌ FAIL] because of Weight is too strongly concentrated or too few instruments are assigned weight.

    ["ts_rank(implied_volatility_call_120/parkinson_volatility_120, 20)", 0.86, 0.26, 44.46, ❌ FAIL] because of Sharpe of 0.86 is below cutoff of 1.25. Fitness of 0.26 is below cutoff of 1. Weight concentration 12.12% is above cutoff of 10% on 1/25/2022.

    ["0.6*rank(implied_volatility_call_120/parkinson_volatility_120)+0.4*rank(mdl177_garpanalystmodel_qgp_relgrowth)", 2.06, 1.67, 19.29, ❌ FAIL] #GOOD because of Weight concentration 10.22% is above cutoff of 10% on 1/25/2022.

    ["rank(implied_volatility_call_120 - implied_volatility_put_120)", 1.91, 0.81, 44.22, ❌ FAIL] because of Fitness of 0.81 is below cutoff of 1. Weight concentration 15.80% is above cutoff of 10% on 1/25/2022. Sub-universe Sharpe of 0.55 is below cutoff of 0.83.

    ["rank(ts_delta(retained_earnings/sharesout, 64))", 0.37, 0.17, 6.56, ❌ FAIL] because of Sharpe of 0.37 is below cutoff of 1.25. Fitness of 0.17 is below cutoff of 1.

    ["ts_rank(fnd6_fopo/debt_lt, 345)", 0.86, 0.33, 3.41, ❌ FAIL] because of Sharpe of 0.86 is below cutoff of 1.25. Fitness of 0.33 is below cutoff of 1. Sub-universe Sharpe of 0.27 is below cutoff of 0.37.

    ["0.4*rank(implied_volatility_call_120/parkinson_volatility_120)+0.4*rank(mdl177_garpanalystmodel_qgp_relgrowth)+0.2*multiply(rank(-returns),rank(volume/adv20),filter=true)", 2.47, 2.00, 22.86, ❌ FAIL] because of Weight is too strongly concentrated or too few instruments are assigned weight.

    ["0.5*rank(0.5*ts_mean(news_mins_10_pct_dn,10)+0.5*ts_mean(news_mins_10_pct_dn,40))+0.5*rank(implied_volatility_call_120/parkinson_volatility_120)", 1.61, 1.28, 44.64, ❌ FAIL] because of Weight is too strongly concentrated or too few instruments are assigned weight.

    ["decay_days = 2; rel_days_since_max = rank(ts_arg_max(close,30));decline_pct = (vwap - close) / vwap;decline_pct / min(ts_decay_linear(rel_days_since_max, decay_days), 0.01)", 1.74, 0.86, 81.49, ❌ FAIL] because of Fitness of 0.86 is below cutoff of 1. Turnover of 81.49% is above cutoff of 70%.

    ["rank(historical_volatility_20 / historical_volatility_120)", 0.73, 0.31, 18.96, ❌ FAIL] because of Sharpe of 0.73 is below cutoff of 1.25. Fitness of 0.31 is below cutoff of 1. Weight is too strongly concentrated or too few instruments are assigned weight.


]

[
    ["0.3*rank(ts_mean(announcement_effect_10,20))+0.7*rank(rel_num_all)", 1.14, 1.05, 1.84, ❌ FAIL], because of Sharpe of 1.14 is below cutoff of 1.25. (performance is -187)

    ["rank(implied_volatility_call_180/parkinson_volatility_180)*rank(-returns)", 2.70, 1.56, 50.33, ❌ FAIL], because of Weight is too strongly concentrated or too few instruments are assigned weight. (performance is -379)

    ["0.3*rank(ts_mean(announcement_effect_10,20))+0.7*rank(rel_num_part)", 1.17, 1.00, 1.71, ❌ FAIL], because of Sharpe of 1.17 is below cutoff of 1.25. Sub-universe Sharpe of 0.38 is below cutoff of 0.51.
    ["0.7*rank(implied_volatility_call_180/parkinson_volatility_180)+0.3*rank(volume)", 2.19, 1.52, 20.31 , ❌ FAIL], because of Weight is too strongly concentrated or too few instruments are assigned weight.
]

[
    [❌ FAIL | rank(zscore(implied_volatility_call_120/parkinson_volatility_120)) Sharpe: 1.93 | Fitness: 0.89 | Turnover: 45.3% ]
    [❌ FAIL | rank(zscore(ts_backfill(implied_volatility_call_120/parkinson_volatility_120, 5))) Sharpe: 1.83 | Fitness: 0.84 | Turnover: 41.8% ]
    [❌ FAIL | rank(implied_volatility_call_30 - implied_volatility_call_270) Sharpe: 0.32 | Fitness: 0.05 | Turnover: 72.0% ]
    [❌ FAIL | rank(implied_volatility_mean_10 - implied_volatility_mean_120) Sharpe: 0.26 | Fitness: 0.04 | Turnover: 71.1% ]
    [❌ FAIL | -rank(ts_delta(parkinson_volatility_120, 20)) Sharpe: -0.71 | Fitness: -0.39 | Turnover: 20.6%]
]

[

    ✅ PASS | rank(ts_mean(zscore(implied_volatility_call_120/parkinson_volatility_120),20))
    Sharpe: 1.46 | Fitness: 1.13 | Turnover: 5.5% | PnL: 📈 +$3.68M (performance is -6)

    ❌ FAIL | group_rank(zscore(implied_volatility_call_120/parkinson_volatility_120),industry)
    Sharpe: 1.99 | Fitness: 0.88 | Turnover: 46.6% | PnL: 📈 +$4.52M

    ✅ PASS | group_rank(ts_mean(zscore(implied_volatility_call_120/parkinson_volatility_120),20),industry)
    Sharpe: 1.45 | Fitness: 1.07 | Turnover: 7.0% | PnL: 📈 +$3.37M (performance is -16)


    ❌ FAIL | rank(zscore(implied_volatility_call_120/parkinson_volatility_120))*rank(rel_num_part)
    Sharpe: 1.69 | Fitness: 0.93 | Turnover: 34.4% | PnL: 📈 +$5.19M

    ❌ FAIL | 0.5*rank(zscore(implied_volatility_call_120/parkinson_volatility_120))+0.5*rank(rel_num_part)
    Sharpe: 1.79 | Fitness: 1.03 | Turnover: 34.3% | PnL: 📈 +$5.65M because of Weight concentration 11.41% is above cutoff of 10% on 1/25/2022.

    ❌ FAIL | 0.3*rank(rel_num_part)+0.7*rank(zscore(implied_volatility_call_120/parkinson_volatility_120))
   Sharpe: 1.91 | Fitness: 0.98 | Turnover: 42.1% | PnL: 📈 +$5.52M

    ✅ PASS | 0.3*rank(rel_num_all)+0.7*rank(zscore(implied_volatility_call_120/parkinson_volatility_120))
    Sharpe: 1.91 | Fitness: 1.01 | Turnover: 42.8% | PnL: 📈 +$5.93M failed because of Weight concentration 11.47% is above cutoff of 10% on 1/25/2022.

    ✅ PASS | 0.5*rank(rel_num_part)+0.5*rank(zscore(implied_volatility_call_120/parkinson_volatility_120))
    Sharpe: 1.79 | Fitness: 1.03 | Turnover: 34.3% | PnL: 📈 +$5.65M failed because of Weight concentration 11.41% is above cutoff of 10% on 1/25/2022.

    ❌ FAIL | rank(rel_num_part)*rank(zscore(implied_volatility_call_120/parkinson_volatility_120))
    Sharpe: 1.69 | Fitness: 0.93 | Turnover: 34.4% | PnL: 📈 +$5.19M

    ❌ FAIL | rank(rel_num_all)*rank(zscore(implied_volatility_call_120/parkinson_volatility_120))
    Sharpe: 1.66 | Fitness: 0.91 | Turnover: 37.5% | PnL: 📈 +$5.54M

    []

    ✅ PASS | rank(ts_mean(zscore(implied_volatility_call_120/parkinson_volatility_120),10))
    Sharpe: 1.43 | Fitness: 1.09 | Turnover: 8.5% | PnL: 📈 +$3.59M (performace is -45 )

    ✅ PASS | rank(ts_mean(zscore(implied_volatility_call_120/parkinson_volatility_120),20))
    Sharpe: 1.46 | Fitness: 1.13 | Turnover: 5.5% | PnL: 📈 +$3.68M ❌ FAIL


    ✅ PASS | rank(ts_decay_linear(zscore(implied_volatility_call_120/parkinson_volatility_120),10))
    Sharpe: 1.66 | Fitness: 1.27 | Turnover: 14.6% | PnL: 📈 +$4.24M failed because of Weight is too strongly concentrated or too few instruments are assigned weight.

    ✅ PASS | rank(ts_decay_linear(zscore(implied_volatility_call_120/parkinson_volatility_120),20))
    Sharpe: 1.62 | Fitness: 1.33 | Turnover: 12.0% | PnL: 📈 +$4.16M failed becasue of Weight concentration 11.55% is above cutoff of 10% on 1/25/2022.

    ❌ FAIL | group_rank(zscore(implied_volatility_call_120/parkinson_volatility_120),industry)
    Sharpe: 1.99 | Fitness: 0.88 | Turnover: 46.6% | PnL: 📈 +$4.52M

    ⚠️  Score fetch failed: Expecting value: line 1 column 1 (char 0)
    ✅ PASS | group_rank(ts_mean(zscore(implied_volatility_call_120/parkinson_volatility_120),10),industry)
    Sharpe: 1.46 | Fitness: 1.08 | Turnover: 10.1% | PnL: 📈 +$3.38M (performance is -57)

    ❌ FAIL | rank(zscore(implied_volatility_call_120/parkinson_volatility_120))*rank(rel_num_part)
    Sharpe: 1.69 | Fitness: 0.93 | Turnover: 34.4% | PnL: 📈 +$5.19M

    ❌ FAIL | rank(zscore(implied_volatility_call_120/parkinson_volatility_120))*rank(rel_num_all)
    Sharpe: 1.66 | Fitness: 0.91 | Turnover: 37.5% | PnL: 📈 +$5.54M

    ✅ PASS | 0.5*rank(zscore(implied_volatility_call_120/parkinson_volatility_120))+0.5*rank(rel_num_part)
    Sharpe: 1.79 | Fitness: 1.03 | Turnover: 34.3% | PnL: 📈 +$5.65M failed because of Weight concentration 11.41% is above cutoff of 10% on 1/25/2022.


    ❌ FAIL | rank(zscore(implied_volatility_call_90/parkinson_volatility_120))
   Sharpe: 1.96 | Fitness: 0.88 | Turnover: 48.1% | PnL: 📈 +$4.76M

    ❌ FAIL | rank(zscore(implied_volatility_call_60/parkinson_volatility_120))
    Sharpe: 1.96 | Fitness: 0.81 | Turnover: 53.0% | PnL: 📈 +$4.51M

    ❌ FAIL | rank(zscore(implied_volatility_call_180/parkinson_volatility_120))
    Sharpe: 1.96 | Fitness: 0.95 | Turnover: 43.3% | PnL: 📈 +$5.00M

    ❌ FAIL | rank(zscore(implied_volatility_mean_120/parkinson_volatility_120))
    Sharpe: 1.42 | Fitness: 0.63 | Turnover: 38.4% | PnL: 📈 +$3.70M

    ❌ FAIL | rank(zscore(implied_volatility_put_120/parkinson_volatility_120))
    Sharpe: 0.89 | Fitness: 0.29 | Turnover: 43.4% | PnL: 📈 +$2.21M

    ❌ FAIL | group_rank(zscore(implied_volatility_call_90/parkinson_volatility_120),industry)
    Sharpe: 2.06 | Fitness: 0.91 | Turnover: 49.1% | PnL: 📈 +$4.73M

    ❌ FAIL | group_rank(zscore(implied_volatility_call_60/parkinson_volatility_120),industry)
    Sharpe: 2.04 | Fitness: 0.84 | Turnover: 53.7% | PnL: 📈 +$4.51M

    ❌ FAIL | group_rank(zscore(implied_volatility_call_180/parkinson_volatility_120),industry)
    Sharpe: 2.00 | Fitness: 0.92 | Turnover: 44.7% | PnL: 📈 +$4.71M

    ✅ PASS | rank(ts_mean(zscore(implied_volatility_call_90/parkinson_volatility_120),20))
    Sharpe: 1.41 | Fitness: 1.05 | Turnover: 5.9% | PnL: 📈 +$3.44M (performance is +7)

    ✅ PASS | rank(ts_mean(zscore(implied_volatility_call_180/parkinson_volatility_120),20))
    Sharpe: 1.52 | Fitness: 1.22 | Turnover: 5.3% | PnL: 📈 +$3.95M (performance is -15) 

]



[
    ❌ FAIL | rank(0.5*ts_mean(zscore(implied_volatility_call_120/parkinson_volatility_120),10)+0.5*ts_mean(zscore(implied_volatility_call_120/parkinson_volatility_120),40)) Sharpe: 1.33 | Fitness: 0.99 | Turnover: 5.8% | PnL: 📈 +$3.41M failed because of Fitness of 0.99 is below cutoff of 1.

    ✅ PASS | rank(0.5*ts_mean(zscore(implied_volatility_call_180/parkinson_volatility_120),10)+0.5*ts_mean(zscore(implied_volatility_call_180/parkinson_volatility_120),40)) Sharpe: 1.40 | Fitness: 1.08 | Turnover: 5.6% | PnL: 📈 +$3.71M (performance is -20)

    ❌ FAIL | rank(0.5*ts_mean(zscore(implied_volatility_call_90/parkinson_volatility_120),10)+0.5*ts_mean(zscore(implied_volatility_call_90/parkinson_volatility_120),40))
    Sharpe: 1.29 | Fitness: 0.93 | Turnover: 6.2% | PnL: 📈 +$3.19M failed because of Fitness of 0.93 is below cutoff of 1.

    ❌ FAIL | rank(0.4*ts_mean(zscore(implied_volatility_call_120/parkinson_volatility_120),10)+0.6*ts_mean(zscore(implied_volatility_call_120/parkinson_volatility_120),60)) Sharpe: 1.27 | Fitness: 0.92 | Turnover: 5.1% | PnL: 📈 +$3.24M failde because of Fitness of 0.92 is below cutoff of 1.

    ❌ FAIL | rank(0.3*ts_mean(zscore(implied_volatility_call_120/parkinson_volatility_120),20)+0.7*ts_mean(zscore(implied_volatility_call_120/parkinson_volatility_120),80)) Sharpe: 1.23 | Fitness: 0.87 | Turnover: 3.4% | PnL: 📈 +$3.13M

    ✅ PASS | 0.3*rank(rel_num_all)+0.7*rank(ts_decay_linear(zscore(implied_volatility_call_120/parkinson_volatility_120),20)) Sharpe: 1.67 | Fitness: 1.54 | Turnover: 11.5% | PnL: 📈 +$5.28M failed because of Weight concentration 11.25% is above cutoff of 10% on 1/25/2022.

    ✅ PASS | 0.4*rank(rel_num_all)+0.6*rank(ts_decay_linear(zscore(implied_volatility_call_120/parkinson_volatility_120),20)) Sharpe: 1.64 | Fitness: 1.56 | Turnover: 11.0% | PnL: 📈 +$5.61M failed because of Weight concentration 10.53% is above cutoff of 10% on 1/25/2022.

    ✅ PASS | group_rank(ts_decay_linear(zscore(implied_volatility_call_120/parkinson_volatility_120),20),industry) Sharpe: 1.62 | Fitness: 1.22 | Turnover: 13.5% | PnL: 📈 +$3.81M

    ❌ FAIL | rank(0.5*ts_mean(zscore(implied_volatility_call_120/parkinson_volatility_120),10)+0.5*ts_mean(zscore(implied_volatility_call_120/parkinson_volatility_120),40)) Sharpe: 1.33 | Fitness: 0.99 | Turnover: 5.8% | PnL: 📈 +$3.41M failed because of Fitness of 0.99 is below cutoff of 1.

    ✅ PASS | 0.2*rank(rel_num_all)+0.8*rank(ts_decay_linear(zscore(implied_volatility_call_120/parkinson_volatility_120),20)) Sharpe: 1.67 | Fitness: 1.49 | Turnover: 11.8% | PnL: 📈 +$4.91M failed because of Weight concentration 12.43% is above cutoff of 10% on 1/25/2022.

    []


    ✅ PASS | 0.2*rank(rel_num_all)+0.8*rank(ts_decay_linear(zscore(implied_volatility_call_120/parkinson_volatility_120),20)) ❌ FAIL
    Sharpe: 1.67 | Fitness: 1.49 | Turnover: 11.8% | PnL: 📈 +$4.91M failded because of Weight concentration 12.43% is above cutoff of 10% on 1/25/2022.

    ✅ PASS | 0.3*rank(rel_num_all)+0.7*rank(ts_decay_linear(zscore(implied_volatility_call_120/parkinson_volatility_120),20)) ❌ FAIL
    Sharpe: 1.67 | Fitness: 1.54 | Turnover: 11.5% | PnL: 📈 +$5.28M

    ✅ PASS | 0.4*rank(rel_num_all)+0.6*rank(ts_decay_linear(zscore(implied_volatility_call_120/parkinson_volatility_120),20)) ❌ FAIL
    Sharpe: 1.64 | Fitness: 1.56 | Turnover: 11.0% | PnL: 📈 +$5.61M

    ✅ PASS | 0.2*rank(rel_num_part)+0.8*rank(ts_decay_linear(zscore(implied_volatility_call_120/parkinson_volatility_120),20)) ❌ FAIL
    Sharpe: 1.67 | Fitness: 1.46 | Turnover: 11.7% | PnL: 📈 +$4.74M failed because of Weight concentration 11.31% is above cutoff of 10% on 1/25/2022.

    ✅ PASS | 0.3*rank(rel_num_part)+0.7*rank(ts_decay_linear(zscore(implied_volatility_call_120/parkinson_volatility_120),20)) ❌ FAIL
    Sharpe: 1.67 | Fitness: 1.50 | Turnover: 11.4% | PnL: 📈 +$5.01M failed because of Weight concentration 11.44% is above cutoff of 10% on 1/25/2022.

[]


    ✅ PASS | group_rank(ts_decay_linear(zscore(implied_volatility_call_120/parkinson_volatility_120),20),industry) ❌ FAIL
    Sharpe: 1.62 | Fitness: 1.22 | Turnover: 13.5% | PnL: 📈 +$3.81M failed becaues of Weight concentration 11.41% is above cutoff of 10% on 1/25/2022.

    ✅ PASS | group_rank(ts_decay_linear(zscore(implied_volatility_call_120/parkinson_volatility_120),30),industry) ❌ FAIL
    Sharpe: 1.57 | Fitness: 1.22 | Turnover: 12.5% | PnL: 📈 +$3.70M failed because of Weight concentration 11.40% is above cutoff of 10% on 1/25/2022.

    ✅ PASS | group_rank(ts_decay_linear(zscore(implied_volatility_call_180/parkinson_volatility_120),20),industry) ❌ FAIL
    Sharpe: 1.65 | Fitness: 1.30 | Turnover: 13.2% | PnL: 📈 +$4.01M failed because of Weight is too strongly concentrated or too few instruments are assigned weight.


    ✅ PASS | group_rank(ts_mean(zscore(implied_volatility_call_180/parkinson_volatility_120),20),industry) ❌ FAIL
    Sharpe: 1.50 | Fitness: 1.14 | Turnover: 6.7% | PnL: 📈 +$3.57M (performance is -14)



]

[
    ✅ PASS | group_neutralize(rank(ts_decay_linear(zscore(implied_volatility_call_120/parkinson_volatility_120),20)),industry)
   Sharpe: 1.62 | Fitness: 1.33 | Turnover: 12.0% | PnL: 📈 +$4.16M ❌ FAIL

    ✅ PASS | group_neutralize(rank(ts_decay_linear(zscore(implied_volatility_call_180/parkinson_volatility_120),20)),industry)
    Sharpe: 1.62 | Fitness: 1.35 | Turnover: 11.6% | PnL: 📈 +$4.28M ❌ FAIL

    ✅ PASS | group_neutralize(rank(ts_mean(zscore(implied_volatility_call_120/parkinson_volatility_120),20)),industry)
    Sharpe: 1.46 | Fitness: 1.13 | Turnover: 5.5% | PnL: 📈 +$3.68M ❌ FAIL

    ✅ PASS | group_neutralize(rank(ts_mean(zscore(implied_volatility_call_180/parkinson_volatility_120),20)),industry)
    Sharpe: 1.52 | Fitness: 1.22 | Turnover: 5.3% | PnL: 📈 +$3.95M ❌ FAIL

    ❌ FAIL | group_neutralize(rank(zscore(implied_volatility_call_120/parkinson_volatility_120)),industry)
    Sharpe: 1.93 | Fitness: 0.89 | Turnover: 45.3% | PnL: 📈 +$4.74M ❌ FAIL

    ✅ PASS | 0.5*group_rank(ts_decay_linear(zscore(implied_volatility_call_120/parkinson_volatility_120),20),industry)+0.5*rank(rel_num_all)
    Sharpe: 1.60 | Fitness: 1.51 | Turnover: 12.0% | PnL: 📈 +$5.48M ❌ FAIL

    ✅ PASS | 0.5*group_rank(ts_decay_linear(zscore(implied_volatility_call_180/parkinson_volatility_120),20),industry)+0.5*rank(rel_num_all)
    Sharpe: 1.58 | Fitness: 1.49 | Turnover: 11.7% | PnL: 📈 +$5.53M ❌ FAIL

    ✅ PASS | 0.5*group_rank(ts_decay_linear(zscore(implied_volatility_call_120/parkinson_volatility_120),20),industry)+0.5*rank(rel_num_part)
    Sharpe: 1.62 | Fitness: 1.45 | Turnover: 11.6% | PnL: 📈 +$4.98M ❌ FAIL

    ✅ PASS | 0.4*group_rank(ts_decay_linear(zscore(implied_volatility_call_120/parkinson_volatility_120),20),industry)+0.6*rank(rel_num_all)
    Sharpe: 1.53 | Fitness: 1.46 | Turnover: 11.0% | PnL: 📈 +$5.65M ❌ FAIL

    ✅ PASS | 0.6*group_rank(ts_decay_linear(zscore(implied_volatility_call_120/parkinson_volatility_120),20),industry)+0.4*rank(rel_num_all)
    Sharpe: 1.64 | Fitness: 1.48 | Turnover: 12.7% | PnL: 📈 +$5.14M ❌ FAIL

    []

    ✅ PASS | group_rank(ts_decay_linear(zscore(implied_volatility_call_120/parkinson_volatility_120),20),subindustry)
    Sharpe: 1.65 | Fitness: 1.19 | Turnover: 14.0% | PnL: 📈 +$3.62M ❌ FAIL

    ✅ PASS | group_rank(ts_decay_linear(zscore(implied_volatility_call_180/parkinson_volatility_120),20),subindustry)
    Sharpe: 1.66 | Fitness: 1.24 | Turnover: 13.6% | PnL: 📈 +$3.73M ❌ FAIL

    ✅ PASS | group_rank(ts_mean(zscore(implied_volatility_call_120/parkinson_volatility_120),20),subindustry)
    Sharpe: 1.50 | Fitness: 1.08 | Turnover: 6.9% | PnL: 📈 +$3.21M ❌ FAIL

    ✅ PASS | group_rank(ts_mean(zscore(implied_volatility_call_180/parkinson_volatility_120),20),subindustry)
    Sharpe: 1.53 | Fitness: 1.13 | Turnover: 6.6% | PnL: 📈 +$3.36M ❌ FAIL

    ✅ PASS | group_rank(rank(ts_decay_linear(zscore(implied_volatility_call_120/parkinson_volatility_120),20)),subindustry)
    Sharpe: 1.65 | Fitness: 1.19 | Turnover: 14.0% | PnL: 📈 +$3.62M ❌ FAIL

    []

    ✅ PASS | 0.45*rank(rel_num_all)+0.55*rank(ts_decay_linear(zscore(implied_volatility_call_120/parkinson_volatility_120),20))
    Sharpe: 1.61 | Fitness: 1.55 | Turnover: 10.7% | PnL: 📈 +$5.72M ❌ FAIL

    ✅ PASS | 0.48*rank(rel_num_all)+0.52*rank(ts_decay_linear(zscore(implied_volatility_call_120/parkinson_volatility_120),20))
    Sharpe: 1.59 | Fitness: 1.54 | Turnover: 10.5% | PnL: 📈 +$5.78M ❌ FAIL

    ✅ PASS | 0.42*rank(rel_num_all)+0.58*rank(ts_decay_linear(zscore(implied_volatility_call_120/parkinson_volatility_120),20))
    Sharpe: 1.63 | Fitness: 1.56 | Turnover: 10.9% | PnL: 📈 +$5.66M ❌ FAIL

    ✅ PASS | 0.45*rank(rel_num_part)+0.55*rank(ts_decay_linear(zscore(implied_volatility_call_120/parkinson_volatility_120),20))
    Sharpe: 1.63 | Fitness: 1.50 | Turnover: 10.4% | PnL: 📈 +$5.22M ❌ FAIL

    ✅ PASS | 0.48*rank(rel_num_part)+0.52*rank(ts_decay_linear(zscore(implied_volatility_call_120/parkinson_volatility_120),20))
    Sharpe: 1.62 | Fitness: 1.49 | Turnover: 10.1% | PnL: 📈 +$5.22M ❌ FAIL

]

New Set

[
    [Delay 1]#0
    ❌ FAIL | rank(opt6_10dorhv / opt6_1000dorhv)
   Sharpe: 0.15 | Fitness: 0.04 | Turnover: 16.5% | PnL: 📈 +$589.4K
   Score: Before=None → After=None | Change: 🔴 N/A

    ❌ FAIL | -rank(opt6_derivinf)
    Sharpe: -0.84 | Fitness: -0.24 | Turnover: 34.7% | PnL: 📉 -$1.44M
    Score: Before=None → After=None | Change: 🔴 N/A

    ❌ FAIL | rank(opt6_ioc)
    Sharpe: 0.24 | Fitness: 0.09 | Turnover: 3.5% | PnL: 📈 +$896.7K
    Score: Before=None → After=None | Change: 🔴 N/A

    ❌ FAIL | rank(opt6_stkvolu / opt6_optvolu20davg)
    Sharpe: -0.16 | Fitness: -0.04 | Turnover: 7.3% | PnL: 📉 -$415.6K
    Score: Before=None → After=None | Change: 🔴 N/A

    ❌ FAIL | rank(opt6_ivhvxernratio)
    Sharpe: 0.06 | Fitness: 0.01 | Turnover: 25.1% | PnL: 📈 +$127.5K
    Score: Before=None → After=None | Change: 🔴 N/A

    ❌ FAIL | -rank(opt6_slopeavg1y - opt6_slopeavg1m)
    Sharpe: -0.14 | Fitness: -0.03 | Turnover: 8.5% | PnL: 📉 -$235.5K
    Score: Before=None → After=None | Change: 🔴 N/A

    ❌ FAIL | -rank(opt6_beta1m)
   Sharpe: -0.08 | Fitness: -0.02 | Turnover: 19.3% | PnL: 📉 -$769.9K
   Score: Before=None → After=None | Change: 🔴 N/A

   ❌ FAIL | rank(ts_mean(opt6_vimta3m, 10))
   Sharpe: -0.05 | Fitness: -0.01 | Turnover: 3.7% | PnL: 📉 -$523.3K
   Score: Before=None → After=None | Change: 🔴 N/A

    ❌ FAIL | rank(opt6_ivpctile1y)
    Sharpe: 0.13 | Fitness: 0.02 | Turnover: 29.1% | PnL: 📈 +$399.8K
    Score: Before=None → After=None | Change: 🔴 N/A

    ❌ FAIL | rank(opt6_or20divfcst - opt6_or20divxern)
    Sharpe: -0.20 | Fitness: -0.03 | Turnover: 46.7% | PnL: 📉 -$610.5K
    Score: Before=None → After=None | Change: 🔴 N/A

    ❌ FAIL | rank(opt6_2rtscf)
    Sharpe: 1.10 | Fitness: 0.86 | Turnover: 2.7% | PnL: 📈 +$3.80M
    Score: Before=None → After=None | Change: 🔴 N/A

    ✅ PASS | 0.5*rank(opt6_slopeavg1y) + 0.5*rank(0.5*ts_mean(news_mins_10_pct_dn,10) + 0.5*ts_mean(news_mins_10_pct_dn,40))
    Sharpe: 1.38 | Fitness: 1.09 | Turnover: 38.2% | PnL: 📈 +$11.80M ❌ FAIL because of Weight is too strongly concentrated or too few instruments are assigned weight.
    Score: Before=None → After=None | Change: 🔴 N/A 

    ❌ FAIL | 0.6*rank(opt6_ivpctile1m) + 0.4*rank(mdl177_garpanalystmodel_qgp_relgrowth)
    Sharpe: 1.39 | Fitness: 0.61 | Turnover: 37.4% | PnL: 📈 +$3.60M
    Score: Before=None → After=None | Change: 🔴 N/A

    ❌ FAIL | 0.4*rank(opt6_slopeavg1y) + 0.4*rank(opt6_ivpctile1m) + 0.2*rank(opt6_derivinf)
    Sharpe: 0.87 | Fitness: 0.41 | Turnover: 29.4% | PnL: 📈 +$3.25M
    Score: Before=None → After=None | Change: 🔴 N/A

    ❌ FAIL | 0.3*rank(opt6_ivpctile1m) + 0.4*rank(mdl177_garpanalystmodel_qgp_relgrowth) + 0.3*rank(0.5*ts_mean(news_mins_10_pct_dn,10)+0.5*ts_mean(news_mins_10_pct_dn,40))
    Sharpe: 1.15 | Fitness: 0.77 | Turnover: 47.0% | PnL: 📈 +$10.39M
    Score: Before=None → After=None | Change: 🔴 N/A

    [] #1

❌ FAIL | rank(opt6_divyield)
   Sharpe: 0.25 | Fitness: 0.13 | Turnover: 3.0% | PnL: 📈 +$1.60M
   Score: Before=None → After=None | Change: 🔴 N/A

❌ FAIL | rank(opt6_slopepctile)
   Sharpe: 0.06 | Fitness: 0.00 | Turnover: 80.2% | PnL: 📈 +$117.7K
   Score: Before=None → After=None | Change: 🔴 N/A

❌ FAIL | rank(opt6_etfivhvxernratio)
   Sharpe: 0.17 | Fitness: 0.02 | Turnover: 48.2% | PnL: 📈 +$456.8K
   Score: Before=None → After=None | Change: 🔴 N/A

❌ FAIL | -rank(opt6_volofivol)
   Sharpe: 0.12 | Fitness: 0.03 | Turnover: 3.6% | PnL: 📈 +$296.0K
   Score: Before=None → After=None | Change: 🔴 N/A

❌ FAIL | -rank(opt6_poi)
   Sharpe: -0.11 | Fitness: -0.03 | Turnover: 4.4% | PnL: 📉 -$460.3K
   Score: Before=None → After=None | Change: 🔴 N/A

❌ FAIL | rank(opt6_cvolu / (opt6_pvolu + 0.001))
   Sharpe: -0.24 | Fitness: -0.02 | Turnover: 94.7% | PnL: 📉 -$505.7K
   Score: Before=None → After=None | Change: 🔴 N/A

❌ FAIL | rank(ts_mean(opt6_vimta3m, 20))
   Sharpe: -0.04 | Fitness: -0.01 | Turnover: 2.4% | PnL: 📉 -$460.3K
   Score: Before=None → After=None | Change: 🔴 N/A


-------------------
   [Delay =0 ] #2

    ❌ FAIL | (close - open) / (high - low + 0.001)
    Sharpe: 0.04 | Fitness: 0.00 | Turnover: 136.0% | PnL: 📈 +$225.0K
    Score: Before=None → After=None | Change: 🔴 N/A

    ❌ FAIL | rank(vwap - close) / rank(vwap + close)
    Sharpe: 0.45 | Fitness: 0.30 | Turnover: 32.5% | PnL: 📈 +$7.24M
    Score: Before=None → After=None | Change: 🔴 N/A

    ❌ FAIL | sign(delta(volume,1)) * (-1 * delta(close,1))
    Sharpe: 0.00 | Fitness: 0.00 | Turnover: 0.0% | PnL: 📉 $0
    Score: Before=None → After=None | Change: 🔴 N/A

    ❌ FAIL | rank(((high + low)/2 - close) / (high - low + 0.001))
    Sharpe: 0.45 | Fitness: 0.09 | Turnover: 132.2% | PnL: 📈 +$2.48M
    Score: Before=None → After=None | Change: 🔴 N/A

    ❌ FAIL | ts_rank(-returns, 5) * ts_rank(volume/adv20, 5)
    Sharpe: -0.28 | Fitness: -0.04 | Turnover: 129.4% | PnL: 📉 -$1.24M
    Score: Before=None → After=None | Change: 🔴 N/A

    ❌ FAIL | -rank(ts_corr(vwap, ts_delay(close,1), 5))
    Sharpe: -0.34 | Fitness: -0.07 | Turnover: 75.0% | PnL: 📉 -$1.53M
    Score: Before=None → After=None | Change: 🔴 N/A

    ❌ FAIL | rank((close - ts_min(close,12)) / (ts_max(close,12) - ts_min(close,12) + 0.001))
    Sharpe: 0.00 | Fitness: 0.00 | Turnover: 0.0% | PnL: 📉 $0
    Score: Before=None → After=None | Change: 🔴 N/A

    ❌ FAIL | rank(opt6_ivpctile1m)
    Sharpe: 0.94 | Fitness: 0.24 | Turnover: 85.2% | PnL: 📈 +$2.75M
    Score: Before=None → After=None | Change: 🔴 N/A

    ❌ FAIL | -rank(opt6_ivspyratio)
   Sharpe: 0.01 | Fitness: 0.00 | Turnover: 23.2% | PnL: 📈 +$113.5K
   Score: Before=None → After=None | Change: 🔴 N/A

    ❌ FAIL | rank(opt6_slopeavg1y)
    Sharpe: 0.65 | Fitness: 0.54 | Turnover: 2.0% | PnL: 📈 +$4.21M
    Score: Before=None → After=None | Change: 🔴 N/A

    ❌ FAIL | 0.6*rank(opt6_ivpctile1m) + 0.4*(-rank(ts_delta(close,1)))
    Sharpe: 0.79 | Fitness: 0.21 | Turnover: 105.6% | PnL: 📈 +$3.54M
    Score: Before=None → After=None | Change: 🔴 N/A

    ❌ FAIL | 0.5*rank(opt6_slopeavg1y) + 0.5*rank(vwap - close)
    Sharpe: 0.85 | Fitness: 0.27 | Turnover: 96.3% | PnL: 📈 +$4.69M
    Score: Before=None → After=None | Change: 🔴 N/A

    ❌ FAIL | 0.4*rank(opt6_ivpctile1m) + 0.3*ts_rank(-returns,5) * ts_rank(volume/adv20,5) + 0.3*rank(((high+low)/2 - close)/(high-low+0.001))
    Sharpe: 0.62 | Fitness: 0.14 | Turnover: 121.7% | PnL: 📈 +$3.04M
    Score: Before=None → After=None | Change: 🔴 N/A

]

[
    Delay 0 #0
❌ FAIL | rank(ts_decay_linear(opt6_slopeavg1y, 5))
   Sharpe: 0.65 | Fitness: 0.54 | Turnover: 1.7% | PnL: 📈 +$4.20M
   Score: Before=None → After=None | Change: 🔴 N/A

❌ FAIL | rank(ts_decay_linear(opt6_slopeavg1y, 10))
   Sharpe: 0.65 | Fitness: 0.54 | Turnover: 1.6% | PnL: 📈 +$4.20M
   Score: Before=None → After=None | Change: 🔴 N/A

❌ FAIL | rank(ts_decay_linear(opt6_ivpctile1m, 10))
   Sharpe: 0.39 | Fitness: 0.15 | Turnover: 18.0% | PnL: 📈 +$1.40M
   Score: Before=None → After=None | Change: 🔴 N/A

❌ FAIL | rank(ts_decay_linear(opt6_ivpctile1m, 20))
   Sharpe: 0.54 | Fitness: 0.29 | Turnover: 13.7% | PnL: 📈 +$1.91M
   Score: Before=None → After=None | Change: 🔴 N/A

❌ FAIL | rank(ts_decay_linear(vwap - close, 5))
   Sharpe: 0.80 | Fitness: 0.36 | Turnover: 41.2% | PnL: 📈 +$4.09M
   Score: Before=None → After=None | Change: 🔴 N/A

❌ FAIL | rank(ts_decay_linear(opt6_2rtscf, 5))
   Sharpe: 0.81 | Fitness: 0.80 | Turnover: 2.1% | PnL: 📈 +$5.99M
   Score: Before=None → After=None | Change: 🔴 N/A

❌ FAIL | rank(ts_decay_linear(opt6_2rtscf, 10))
   Sharpe: 0.82 | Fitness: 0.81 | Turnover: 2.0% | PnL: 📈 +$6.00M
   Score: Before=None → After=None | Change: 🔴 N/A

❌ FAIL | 0.5*rank(ts_decay_linear(opt6_slopeavg1y,5)) + 0.5*rank(ts_decay_linear(opt6_ivpctile1m,10))
   Sharpe: 0.83 | Fitness: 0.66 | Turnover: 14.0% | PnL: 📈 +$4.33M
   Score: Before=None → After=None | Change: 🔴 N/A

❌ FAIL | rank(ts_decay_linear(opt6_absavgernmv, 10))
   Sharpe: 0.27 | Fitness: 0.15 | Turnover: 1.6% | PnL: 📈 +$1.93M
   Score: Before=None → After=None | Change: 🔴 N/A

❌ FAIL | 0.6*rank(ts_decay_linear(opt6_slopeavg1y,5)) + 0.4*rank(ts_decay_linear(opt6_2rtscf,5))
   Sharpe: 0.78 | Fitness: 0.77 | Turnover: 1.9% | PnL: 📈 +$6.02M
   Score: Before=None → After=None | Change: 🔴 N/A

❌ FAIL | 0.7*rank(ts_decay_linear(opt6_slopeavg1y,5)) + 0.3*rank(ts_decay_linear(close/vwap,5))
   Sharpe: 0.34 | Fitness: 0.20 | Turnover: 13.1% | PnL: 📈 +$2.34M
   Score: Before=None → After=None | Change: 🔴 N/A

❌ FAIL | rank(ts_decay_linear(opt6_vimta3m, 10))
   Sharpe: -0.01 | Fitness: -0.00 | Turnover: 3.4% | PnL: 📉 -$66.7K
   Score: Before=None → After=None | Change: 🔴 N/A

❌ FAIL | -rank(ts_decay_linear(opt6_volofivol, 5))
   Sharpe: 0.27 | Fitness: 0.11 | Turnover: 2.6% | PnL: 📈 +$967.2K
   Score: Before=None → After=None | Change: 🔴 N/A


    Delay 1 #1

❌ FAIL | rank(opt6_2rtscf)
   Sharpe: 0.68 | Fitness: 0.54 | Turnover: 2.9% | PnL: 📈 +$3.84M
   Score: Before=None → After=None | Change: 🔴 N/A

❌ FAIL | rank(ts_mean(opt6_2rtscf, 10))
   Sharpe: 0.62 | Fitness: 0.46 | Turnover: 1.8% | PnL: 📈 +$3.47M
   Score: Before=None → After=None | Change: 🔴 N/A

❌ FAIL | rank(opt6_slopeavg1y)
   Sharpe: 0.18 | Fitness: 0.09 | Turnover: 2.2% | PnL: 📈 +$1.45M
   Score: Before=None → After=None | Change: 🔴 N/A

❌ FAIL | -rank(ts_delta(opt6_slopeavg1y, 5))
   Sharpe: 1.23 | Fitness: 0.58 | Turnover: 30.6% | PnL: 📈 +$3.42M
   Score: Before=None → After=None | Change: 🔴 N/A

❌ FAIL | -ts_rank(fn_liab_fair_val_l1_a, 129)
   Sharpe: 0.58 | Fitness: 0.36 | Turnover: 5.0% | PnL: 📈 +$2.43M
   Score: Before=None → After=None | Change: 🔴 N/A

❌ FAIL | -ts_rank(fn_liab_fair_val_l1_a, 200)
   Sharpe: 0.08 | Fitness: 0.02 | Turnover: 3.7% | PnL: 📈 +$241.2K
   Score: Before=None → After=None | Change: 🔴 N/A

❌ FAIL | 0.6*rank(opt6_2rtscf) + 0.4*(-ts_rank(fn_liab_fair_val_l1_a,129))
   Sharpe: 0.39 | Fitness: 0.22 | Turnover: 2.6% | PnL: 📈 +$1.90M
   Score: Before=None → After=None | Change: 🔴 N/A

❌ FAIL | 0.5*rank(opt6_slopeavg1y) + 0.5*(-ts_rank(fn_liab_fair_val_l1_a,129))
   Sharpe: -0.02 | Fitness: -0.00 | Turnover: 2.8% | PnL: 📉 -$152.4K
   Score: Before=None → After=None | Change: 🔴 N/A

❌ FAIL | rank(ts_mean(opt6_ivpctile1m, 10))
   Sharpe: 0.18 | Fitness: 0.05 | Turnover: 19.8% | PnL: 📈 +$621.7K
   Score: Before=None → After=None | Change: 🔴 N/A

❌ FAIL | 0.5*rank(opt6_2rtscf) + 0.5*rank(mdl177_garpanalystmodel_qgp_relgrowth)
   Sharpe: 0.80 | Fitness: 0.69 | Turnover: 5.1% | PnL: 📈 +$4.64M
   Score: Before=None → After=None | Change: 🔴 N/A

❌ FAIL | 0.4*rank(opt6_slopeavg1y) + 0.6*rank(mdl177_garpanalystmodel_qgp_relgrowth)
   Sharpe: 0.46 | Fitness: 0.31 | Turnover: 5.1% | PnL: 📈 +$2.82M
   Score: Before=None → After=None | Change: 🔴 N/A

❌ FAIL | rank(ts_mean(opt6_vimta3m, 5))
   Sharpe: 0.12 | Fitness: 0.06 | Turnover: 4.9% | PnL: 📈 +$1.50M
   Score: Before=None → After=None | Change: 🔴 N/A

❌ FAIL | -rank(opt6_vimta3m - opt6_vimta2m)
   Sharpe: 0.11 | Fitness: 0.02 | Turnover: 57.4% | PnL: 📈 +$547.4K
   Score: Before=None → After=None | Change: 🔴 N/A

    Delay 1 #1

    ❌ FAIL | rank(ts_mean(opt6_2rtscf, 5))
   Sharpe: 1.08 | Fitness: 0.84 | Turnover: 1.9% | PnL: 📈 +$3.70M
   Score: Before=None → After=None | Change: 🔴 N/A

❌ FAIL | group_rank(opt6_2rtscf, sector)
   Sharpe: 1.07 | Fitness: 0.82 | Turnover: 2.7% | PnL: 📈 +$3.62M
   Score: Before=None → After=None | Change: 🔴 N/A

✅ PASS | 0.7*rank(opt6_2rtscf) + 0.3*rank(mdl177_garpanalystmodel_qgp_relgrowth)
   Sharpe: 1.33 | Fitness: 1.19 | Turnover: 3.3% | PnL: 📈 +$4.92M
   Score: Before=None → After=None | Change: 🔴 N/A failed because of Weight is too strongly concentrated or too few instruments are assigned weight.

❌ FAIL | 0.5*group_rank(ts_mean(news_mins_10_pct_dn,5), sector) + 0.5*rank(opt6_slopeavg1y)
   Sharpe: 1.24 | Fitness: 0.87 | Turnover: 66.0% | PnL: 📈 +$16.09M
   Score: Before=None → After=None | Change: 🔴 N/A

✅ PASS | 0.4*rank(0.5*ts_mean(news_mins_10_pct_dn,10)+0.5*ts_mean(news_mins_10_pct_dn,40)) + 0.6*rank(opt6_slopeavg1y)
   Sharpe: 1.34 | Fitness: 1.09 | Turnover: 37.8% | PnL: 📈 +$12.36M
   Score: Before=None → After=None | Change: 🔴 N/A failed because of Weight is too strongly concentrated or too few instruments are assigned weight.

❌ FAIL | rank(opt6_absavgernmv)
   Sharpe: 0.30 | Fitness: 0.15 | Turnover: 2.1% | PnL: 📈 +$1.47M
   Score: Before=None → After=None | Change: 🔴 N/A

❌ FAIL | -rank(ts_mean(opt6_absavgernmv, 10))
   Sharpe: -0.34 | Fitness: -0.17 | Turnover: 1.5% | PnL: 📉 -$1.62M
   Score: Before=None → After=None | Change: 🔴 N/A

❌ FAIL | rank(ts_mean(opt6_ivpctile1m, 20))
   Sharpe: 0.66 | Fitness: 0.32 | Turnover: 12.4% | PnL: 📈 +$1.47M
   Score: Before=None → After=None | Change: 🔴 N/A

❌ FAIL | rank(ts_backfill(opt6_ivpctile1m, 5))
   Sharpe: 0.66 | Fitness: 0.16 | Turnover: 45.2% | PnL: 📈 +$1.38M
   Score: Before=None → After=None | Change: 🔴 N/A

❌ FAIL | rank(opt6_slopestd1y)
   Sharpe: -0.33 | Fitness: -0.11 | Turnover: 2.1% | PnL: 📉 -$746.8K
   Score: Before=None → After=None | Change: 🔴 N/A

❌ FAIL | -rank(ts_delta(opt6_slopeavg1y, 20))
   Sharpe: 0.45 | Fitness: 0.16 | Turnover: 9.3% | PnL: 📈 +$828.3K
   Score: Before=None → After=None | Change: 🔴 N/A

❌ FAIL | 0.5*rank(opt6_2rtscf) + 0.5*rank(opt6_slopeavg1y)
   Sharpe: 0.83 | Fitness: 0.67 | Turnover: 2.4% | PnL: 📈 +$4.07M
   Score: Before=None → After=None | Change: 🔴 N/A

❌ FAIL | group_rank(opt6_vimta3m, sector)
   Sharpe: 0.02 | Fitness: 0.00 | Turnover: 10.4% | PnL: 📈 +$229.9K
   Score: Before=None → After=None | Change: 🔴 N/A

❌ FAIL | rank(ts_delta(opt6_vimta3m, 10))
   Sharpe: 0.78 | Fitness: 0.24 | Turnover: 46.2% | PnL: 📈 +$2.17M
   Score: Before=None → After=None | Change: 🔴 N/A


]

--Gemini
[
    [Delay 0]

❌ FAIL | group_rank(rank(opt6_10dorhv / opt6_120dorhv), densify(industry))
   Sharpe: 0.56 | Fitness: 0.24 | Turnover: 18.1% | PnL: 📈 +$1.63M
   Score: Before=None → After=None | Change: 🔴 N/A

❌ FAIL | group_rank(rank(opt6_20div / opt6_vhslcd252), densify(industry))
   Sharpe: 0.30 | Fitness: 0.10 | Turnover: 17.5% | PnL: 📈 +$904.6K
   Score: Before=None → After=None | Change: 🔴 N/A

❌ FAIL | rank(ts_decay_linear(log(opt6_m1atmfitiv / opt6_m2atmfitiv), 10))
   Sharpe: -0.65 | Fitness: -0.26 | Turnover: 16.0% | PnL: 📉 -$1.30M
   Score: Before=None → After=None | Change: 🔴 N/A

❌ FAIL | group_neutralize(ts_zscore(opt6_vhslcd5 / opt6_vhslcd60, 20), industry)
   Sharpe: 0.00 | Fitness: 0.00 | Turnover: 0.0% | PnL: 📉 $0
   Score: Before=None → After=None | Change: 🔴 N/A

❌ FAIL | group_rank(zscore(opt6_fcstr2imp * opt6_90dorhv), densify(industry))
   Sharpe: 1.14 | Fitness: 1.00 | Turnover: 3.0% | PnL: 📈 +$4.80M
   Score: Before=None → After=None | Change: 🔴 N/A

❌ FAIL | group_rank(ts_delta(opt6_30div, 20), densify(industry))
   Sharpe: 0.68 | Fitness: 0.27 | Turnover: 29.1% | PnL: 📈 +$2.31M
   Score: Before=None → After=None | Change: 🔴 N/A

❌ FAIL | group_neutralize(ts_decay_linear(zscore(opt6_vim6 / opt6_20div), 15), industry)
   Sharpe: 0.15 | Fitness: 0.03 | Turnover: 11.2% | PnL: 📈 +$326.7K
   Score: Before=None → After=None | Change: 🔴 N/A

❌ FAIL | group_rank(rank(-ts_decay_linear(log(opt6_1000dorhv), 30)), densify(industry))
   Sharpe: -0.01 | Fitness: -0.00 | Turnover: 1.7% | PnL: 📉 -$58.8K
   Score: Before=None → After=None | Change: 🔴 N/A

❌ FAIL | rank(0.4 * rank(opt6_m1atmfitiv) + 0.6 * rank(opt6_m4atmfitiv))
   Sharpe: 0.11 | Fitness: 0.05 | Turnover: 7.6% | PnL: 📈 +$1.21M
   Score: Before=None → After=None | Change: 🔴 N/A

❌ FAIL | group_rank(rank(-ts_delta(opt6_or20divfcst / opt6_slcxp, 10)), densify(industry))
   Sharpe: -0.03 | Fitness: -0.00 | Turnover: 36.0% | PnL: 📉 -$147.8K
   Score: Before=None → After=None | Change: 🔴 N/A


Delay 1

❌ FAIL | group_neutralize(zscore(opt6_ivetfratio), industry)
   Sharpe: -0.24 | Fitness: -0.16 | Turnover: 5.0% | PnL: 📉 -$2.84M
   Score: Before=None → After=None | Change: 🔴 N/A

❌ FAIL | rank(ts_decay_linear(opt6_slopepctile, 10))
   Sharpe: -0.13 | Fitness: -0.03 | Turnover: 7.8% | PnL: 📉 -$274.0K
   Score: Before=None → After=None | Change: 🔴 N/A

❌ FAIL | group_rank(rank(opt6_ivspyratio / opt6_ivspyratioavg1m), densify(industry))
   Sharpe: -0.60 | Fitness: -0.12 | Turnover: 39.9% | PnL: 📉 -$835.2K
   Score: Before=None → After=None | Change: 🔴 N/A

❌ FAIL | group_rank(ts_decay_linear(zscore(opt6_ivpctilely), 20), densify(industry))
   Sharpe: 0.00 | Fitness: 0.00 | Turnover: 0.0% | PnL: 📉 $0
   Score: Before=None → After=None | Change: 🔴 N/A

❌ FAIL | group_neutralize(ts_decay_linear(log(opt6_slope / opt6_slopefcst), 15), industry)
   Sharpe: -0.23 | Fitness: -0.03 | Turnover: 68.6% | PnL: 📉 -$657.4K
   Score: Before=None → After=None | Change: 🔴 N/A

❌ FAIL | ts_decay_linear(opt6_slope, 5) * rank(opt6_stkvolu) + ts_decay_linear(opt6_slope, 20) * (1.0 - rank(opt6_stkvolu))
   Sharpe: 0.46 | Fitness: 0.30 | Turnover: 5.6% | PnL: 📈 +$2.71M
   Score: Before=None → After=None | Change: 🔴 N/A

❌ FAIL | group_rank(rank(opt6_impliediee * opt6_m1atmfitiv), densify(industry))
   Sharpe: 0.06 | Fitness: 0.02 | Turnover: 13.4% | PnL: 📈 +$465.3K
   Score: Before=None → After=None | Change: 🔴 N/A

❌ FAIL | vector_neut(group_rank(opt6_ivpctileetf, industry), rank(opt6_mktcap))
   Sharpe: 0.14 | Fitness: 0.05 | Turnover: 8.0% | PnL: 📈 +$935.5K
   Score: Before=None → After=None | Change: 🔴 N/A

❌ FAIL | group_rank(rank(ts_delta(opt6_xxpslckwi, 5)), densify(industry))
   Sharpe: 0.00 | Fitness: 0.00 | Turnover: 0.0% | PnL: 📉 $0
   Score: Before=None → After=None | Change: 🔴 N/A

Delay 1
❌ FAIL | group_rank(rank(opt6_volofvol / opt6_optvolu20davg), densify(industry))
   Sharpe: -0.02 | Fitness: -0.00 | Turnover: 2.6% | PnL: 📉 -$63.8K
   Score: Before=None → After=None | Change: 🔴 N/A

❌ FAIL | group_neutralize(ts_decay_linear(zscore(opt6_beta1m), 10), industry)
   Sharpe: -0.15 | Fitness: -0.07 | Turnover: 9.0% | PnL: 📉 -$1.39M
   Score: Before=None → After=None | Change: 🔴 N/A

❌ FAIL | group_rank(rank(-ts_std_dev(opt6_betaly, 20)), densify(industry))
   Sharpe: 0.00 | Fitness: 0.00 | Turnover: 0.0% | PnL: 📉 $0
   Score: Before=None → After=None | Change: 🔴 N/A

❌ FAIL | group_rank(ts_decay_linear(zscore(ts_backfill(opt6_volofivol, 2)), 20), industry)
   Sharpe: 0.55 | Fitness: 0.23 | Turnover: 2.0% | PnL: 📈 +$1.05M
   Score: Before=None → After=None | Change: 🔴 N/A

❌ FAIL | vector_neut(rank(opt6_optvolu20davg), rank(opt6_betaly))
   Sharpe: 0.00 | Fitness: 0.00 | Turnover: 0.0% | PnL: 📉 $0
   Score: Before=None → After=None | Change: 🔴 N/A

❌ FAIL | vector_neut(group_rank(opt6_px1kgam, industry), rank(opt6_volofvol))
   Sharpe: 0.16 | Fitness: 0.05 | Turnover: 2.9% | PnL: 📈 +$612.9K
   Score: Before=None → After=None | Change: 🔴 N/A

❌ FAIL | vector_neut(rank(ts_decay_linear(opt6_ivstdevly, 15)), rank(opt6_beta1m))
   Sharpe: 0.00 | Fitness: 0.00 | Turnover: 0.0% | PnL: 📉 $0
   Score: Before=None → After=None | Change: 🔴 N/A

❌ FAIL | group_neutralize(rank(0.5 * zscore(opt6_volofvol) + 0.5 * zscore(opt6_volofivol)), industry)
   Sharpe: -0.33 | Fitness: -0.12 | Turnover: 2.7% | PnL: 📉 -$804.9K
   Score: Before=None → After=None | Change: 🔴 N/A

❌ FAIL | group_rank(rank(-opt6_ivstdevsmean), densify(industry))
   Sharpe: 0.21 | Fitness: 0.07 | Turnover: 9.8% | PnL: 📈 +$620.2K
   Score: Before=None → After=None | Change: 🔴 N/A
]

--- Chatgpt
[
    [Delay 0] #0
    ❌ FAIL | rank(ts_decay_linear(zscore(opt6_ivetfratio),20))
   Sharpe: -0.05 | Fitness: -0.01 | Turnover: 4.0% | PnL: 📉 -$463.5K

❌ FAIL | rank(ts_decay_linear(zscore(opt6_etfivhvxernratio),20))
   Sharpe: 0.05 | Fitness: 0.01 | Turnover: 9.0% | PnL: 📈 +$131.0K

✅ PASS | rank(ts_mean(zscore(opt6_fcstr2imp),20))
   Sharpe: 1.26 | Fitness: 1.02 | Turnover: 1.6% | PnL: 📈 +$4.02M sharpe >2 to pass and fitness > 1.30 

❌ FAIL | rank(ts_decay_linear(zscore(opt6_derivinffcst),15))
   Sharpe: 0.36 | Fitness: 0.14 | Turnover: 5.5% | PnL: 📈 +$971.2K

❌ FAIL | group_rank(ts_decay_linear(zscore(opt6_ivetfratioavg1m),20),industry)
   Sharpe: 0.01 | Fitness: 0.00 | Turnover: 4.5% | PnL: 📈 +$56.6K

❌ FAIL | group_rank(ts_decay_linear(zscore(opt6_ivhvxernratio),20),subindustry)
   Sharpe: -0.17 | Fitness: -0.04 | Turnover: 9.5% | PnL: 📉 -$350.5K

❌ FAIL | rank(ts_mean(zscore(opt6_impliediee),15))
   Sharpe: 0.70 | Fitness: 0.40 | Turnover: 10.4% | PnL: 📈 +$2.06M

❌ FAIL | rank(ts_decay_linear(zscore(opt6_etfsloperatioavg1m),20))
   Sharpe: 0.55 | Fitness: 0.35 | Turnover: 4.4% | PnL: 📈 +$2.45M

❌ FAIL | group_rank(ts_mean(zscore(opt6_correletf1y),20),industry)
   Sharpe: 0.41 | Fitness: 0.21 | Turnover: 2.1% | PnL: 📈 +$1.56M

❌ FAIL | rank(ts_decay_linear(zscore(opt6_fcstr2imp*opt6_ivetfratio),15))
   Sharpe: 1.22 | Fitness: 0.98 | Turnover: 3.4% | PnL: 📈 +$4.01M

❌ FAIL | group_rank(rank(ts_mean(opt6_derivinf,20)),subindustry)
   Sharpe: 0.84 | Fitness: 0.43 | Turnover: 6.4% | PnL: 📈 +$1.64M

❌ FAIL | rank(ts_mean(zscore(opt6_etfivhvxernratio1m),15))
   Sharpe: 0.03 | Fitness: 0.00 | Turnover: 6.2% | PnL: 📈 +$72.9K

❌ FAIL | group_rank(ts_decay_linear(zscore(opt6_ivetfratioavg1y),20),industry)
   Sharpe: 0.01 | Fitness: 0.00 | Turnover: 4.5% | PnL: 📈 +$45.6K

❌ FAIL | rank(ts_decay_linear(zscore(opt6_ivetfratiostd1y),20))
   Sharpe: -0.07 | Fitness: -0.02 | Turnover: 4.1% | PnL: 📉 -$572.1K

❌ FAIL | group_rank(ts_mean(zscore(opt6_etfsloperatioavgstd1y),20),industry)
   Sharpe: 0.23 | Fitness: 0.07 | Turnover: 2.2% | PnL: 📈 +$617.0K


   [Delay 1] #1

❌ FAIL | rank(0.5*ts_mean(opt6_ivetfratio,10)+0.5*ts_mean(opt6_ivetfratio,40))
   Sharpe: -0.08 | Fitness: -0.03 | Turnover: 2.6% | PnL: 📉 -$783.1K

❌ FAIL | rank(0.5*ts_mean(opt6_ivhvxernratio,10)+0.5*ts_mean(opt6_ivhvxernratio,40))
   Sharpe: -0.25 | Fitness: -0.08 | Turnover: 7.1% | PnL: 📉 -$659.2K

❌ FAIL | rank(0.4*ts_mean(opt6_fcstr2imp,10)+0.6*ts_mean(opt6_fcstr2imp,60))
   Sharpe: 1.18 | Fitness: 0.99 | Turnover: 1.4% | PnL: 📈 +$4.36M

❌ FAIL | group_rank(ts_mean(opt6_derivinffcst,20),industry)
   Sharpe: 0.68 | Fitness: 0.39 | Turnover: 4.0% | PnL: 📈 +$2.02M

❌ FAIL | group_rank(ts_mean(opt6_impliediee,20),subindustry)
   Sharpe: 0.91 | Fitness: 0.56 | Turnover: 9.2% | PnL: 📈 +$2.33M

❌ FAIL | rank(ts_mean(opt6_etfsloperatioavg1y,20))
   Sharpe: 0.63 | Fitness: 0.46 | Turnover: 1.6% | PnL: 📈 +$3.33M

❌ FAIL | rank(ts_mean(opt6_etfivhvxernratio1y,20))
   Sharpe: -0.16 | Fitness: -0.04 | Turnover: 1.7% | PnL: 📉 -$439.5K

❌ FAIL | group_rank(ts_mean(opt6_ivetfratioavg1m,20),industry)
   Sharpe: 0.07 | Fitness: 0.02 | Turnover: 3.0% | PnL: 📈 +$572.8K

❌ FAIL | group_rank(ts_mean(opt6_ivetfratioavg1y,20),subindustry)
   Sharpe: 0.10 | Fitness: 0.03 | Turnover: 3.4% | PnL: 📈 +$668.4K

❌ FAIL | rank(ts_mean(opt6_correletf1y,30))
   Sharpe: 0.47 | Fitness: 0.28 | Turnover: 1.6% | PnL: 📈 +$2.16M

❌ FAIL | rank(ts_mean(opt6_correlspy1y,30))
   Sharpe: 0.35 | Fitness: 0.18 | Turnover: 1.7% | PnL: 📈 +$1.66M

❌ FAIL | group_rank(ts_mean(opt6_etfsloperatioavgstd1y,20),industry)
   Sharpe: 0.58 | Fitness: 0.31 | Turnover: 2.1% | PnL: 📈 +$1.74M

❌ FAIL | rank(ts_mean(opt6_am002vi,30))
   Sharpe: -0.07 | Fitness: -0.02 | Turnover: 1.0% | PnL: 📉 -$696.5K

❌ FAIL | group_rank(ts_mean(opt6_absavgernmv,20),subindustry)
   Sharpe: 0.54 | Fitness: 0.32 | Turnover: 1.5% | PnL: 📈 +$2.15M

❌ FAIL | rank(ts_mean(opt6_divyield,40))
   Sharpe: 0.12 | Fitness: 0.04 | Turnover: 0.9% | PnL: 📈 +$678.4K

    [Delay 1] #2

    ❌ FAIL | rank(ts_mean(opt6_fcstr2imp,20))*rank(ts_mean(opt6_ivetfratio,20))
   Sharpe: 0.85 | Fitness: 0.69 | Turnover: 2.5% | PnL: 📈 +$4.10M

❌ FAIL | rank(ts_mean(opt6_impliediee,20))*rank(ts_mean(opt6_derivinffcst,20))
   Sharpe: 0.33 | Fitness: 0.14 | Turnover: 7.0% | PnL: 📈 +$1.12M

❌ FAIL | rank(ts_mean(opt6_etfivhvxernratio1m,20))*rank(ts_mean(opt6_fcstr2imp,20))
   Sharpe: 0.94 | Fitness: 0.64 | Turnover: 4.4% | PnL: 📈 +$2.85M

❌ FAIL | 0.5*rank(ts_mean(opt6_ivetfratioavg1m,20))+0.5*rank(ts_mean(opt6_correlspy1y,20))
   Sharpe: 0.23 | Fitness: 0.10 | Turnover: 2.9% | PnL: 📈 +$1.20M

❌ FAIL | 0.5*rank(ts_mean(opt6_correletf1y,20))+0.5*rank(ts_mean(opt6_etfsloperatioavg1y,20))
   Sharpe: 0.61 | Fitness: 0.42 | Turnover: 1.6% | PnL: 📈 +$2.91M

❌ FAIL | group_rank(rank(ts_mean(opt6_derivinf,20))*rank(ts_mean(opt6_fcstr2imp,20)),industry)
   Sharpe: 1.03 | Fitness: 0.75 | Turnover: 4.2% | PnL: 📈 +$3.25M

❌ FAIL | group_rank(rank(ts_mean(opt6_impliediee,20))*rank(ts_mean(opt6_etfivhvxernratio1m,20)),subindustry)
   Sharpe: 0.44 | Fitness: 0.20 | Turnover: 7.8% | PnL: 📈 +$1.26M

❌ FAIL | rank(ts_decay_linear(opt6_ivetfratioavg1y,20))*rank(ts_decay_linear(opt6_fcstr2imp,20))
   Sharpe: 0.85 | Fitness: 0.69 | Turnover: 3.2% | PnL: 📈 +$4.12M

❌ FAIL | rank(ts_decay_linear(opt6_etfsloperatioavg1m,20))*rank(ts_decay_linear(opt6_derivinffcst,20))
   Sharpe: 0.42 | Fitness: 0.22 | Turnover: 5.0% | PnL: 📈 +$1.74M

❌ FAIL | group_rank(rank(ts_mean(opt6_ivetfratiostd1y,20)),industry)
   Sharpe: -0.03 | Fitness: -0.01 | Turnover: 3.1% | PnL: 📉 -$240.1K

❌ FAIL | group_rank(rank(ts_mean(opt6_beta1y,20)),industry)
   Sharpe: 0.27 | Fitness: 0.16 | Turnover: 2.2% | PnL: 📈 +$2.07M

❌ FAIL | group_rank(rank(ts_mean(opt6_beta1m,20)),subindustry)
   Sharpe: 0.14 | Fitness: 0.05 | Turnover: 6.6% | PnL: 📈 +$927.1K

❌ FAIL | rank(ts_mean(opt6_divyield,20))*rank(ts_mean(opt6_divfreq,20))
   Sharpe: 0.38 | Fitness: 0.21 | Turnover: 1.1% | PnL: 📈 +$1.94M

❌ FAIL | rank(ts_mean(opt6_ioc,20))*rank(ts_mean(opt6_cvolu,20))
   Sharpe: 0.14 | Fitness: 0.04 | Turnover: 2.2% | PnL: 📈 +$548.6K

❌ FAIL | group_rank(rank(ts_mean(opt6_absavgernmv,20)),industry)
   Sharpe: 0.33 | Fitness: 0.16 | Turnover: 1.4% | PnL: 📈 +$1.47M

]

[
    [Delay 0] #0

❌ FAIL | rank(ts_mean(opt6_fcstr2imp,20)-ts_mean(opt6_fcstr2imp,120))*rank(ts_delta(opt6_fcstr2imp,20))
   Sharpe: 0.12 | Fitness: 0.03 | Turnover: 6.7% | PnL: 📈 +$303.8K

❌ FAIL | rank(ts_decay_linear(ts_delta(opt6_fcstr2imp,20),10))*rank(ts_mean(opt6_fcstr2imp,60))
   Sharpe: 1.15 | Fitness: 0.82 | Turnover: 6.3% | PnL: 📈 +$3.17M

❌ FAIL | group_rank(rank(ts_mean(opt6_fcstr2imp,20)-ts_mean(opt6_fcstr2imp,80)),subindustry)
   Sharpe: -0.15 | Fitness: -0.03 | Turnover: 3.8% | PnL: 📉 -$302.5K

❌ FAIL | rank(ts_mean(opt6_fcstr2imp,20))*rank(ts_mean(opt6_derivinf,20))*rank(ts_delta(opt6_derivinf,20))
   Sharpe: 0.93 | Fitness: 0.36 | Turnover: 33.5% | PnL: 📈 +$2.54M

❌ FAIL | rank(ts_mean(opt6_fcstr2imp,20))*rank(ts_mean(opt6_derivinffcst,20))*rank(ts_delta(opt6_fcstr2imp,20))
   Sharpe: 1.00 | Fitness: 0.72 | Turnover: 7.6% | PnL: 📈 +$3.20M

❌ FAIL | group_rank(rank(ts_mean(opt6_fcstr2imp,20))*rank(ts_mean(opt6_impliediee,20)),industry)
   Sharpe: 0.95 | Fitness: 0.69 | Turnover: 6.8% | PnL: 📈 +$3.24M

❌ FAIL | rank(ts_decay_linear(opt6_fcstr2imp,20))*rank(ts_decay_linear(opt6_derivinf,20))
   Sharpe: 1.12 | Fitness: 0.83 | Turnover: 6.1% | PnL: 📈 +$3.44M

❌ FAIL | rank(ts_mean(opt6_fcstr2imp,20)-ts_mean(opt6_fcstr2imp,60))*rank(ts_mean(opt6_impliediee,20))
   Sharpe: 0.39 | Fitness: 0.14 | Turnover: 7.2% | PnL: 📈 +$796.5K

❌ FAIL | group_rank(rank(ts_delta(opt6_fcstr2imp,40))*rank(ts_mean(opt6_derivinf,20)),subindustry)
   Sharpe: 0.45 | Fitness: 0.16 | Turnover: 8.1% | PnL: 📈 +$735.1K

❌ FAIL | rank(ts_delta(opt6_fcstr2imp,20))*rank(ts_delta(opt6_derivinffcst,20))*rank(ts_mean(opt6_fcstr2imp,60))
   Sharpe: 1.33 | Fitness: 0.85 | Turnover: 15.5% | PnL: 📈 +$3.14M


   [Delay 1] #1


❌ FAIL | 0.5*rank(ts_mean(opt6_fcstr2imp,20))+0.5*rank(ts_mean(opt6_derivinf,20))
   Sharpe: 1.09 | Fitness: 0.92 | Turnover: 3.9% | PnL: 📈 +$4.39M

❌ FAIL | 0.4*rank(ts_mean(opt6_fcstr2imp,20))+0.6*group_rank(ts_mean(opt6_derivinffcst,20),industry)
   Sharpe: 0.75 | Fitness: 0.55 | Turnover: 3.9% | PnL: 📈 +$3.29M

❌ FAIL | rank(ts_mean(opt6_fcstr2imp,20))*rank(ts_mean(opt6_impliediee,20))
   Sharpe: 0.92 | Fitness: 0.69 | Turnover: 5.4% | PnL: 📈 +$3.47M

❌ FAIL | group_rank(rank(ts_mean(opt6_fcstr2imp,20))*rank(ts_mean(opt6_derivinf,20)),industry)
   Sharpe: 1.22 | Fitness: 1.03 | Turnover: 3.6% | PnL: 📈 +$4.39M

❌ FAIL | rank(ts_mean(opt6_fcstr2imp,20)-ts_mean(opt6_fcstr2imp,80))*rank(ts_mean(opt6_derivinffcst,20))
   Sharpe: 0.42 | Fitness: 0.18 | Turnover: 3.9% | PnL: 📈 +$1.15M

❌ FAIL | rank(ts_mean(opt6_fcstr2imp,20))*rank(ts_delta(opt6_derivinf,40))
   Sharpe: 1.21 | Fitness: 0.68 | Turnover: 24.4% | PnL: 📈 +$3.86M

❌ FAIL | rank(ts_decay_linear(opt6_fcstr2imp,20))*rank(ts_mean(opt6_impliediee,20))
   Sharpe: 0.91 | Fitness: 0.68 | Turnover: 5.8% | PnL: 📈 +$3.43M

❌ FAIL | group_rank(rank(ts_mean(opt6_derivinf,20))*rank(ts_mean(opt6_impliediee,20)),industry)
   Sharpe: 0.97 | Fitness: 0.69 | Turnover: 6.3% | PnL: 📈 +$3.09M

❌ FAIL | 0.3*rank(ts_mean(opt6_fcstr2imp,20))+0.7*rank(ts_mean(opt6_derivinffcst,20))
   Sharpe: 0.68 | Fitness: 0.46 | Turnover: 3.7% | PnL: 📈 +$2.81M

❌ FAIL | rank(ts_mean(opt6_fcstr2imp,20))*rank(ts_mean(opt6_derivinffcst,20))*rank(ts_mean(opt6_impliediee,20))
   Sharpe: 0.63 | Fitness: 0.41 | Turnover: 5.6% | PnL: 📈 +$2.60M

   [Delay 1] #2

   ❌ FAIL | group_rank(rank(ts_mean(opt6_fcstr2imp,20)-ts_mean(opt6_fcstr2imp,120)),industry)
   Sharpe: -0.03 | Fitness: -0.00 | Turnover: 3.0% | PnL: 📉 -$64.7K

❌ FAIL | group_rank(rank(ts_delta(opt6_fcstr2imp,60)),industry)
   Sharpe: -0.00 | Fitness: -0.00 | Turnover: 5.2% | PnL: 📉 -$2.3K

❌ FAIL | rank(ts_mean(opt6_fcstr2imp,20))*group_rank(ts_mean(opt6_derivinf,20),industry)
   Sharpe: 1.00 | Fitness: 0.70 | Turnover: 4.1% | PnL: 📈 +$3.02M

❌ FAIL | rank(ts_mean(opt6_fcstr2imp,20))*group_rank(ts_mean(opt6_impliediee,20),subindustry)
   Sharpe: 0.90 | Fitness: 0.59 | Turnover: 6.3% | PnL: 📈 +$2.69M

❌ FAIL | group_rank(rank(ts_mean(opt6_derivinffcst,20))*rank(ts_mean(opt6_impliediee,20)),industry)
   Sharpe: 0.48 | Fitness: 0.24 | Turnover: 6.5% | PnL: 📈 +$1.55M

❌ FAIL | rank(ts_mean(opt6_fcstr2imp,20)-ts_mean(opt6_fcstr2imp,60))*rank(ts_mean(opt6_derivinf,20)-ts_mean(opt6_derivinf,60))
   Sharpe: 0.03 | Fitness: 0.00 | Turnover: 8.0% | PnL: 📈 +$46.7K

❌ FAIL | rank(ts_decay_linear(opt6_fcstr2imp,20))*rank(ts_decay_linear(opt6_impliediee,20))
   Sharpe: 0.99 | Fitness: 0.72 | Turnover: 7.0% | PnL: 📈 +$3.25M

❌ FAIL | group_rank(rank(ts_delta(opt6_derivinffcst,40))*rank(ts_mean(opt6_fcstr2imp,20)),subindustry)
   Sharpe: 1.31 | Fitness: 0.91 | Turnover: 9.5% | PnL: 📈 +$2.99M

❌ FAIL | rank(ts_mean(opt6_fcstr2imp,20))*rank(ts_delta(opt6_impliediee,40))*rank(ts_mean(opt6_derivinf,20))
   Sharpe: 1.05 | Fitness: 0.62 | Turnover: 16.9% | PnL: 📈 +$2.92M

❌ FAIL | group_rank(rank(ts_mean(opt6_fcstr2imp,20))*rank(ts_mean(opt6_derivinffcst,20))*rank(ts_mean(opt6_impliediee,20)),industry)
   Sharpe: 0.76 | Fitness: 0.52 | Turnover: 5.5% | PnL: 📈 +$2.91M
]