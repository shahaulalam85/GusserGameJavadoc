Testing alphas...

❌ FAIL | ts_backfill(vec_avg(ern4_ernmv1), 5)
   Sharpe: -0.22 | Fitness: -0.06 | Turnover: 4.2% | PnL: 📉 -$523.0K

❌ FAIL | rank(vec_avg(ern4_30div) - vec_avg(ern4_30dexerniv))
   Sharpe: 0.32 | Fitness: 0.08 | Turnover: 32.2% | PnL: 📈 +$908.1K

❌ FAIL | rank(vec_avg(ern4_absavgernmv) / (vec_avg(ern4_ernmvstdev) + 0.001))
   Sharpe: 0.88 | Fitness: 0.36 | Turnover: 7.3% | PnL: 📈 +$1.03M

❌ FAIL | ts_backfill(vec_avg(ern4_ernmv2), 5)
   Sharpe: -0.06 | Fitness: -0.01 | Turnover: 4.0% | PnL: 📉 -$134.4K

❌ FAIL | rank(vec_avg(ern4_m3atmiv) - vec_avg(ern4_m2atmiv))
   Sharpe: -0.09 | Fitness: -0.01 | Turnover: 34.6% | PnL: 📉 -$252.0K

❌ FAIL | rank(vec_avg(ern4_1000dclshv) - vec_avg(ern4_10dclshv))
   Sharpe: -0.64 | Fitness: -0.30 | Turnover: 19.8% | PnL: 📉 -$2.20M

❌ FAIL | rank(vec_avg(ern4_avg20doptvolu))
   Sharpe: 0.29 | Fitness: 0.12 | Turnover: 8.7% | PnL: 📈 +$1.01M

❌ FAIL | rank(vec_avg(ern4_fcsterneffct) - ts_backfill(vec_avg(ern4_erneffct1), 5))
   Sharpe: 0.51 | Fitness: 0.17 | Turnover: 9.6% | PnL: 📈 +$683.9K

❌ FAIL | -rank(vec_avg(ern4_impernmv90d) - vec_avg(ern4_absavgernmv))
   Sharpe: 0.02 | Fitness: 0.00 | Turnover: 16.5% | PnL: 📈 +$83.9K

❌ FAIL | rank(vec_avg(ern4_m4atmiv) - vec_avg(ern4_m1atmiv))
   Sharpe: 0.04 | Fitness: 0.00 | Turnover: 31.1% | PnL: 📈 +$104.1K


Testing alphas...

❌ FAIL | rank(ts_delta(anl4_afv4_eps_mean, 63))
   Sharpe: 0.64 | Fitness: 0.34 | Turnover: 4.7% | PnL: 📈 +$1.72M

❌ FAIL | rank(actual_eps_value_quarterly - anl4_afv4_eps_mean)
   Sharpe: -0.49 | Fitness: -0.31 | Turnover: 1.4% | PnL: 📉 -$2.52M

❌ FAIL | rank(ts_delta(sales_estimate_average, 63))
   Sharpe: 0.21 | Fitness: 0.07 | Turnover: 4.6% | PnL: 📈 +$601.2K

 ❌ FAIL | -rank(ts_delta(anl4_afv4_dts_spe, 63))
   Sharpe: -0.28 | Fitness: -0.08 | Turnover: 7.1% | PnL: 📉 -$505.4K

❌ FAIL | rank(ts_delta(anl4_afv4_eps_number, 63))
   Sharpe: -0.47 | Fitness: -0.15 | Turnover: 4.7% | PnL: 📉 -$598.0K

❌ FAIL | rank(ts_delta(anl4_ebitda_value / actual_sales_value_quarterly, 63))
   Sharpe: 0.56 | Fitness: 0.23 | Turnover: 5.5% | PnL: 📈 +$1.06M

❌ FAIL | rank(eps_max_guidance_quarterly - anl4_afv4_eps_mean)
   Sharpe: -0.40 | Fitness: -0.25 | Turnover: 1.1% | PnL: 📉 -$2.32M

❌ FAIL | -rank((anl4_afv4_eps_high - anl4_afv4_eps_low) / (abs(anl4_afv4_eps_mean) + 0.01))
   Sharpe: -0.04 | Fitness: -0.00 | Turnover: 2.4% | PnL: 📉 -$80.0K

❌ FAIL | rank(actual_sales_value_quarterly - sales_estimate_average)
   Sharpe: -0.67 | Fitness: -0.34 | Turnover: 2.3% | PnL: 📉 -$1.62M

