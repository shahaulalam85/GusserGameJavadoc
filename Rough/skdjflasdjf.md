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
    ["],
    ["],
    ["],
    ["],
    ["],
    ["],
    ["],
    ["],
    ["],
    ["],
    ["],
    ["],
    ["],
    ["],
    ["],
    ["],
    ["],
    ["],
]