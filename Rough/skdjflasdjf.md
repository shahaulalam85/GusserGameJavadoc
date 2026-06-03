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