❌ FAIL | rank(ts_delta(anl4_ebit_value / actual_sales_value_quarterly, 63))
   Sharpe: 0.71 | Fitness: 0.33 | Turnover: 5.5% | PnL: 📈 +$1.34M

❌ FAIL | ts_backfill(vec_avg(ern4_ernmv1), 5)
   Sharpe: -0.07 | Fitness: -0.01 | Turnover: 4.2% | PnL: 📉 -$163.3K

❌ FAIL | rank(vec_avg(ern4_30div) - vec_avg(ern4_30dexerniv))
   Sharpe: 0.17 | Fitness: 0.03 | Turnover: 39.4% | PnL: 📈 +$506.8K

❌ FAIL | rank(vec_avg(ern4_absavgernmv) / (vec_avg(ern4_ernmvstdev) + 0.001))
   Sharpe: 0.57 | Fitness: 0.19 | Turnover: 7.3% | PnL: 📈 +$713.6K

❌ FAIL | ts_backfill(vec_avg(ern4_ernmv2), 5)
   Sharpe: 0.25 | Fitness: 0.08 | Turnover: 4.0% | PnL: 📈 +$569.8K

❌ FAIL | rank(vec_avg(ern4_m3atmiv) - vec_avg(ern4_m2atmiv))
   Sharpe: 0.09 | Fitness: 0.01 | Turnover: 46.8% | PnL: 📈 +$247.2K

❌ FAIL | rank(vec_avg(ern4_1000dclshv) - vec_avg(ern4_10dclshv))
   Sharpe: -0.58 | Fitness: -0.27 | Turnover: 22.3% | PnL: 📉 -$2.40M

❌ FAIL | rank(vec_avg(ern4_avg20doptvolu))
   Sharpe: 0.18 | Fitness: 0.06 | Turnover: 8.7% | PnL: 📈 +$725.1K

❌ FAIL | rank(vec_avg(ern4_fcsterneffct) - ts_backfill(vec_avg(ern4_erneffct1), 5))
   Sharpe: 0.60 | Fitness: 0.23 | Turnover: 10.0% | PnL: 📈 +$869.2K

❌ FAIL | -rank(vec_avg(ern4_impernmv90d) - vec_avg(ern4_absavgernmv))
   Sharpe: 0.04 | Fitness: 0.01 | Turnover: 20.7% | PnL: 📈 +$170.6K

❌ FAIL | rank(vec_avg(ern4_m4atmiv) - vec_avg(ern4_m1atmiv))
   Sharpe: -0.02 | Fitness: -0.00 | Turnover: 41.7% | PnL: 📉 -$79.5K


####################

Testing alphas...

   ⚠️  Score fetch failed: Expecting value: line 1 column 1 (char 0)
✅ PASS | 0.3*rank(anl4_bvps_flag) + 0.7*rank(mdl177_garpanalystmodel_qgp_relgrowth)
   Sharpe: 1.65 | Fitness: 1.71 | Turnover: 3.3% | PnL: 📈 +$6.67M

   ⚠️  Score fetch failed: Expecting value: line 1 column 1 (char 0)
✅ PASS | 0.3*rank(0.5*ts_mean(anl4_bvps_flag, 10) + 0.5*ts_mean(anl4_bvps_flag, 40)) + 0.7*rank(mdl177_garpanalystmodel_qgp_relgrowth)
   Sharpe: 1.63 | Fitness: 1.68 | Turnover: 3.1% | PnL: 📈 +$6.58M

❌ FAIL | 0.3*rank(anl4_ebit_flag) + 0.7*rank(mdl177_garpanalystmodel_qgp_relgrowth)
   Sharpe: 0.00 | Fitness: 0.00 | Turnover: 0.0% | PnL: 📉 $0

   ⚠️  Score fetch failed: Expecting value: line 1 column 1 (char 0)
✅ PASS | 0.3*rank(rel_num_comp) + 0.7*rank(mdl177_garpanalystmodel_qgp_relgrowth)
   Sharpe: 1.43 | Fitness: 1.33 | Turnover: 2.6% | PnL: 📈 +$5.35M

   ⚠️  Score fetch failed: Expecting value: line 1 column 1 (char 0)
✅ PASS | 0.3*rank(ts_mean(rel_num_comp, 20)) + 0.7*rank(mdl177_garpanalystmodel_qgp_relgrowth)
   Sharpe: 1.42 | Fitness: 1.32 | Turnover: 2.6% | PnL: 📈 +$5.33M

✅ PASS | 0.3*rank(opt6_2rtscf) + 0.7*rank(mdl177_garpanalystmodel_qgp_relgrowth)
   Sharpe: 1.34 | Fitness: 1.26 | Turnover: 3.4% | PnL: 📈 +$5.45M

   ⚠️  Score fetch failed: Expecting value: line 1 column 1 (char 0)
✅ PASS | 0.3*rank(anl4_capex_flag) + 0.7*rank(mdl177_garpanalystmodel_qgp_relgrowth)
   Sharpe: 1.47 | Fitness: 1.35 | Turnover: 3.4% | PnL: 📈 +$5.18M

   ⚠️  Score fetch failed: Expecting value: line 1 column 1 (char 0)
✅ PASS | 0.3*rank(0.5*ts_mean(announcement_effect_7, 10) + 0.5*ts_mean(announcement_effect_7, 40)) + 0.7*rank(mdl177_garpanalystmodel_qgp_relgrowth)
   Sharpe: 1.31 | Fitness: 1.18 | Turnover: 2.9% | PnL: 📈 +$4.98M

   ⚠️  Score fetch failed: Expecting value: line 1 column 1 (char 0)
✅ PASS | 0.3*rank(ts_mean(rank(anl4_bvps_flag), 20)) + 0.7*rank(mdl177_garpanalystmodel_qgp_relgrowth)
   Sharpe: 1.63 | Fitness: 1.67 | Turnover: 3.5% | PnL: 📈 +$6.50M

   ⚠️  Score fetch failed: Expecting value: line 1 column 1 (char 0)
✅ PASS | 0.2*rank(anl4_bvps_flag) + 0.1*rank(rel_num_all) + 0.7*rank(mdl177_garpanalystmodel_qgp_relgrowth)
   Sharpe: 1.63 | Fitness: 1.71 | Turnover: 3.3% | PnL: 📈 +$6.77M

❌ FAIL | rank(ts_delta(fnd7_ointfund_21fpeo, 63))
   Sharpe: 0.17 | Fitness: 0.05 | Turnover: 3.7% | PnL: 📈 +$489.9K

❌ FAIL | rank((fnd7_ointfund_qfcnao - fnd7_ointfund_qin) / fnd7_ointfund_qta)
   Sharpe: 0.45 | Fitness: 0.23 | Turnover: 3.1% | PnL: 📈 +$1.64M

❌ FAIL | rank(fnd7_ointfund_qip / fnd7_ointfund_qta)
   Sharpe: 0.13 | Fitness: 0.05 | Turnover: 2.0% | PnL: 📈 +$868.3K

❌ FAIL | rank(-fnd7_ointfund_qhcvni / fnd7_ointfund_qelas)
   Sharpe: -1.20 | Fitness: -0.72 | Turnover: 3.0% | PnL: 📉 -$2.26M

❌ FAIL | rank(fnd7_ointfund_qin / fnd7_ointfund_qqec)
   Sharpe: 0.36 | Fitness: 0.19 | Turnover: 2.1% | PnL: 📈 +$1.72M

❌ FAIL | -rank(ts_delta(fnd7_ointfund_qttld / fnd7_ointfund_qta, 63))
   Sharpe: 0.41 | Fitness: 0.15 | Turnover: 4.4% | PnL: 📈 +$844.8K

❌ FAIL | rank(ts_delta(fnd7_ointfund_qpdbio / fnd7_ointfund_qelas, 63))
   Sharpe: 0.45 | Fitness: 0.17 | Turnover: 4.9% | PnL: 📈 +$834.1K

❌ FAIL | 0.3*rank(ts_delta(fnd7_ointfund_21fpeo, 63)) + 0.7*rank(mdl177_garpanalystmodel_qgp_relgrowth)
   Sharpe: 1.20 | Fitness: 0.89 | Turnover: 4.1% | PnL: 📈 +$3.39M

❌ FAIL | 0.3*rank((fnd7_ointfund_qfcnao - fnd7_ointfund_qin) / fnd7_ointfund_qta) + 0.7*rank(mdl177_garpanalystmodel_qgp_relgrowth)
   Sharpe: 1.24 | Fitness: 1.03 | Turnover: 3.8% | PnL: 📈 +$4.27M

   ⚠️  Score fetch failed: Expecting value: line 1 column 1 (char 0)
✅ PASS | -rank(max_adjusted_net_income_guidance - min_adjusted_net_income_guidance) + 0.2*rank(anl4_bvps_flag)
   Sharpe: 1.81 | Fitness: 1.87 | Turnover: 1.9% | PnL: 📈 +$6.62M


✅ PASS | rank(anl4_bvps_flag)
   Sharpe: 1.36 | Fitness: 1.28 | Turnover: 1.8% | PnL: 📈 +$5.50M

✅ PASS | ts_mean(rank(anl4_bvps_flag), 20)
   Sharpe: 1.32 | Fitness: 1.23 | Turnover: 1.5% | PnL: 📈 +$5.35M

   ⚠️  Score fetch failed: Expecting value: line 1 column 1 (char 0)
✅ PASS | rank(ts_mean(rank(anl4_bvps_flag), 20))
   Sharpe: 1.37 | Fitness: 1.24 | Turnover: 4.0% | PnL: 📈 +$5.11M

   ⚠️  Score fetch failed: Expecting value: line 1 column 1 (char 0)
✅ PASS | 0.5*rank(anl4_ptp_flag) + 0.5*rank(anl4_bvps_flag)
   Sharpe: 1.49 | Fitness: 1.49 | Turnover: 2.5% | PnL: 📈 +$6.18M

   ⚠️  Score fetch failed: Expecting value: line 1 column 1 (char 0)
✅ PASS | ts_mean(0.5*rank(anl4_ptp_flag) + 0.5*rank(anl4_bvps_flag), 20)
   Sharpe: 1.53 | Fitness: 1.55 | Turnover: 2.0% | PnL: 📈 +$6.34M

❌ FAIL | rank(anl4_ebit_flag)
   Sharpe: 0.00 | Fitness: 0.00 | Turnover: 0.0% | PnL: 📉 $0

❌ FAIL | ts_mean(rank(anl4_ebit_flag), 20)
   Sharpe: 0.00 | Fitness: 0.00 | Turnover: 0.0% | PnL: 📉 $0

❌ FAIL | rank(ts_mean(rank(anl4_ebit_flag), 20))
   Sharpe: 0.00 | Fitness: 0.00 | Turnover: 0.0% | PnL: 📉 $0

❌ FAIL | 0.5*rank(anl4_bvps_flag) + 0.5*rank(anl4_ebit_flag)
   Sharpe: 0.00 | Fitness: 0.00 | Turnover: 0.0% | PnL: 📉 $0

❌ FAIL | 0.33*rank(anl4_ptp_flag) + 0.33*rank(anl4_bvps_flag) + 0.34*rank(anl4_ebit_flag)
   Sharpe: 0.00 | Fitness: 0.00 | Turnover: 0.0% | PnL: 📉 $0


######################

Testing alphas...

❌ FAIL | rank(ts_delta(fnd7_ointfund_21fpeo, 63))
   Sharpe: 0.20 | Fitness: 0.06 | Turnover: 4.2% | PnL: 📈 +$584.7K

❌ FAIL | rank(fnd7_ointfund_qip / fnd7_ointfund_qta)
   Sharpe: 0.13 | Fitness: 0.05 | Turnover: 2.0% | PnL: 📈 +$872.5K

❌ FAIL | -rank(ts_delta(fnd7_ointfund_qttld / fnd7_ointfund_qta, 63))
   Sharpe: 0.40 | Fitness: 0.14 | Turnover: 4.7% | PnL: 📈 +$812.8K

❌ FAIL | rank((fnd7_ointfund_qfcnao - fnd7_ointfund_qin) / fnd7_ointfund_qta)
   Sharpe: 0.45 | Fitness: 0.23 | Turnover: 3.0% | PnL: 📈 +$1.62M

❌ FAIL | group_rank(fnd7_ointfund_qip / fnd7_ointfund_qta, industry)
   Sharpe: 0.09 | Fitness: 0.03 | Turnover: 2.0% | PnL: 📈 +$486.5K

❌ FAIL | group_zscore(fnd7_ointfund_qip / fnd7_ointfund_qta, industry)
   Sharpe: 0.24 | Fitness: 0.12 | Turnover: 2.9% | PnL: 📈 +$1.65M

❌ FAIL | rank(ts_delta(fnd7_ointfund_21fpeo, 21) - ts_delta(fnd7_ointfund_21fpeo, 63))
   Sharpe: -0.00 | Fitness: -0.00 | Turnover: 7.0% | PnL: 📉 -$12.6K

❌ FAIL | rank(fnd7_ointfund_qin / fnd7_ointfund_qqec)
   Sharpe: 0.38 | Fitness: 0.20 | Turnover: 2.1% | PnL: 📈 +$1.79M

❌ FAIL | rank(ts_delta(fnd7_ointfund_qfcnao / fnd7_ointfund_qta, 63))
   Sharpe: 0.38 | Fitness: 0.18 | Turnover: 5.4% | PnL: 📈 +$1.45M

❌ FAIL | -group_rank(fnd7_ointfund_qttld / fnd7_ointfund_qta, industry)
   Sharpe: -1.37 | Fitness: -1.11 | Turnover: 1.4% | PnL: 📉 -$4.03M

Testing alphas...

❌ FAIL | group_rank(anl4_ebit_flag, sector)
   Sharpe: 0.00 | Fitness: 0.00 | Turnover: 0.0% | PnL: 📉 $0

❌ FAIL | group_zscore(anl4_ebit_flag, sector)
   Sharpe: 0.00 | Fitness: 0.00 | Turnover: 0.0% | PnL: 📉 $0

❌ FAIL | ts_rank(anl4_ebit_flag, 60)
   Sharpe: 0.00 | Fitness: 0.00 | Turnover: 0.0% | PnL: 📉 $0

❌ FAIL | group_rank(anl4_capex_flag, sector)
   Sharpe: 0.56 | Fitness: 0.28 | Turnover: 1.8% | PnL: 📈 +$1.50M

❌ FAIL | group_zscore(anl4_capex_flag, sector)
   Sharpe: 0.91 | Fitness: 0.76 | Turnover: 2.0% | PnL: 📈 +$4.36M

❌ FAIL | rank(anl4_ebit_flag) * rank(anl4_bvps_flag)
   Sharpe: 0.00 | Fitness: 0.00 | Turnover: 0.0% | PnL: 📉 $0

❌ FAIL | rank(anl4_ebit_flag) - rank(anl4_capex_flag)
   Sharpe: 0.00 | Fitness: 0.00 | Turnover: 0.0% | PnL: 📉 $0

❌ FAIL | group_rank(ts_mean(anl4_ebit_flag, 20), sector)
   Sharpe: 0.00 | Fitness: 0.00 | Turnover: 0.0% | PnL: 📉 $0

❌ FAIL | rank(ts_decay_linear(anl4_ebit_flag, 20))
   Sharpe: 0.00 | Fitness: 0.00 | Turnover: 0.0% | PnL: 📉 $0

❌ FAIL | ts_rank(ts_mean(anl4_ebit_flag, 20), 60)
   Sharpe: 0.00 | Fitness: 0.00 | Turnover: 0.0% | PnL: 📉 $0


   ⚠️  Score fetch failed: Expecting value: line 1 column 1 (char 0)
✅ PASS | group_rank(anl4_bvps_flag, subindustry)
   Sharpe: 1.27 | Fitness: 1.15 | Turnover: 2.1% | PnL: 📈 +$5.11M

✅ PASS | group_zscore(anl4_bvps_flag, subindustry)
   Sharpe: 1.38 | Fitness: 1.29 | Turnover: 2.1% | PnL: 📈 +$5.43M

❌ FAIL | ts_rank(anl4_bvps_flag, 60)
   Sharpe: -0.08 | Fitness: -0.02 | Turnover: 7.2% | PnL: 📉 -$529.9K

❌ FAIL | group_rank(ts_decay_linear(anl4_bvps_flag, 20), subindustry)
   Sharpe: 1.26 | Fitness: 0.83 | Turnover: 2.7% | PnL: 📈 +$2.68M

❌ FAIL | rank(ts_mean(anl4_bvps_flag, 5) - ts_mean(anl4_bvps_flag, 20))
   Sharpe: -0.27 | Fitness: -0.16 | Turnover: 17.6% | PnL: 📉 -$3.17M

❌ FAIL | ts_rank(ts_mean(anl4_bvps_flag, 20), 60)
   Sharpe: -0.04 | Fitness: -0.01 | Turnover: 5.7% | PnL: 📉 -$264.6K

❌ FAIL | rank(ts_delta(anl4_bvps_flag, 20))
   Sharpe: -0.26 | Fitness: -0.15 | Turnover: 17.6% | PnL: 📉 -$2.93M

   ⚠️  Score fetch failed: Expecting value: line 1 column 1 (char 0)
✅ PASS | group_rank(ts_mean(anl4_bvps_flag, 20), subindustry)
   Sharpe: 1.29 | Fitness: 1.18 | Turnover: 1.8% | PnL: 📈 +$5.18M

❌ FAIL | rank(anl4_bvps_flag) * rank(anl4_ebit_flag)
   Sharpe: 0.00 | Fitness: 0.00 | Turnover: 0.0% | PnL: 📉 $0

✅ PASS | group_zscore(ts_decay_linear(anl4_bvps_flag, 20), subindustry)
   Sharpe: 1.42 | Fitness: 1.17 | Turnover: 2.2% | PnL: 📈 +$4.21M

   ##############################

Testing alphas...

❌ FAIL | 0.5*group_zscore(anl4_bvps_flag, subindustry) - 0.5*rank(mdl53_jc5_1year)
   Sharpe: 0.88 | Fitness: 0.74 | Turnover: 2.6% | PnL: 📈 +$4.40M

❌ FAIL | 0.5*group_zscore(anl4_bvps_flag, subindustry) + 0.5*rank(mdl53_implied_ratings)
   Sharpe: 1.08 | Fitness: 0.88 | Turnover: 4.1% | PnL: 📈 +$4.10M

❌ FAIL | 0.5*group_rank(anl4_bvps_flag, subindustry) - 0.5*rank(mdl53_implied_spreads)
   Sharpe: 0.44 | Fitness: 0.29 | Turnover: 11.6% | PnL: 📈 +$2.60M

❌ FAIL | 0.5*group_rank(ts_mean(anl4_bvps_flag, 20), subindustry) - 0.5*rank(mdl53_jc5_1year)
   Sharpe: 0.49 | Fitness: 0.33 | Turnover: 3.2% | PnL: 📈 +$2.80M

❌ FAIL | -group_rank(mdl53_jc5_1year, subindustry)
   Sharpe: 0.04 | Fitness: 0.01 | Turnover: 3.8% | PnL: 📈 +$210.8K

❌ FAIL | -group_zscore(mdl53_implied_spreads, subindustry)
   Sharpe: -0.07 | Fitness: -0.02 | Turnover: 15.5% | PnL: 📉 -$444.0K

❌ FAIL | -group_rank(mdl53_jc5_5year, subindustry)
   Sharpe: 0.05 | Fitness: 0.01 | Turnover: 3.1% | PnL: 📈 +$219.7K

❌ FAIL | -group_rank(mdl53_jc5_5year - mdl53_jc5_1year, subindustry)
   Sharpe: 0.95 | Fitness: 0.59 | Turnover: 5.7% | PnL: 📈 +$2.39M

✅ PASS | 0.5*group_zscore(anl4_bvps_flag, subindustry) - 0.5*rank(mdl53_jc5_5year - mdl53_jc5_1year)
   Sharpe: 1.26 | Fitness: 1.16 | Turnover: 3.1% | PnL: 📈 +$5.22M failed because of Sub-universe Sharpe of 0.39 is below cutoff of 0.55.

❌ FAIL | -rank(ts_delta(mdl53_jc5_1year, 63))
   Sharpe: -0.28 | Fitness: -0.11 | Turnover: 11.1% | PnL: 📉 -$1.02M


Testing alphas...

❌ FAIL | rank(vec_avg(ern4_30div) - vec_avg(ern4_30dexerniv))
   Sharpe: 0.20 | Fitness: 0.04 | Turnover: 32.4% | PnL: 📈 +$603.1K

❌ FAIL | rank(vec_avg(ern4_90div) - vec_avg(ern4_90dexerniv))
   Sharpe: 0.78 | Fitness: 0.23 | Turnover: 39.7% | PnL: 📈 +$1.65M

❌ FAIL | rank(vec_avg(ern4_60div) - vec_avg(ern4_60dexerniv))
   Sharpe: 0.50 | Fitness: 0.12 | Turnover: 37.3% | PnL: 📈 +$1.09M

❌ FAIL | rank(ts_backfill(vec_avg(ern4_ernmv1), 5))
   Sharpe: -0.04 | Fitness: -0.00 | Turnover: 3.5% | PnL: 📉 -$65.8K

❌ FAIL | rank(vec_avg(ern4_fcsterneffct))
   Sharpe: 1.13 | Fitness: 0.87 | Turnover: 6.9% | PnL: 📈 +$3.67M

❌ FAIL | rank(vec_avg(ern4_erneffct1) - vec_avg(ern4_fcsterneffct))
   Sharpe: -0.67 | Fitness: -0.27 | Turnover: 9.4% | PnL: 📉 -$978.9K

❌ FAIL | rank(vec_avg(ern4_absavgernmv))
   Sharpe: 0.39 | Fitness: 0.23 | Turnover: 6.9% | PnL: 📈 +$2.07M

❌ FAIL | -rank(vec_avg(ern4_ernmvstdev))
   Sharpe: -0.48 | Fitness: -0.29 | Turnover: 6.8% | PnL: 📉 -$2.31M

❌ FAIL | rank(vec_avg(ern4_fairvol90d) - vec_avg(ern4_90div))
   Sharpe: -0.27 | Fitness: -0.06 | Turnover: 34.4% | PnL: 📉 -$720.2K

❌ FAIL | rank(ts_backfill(vec_avg(ern4_ernmv1), 5) - vec_avg(ern4_absavgernmv))
   Sharpe: -0.39 | Fitness: -0.15 | Turnover: 8.8% | PnL: 📉 -$950.3K


Testing alphas...

❌ FAIL | -rank(mdl53_jc5_1year)
   Sharpe: 0.08 | Fitness: 0.02 | Turnover: 2.5% | PnL: 📈 +$449.0K

❌ FAIL | -rank(mdl53_implied_spreads)
   Sharpe: -0.01 | Fitness: -0.00 | Turnover: 9.5% | PnL: 📉 -$43.4K

❌ FAIL | rank(mdl53_implied_ratings)
   Sharpe: 0.23 | Fitness: 0.06 | Turnover: 5.9% | PnL: 📈 +$391.7K

❌ FAIL | -rank(ts_delta(mdl53_jc5_1year, 21))
   Sharpe: -0.36 | Fitness: -0.15 | Turnover: 15.8% | PnL: 📉 -$1.39M

❌ FAIL | -rank(mdl53_jc5_5year - mdl53_jc5_1year)
   Sharpe: 0.96 | Fitness: 0.68 | Turnover: 4.0% | PnL: 📈 +$3.10M

❌ FAIL | -rank(ts_delta(mdl53_jc5_5year - mdl53_jc5_1year, 21))
   Sharpe: 0.10 | Fitness: 0.02 | Turnover: 16.8% | PnL: 📈 +$366.5K

❌ FAIL | -rank(mdl53_jc5_3month)
   Sharpe: 0.04 | Fitness: 0.01 | Turnover: 2.5% | PnL: 📈 +$238.0K

❌ FAIL | -rank(ts_mean(mdl53_implied_spreads, 20))
   Sharpe: -0.01 | Fitness: -0.00 | Turnover: 1.8% | PnL: 📉 -$58.9K

❌ FAIL | -group_rank(mdl53_jc5_1year, industry)
   Sharpe: 0.03 | Fitness: 0.00 | Turnover: 2.9% | PnL: 📈 +$148.0K

❌ FAIL | -rank(mdl53_jc6_1year)
   Sharpe: -0.03 | Fitness: -0.01 | Turnover: 2.5% | PnL: 📉 -$200.1K

## ###############################

Testing alphas...

❌ FAIL | group_rank(vec_avg(ern4_fcsterneffct), subindustry)
   Sharpe: 1.11 | Fitness: 0.69 | Turnover: 6.9% | PnL: 📈 +$2.36M

❌ FAIL | group_zscore(vec_avg(ern4_fcsterneffct), subindustry)
   Sharpe: 1.19 | Fitness: 0.82 | Turnover: 7.3% | PnL: 📈 +$2.92M

❌ FAIL | rank(mdl17_dynamicfocusrank)
   Sharpe: -0.09 | Fitness: -0.01 | Turnover: 41.4% | PnL: 📉 -$167.1K

❌ FAIL | group_rank(mdl17_dynamicfocusrank, subindustry)
   Sharpe: 0.01 | Fitness: 0.00 | Turnover: 41.4% | PnL: 📈 +$11.7K

❌ FAIL | group_zscore(mdl17_dynamicfocusrank, subindustry)
   Sharpe: -0.01 | Fitness: -0.00 | Turnover: 41.4% | PnL: 📉 -$22.6K

❌ FAIL | group_rank(mdl17_score, subindustry)
   Sharpe: -1.14 | Fitness: -0.25 | Turnover: 41.4% | PnL: 📉 -$997.5K

❌ FAIL | group_zscore(mdl17_score_equityfocusrank, subindustry)
   Sharpe: -0.54 | Fitness: -0.11 | Turnover: 41.4% | PnL: 📉 -$865.6K

❌ FAIL | -group_rank(mdl17_score_dtstsespe, subindustry)
   Sharpe: -0.82 | Fitness: -0.20 | Turnover: 41.4% | PnL: 📉 -$1.17M

❌ FAIL | group_rank(mdl17_score_netrec_pct, subindustry)
   Sharpe: 0.32 | Fitness: 0.03 | Turnover: 41.4% | PnL: 📈 +$232.3K

❌ FAIL | group_rank(mdl17_score_buyrec_pct, subindustry)
   Sharpe: 0.35 | Fitness: 0.04 | Turnover: 41.4% | PnL: 📈 +$253.9K


Testing alphas...

❌ FAIL | -rank(pcr_oi_270)
   Sharpe: -0.29 | Fitness: -0.09 | Turnover: 8.4% | PnL: 📉 -$588.1K

❌ FAIL | -rank(pcr_oi_180)
   Sharpe: -0.45 | Fitness: -0.17 | Turnover: 7.4% | PnL: 📉 -$911.9K

❌ FAIL | -rank(pcr_oi_90)
   Sharpe: -0.09 | Fitness: -0.02 | Turnover: 7.6% | PnL: 📉 -$216.1K

❌ FAIL | rank(unsystematic_risk_last_360_days)
   Sharpe: -0.08 | Fitness: -0.03 | Turnover: 13.3% | PnL: 📉 -$754.3K

❌ FAIL | rank(unsystematic_risk_last_90_days)
   Sharpe: -0.14 | Fitness: -0.06 | Turnover: 14.3% | PnL: 📉 -$1.19M

❌ FAIL | -rank(beta_last_60_days_spy)
   Sharpe: -0.08 | Fitness: -0.03 | Turnover: 13.4% | PnL: 📉 -$781.2K

❌ FAIL | -group_rank(pcr_oi_180, industry)
   Sharpe: -0.49 | Fitness: -0.20 | Turnover: 7.9% | PnL: 📉 -$984.0K

❌ FAIL | group_rank(unsystematic_risk_last_360_days, industry)
   Sharpe: 0.01 | Fitness: 0.00 | Turnover: 14.1% | PnL: 📈 +$75.2K

❌ FAIL | -rank(ts_delta(pcr_oi_180, 21))
   Sharpe: 0.31 | Fitness: 0.07 | Turnover: 14.2% | PnL: 📈 +$343.0K

❌ FAIL | rank(unsystematic_risk_last_90_days) - rank(beta_last_60_days_spy)
   Sharpe: -0.40 | Fitness: -0.19 | Turnover: 16.4% | PnL: 📉 -$1.86M

Testing alphas...

❌ FAIL | group_rank(analyst_revision_rank_derivative, subindustry)
   Sharpe: -0.87 | Fitness: -0.60 | Turnover: 2.2% | PnL: 📉 -$2.95M

❌ FAIL | group_zscore(analyst_revision_rank_derivative, subindustry)
   Sharpe: -0.93 | Fitness: -0.63 | Turnover: 8.6% | PnL: 📉 -$2.81M

❌ FAIL | group_rank(earnings_certainty_rank_derivative, subindustry)
   Sharpe: -0.86 | Fitness: -0.59 | Turnover: 2.2% | PnL: 📉 -$2.95M

❌ FAIL | group_zscore(earnings_certainty_rank_derivative, subindustry)
   Sharpe: -0.89 | Fitness: -0.59 | Turnover: 8.2% | PnL: 📉 -$2.73M

❌ FAIL | group_rank(composite_factor_score_derivative, subindustry)
   Sharpe: -0.89 | Fitness: -0.62 | Turnover: 2.2% | PnL: 📉 -$3.01M

❌ FAIL | group_zscore(composite_factor_score_derivative, subindustry)
   Sharpe: -0.94 | Fitness: -0.63 | Turnover: 9.3% | PnL: 📉 -$2.79M

❌ FAIL | group_rank(cashflow_efficiency_rank_derivative, subindustry)
   Sharpe: -0.86 | Fitness: -0.59 | Turnover: 2.2% | PnL: 📉 -$2.93M

❌ FAIL | group_zscore(cashflow_efficiency_rank_derivative, subindustry)
   Sharpe: -0.86 | Fitness: -0.56 | Turnover: 8.6% | PnL: 📉 -$2.63M

❌ FAIL | group_rank(growth_potential_rank_derivative, subindustry)
   Sharpe: -0.87 | Fitness: -0.60 | Turnover: 2.2% | PnL: 📉 -$2.98M

❌ FAIL | group_zscore(multi_factor_acceleration_score_derivative, subindustry)
   Sharpe: -0.94 | Fitness: -0.63 | Turnover: 9.3% | PnL: 📉 -$2.79M

## #######################