import wqb
import os
import asyncio
import time
import csv
from itertools import product
from datetime import datetime
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from dotenv import load_dotenv
load_dotenv()

# ─────────────────────────────────────────
# OUTPUT FILES
# ─────────────────────────────────────────
RESULTS_FILE = "grid_results.csv"
PASS_FILE    = "grid_SUBMIT_THESE.csv"

# ─────────────────────────────────────────
# GRID
# ─────────────────────────────────────────
UNIVERSES       = ["TOP3000", "TOP500"]
NEUTRALIZATIONS = ["SUBINDUSTRY", "MARKET"]
DECAYS          = [0, 5]
TRUNCATIONS     = [0.08, 0.04]

# ─────────────────────────────────────────
# ALPHA LIST
# ─────────────────────────────────────────
ALPHAS = [
    # NEWS + RISK
    "0.5*rank(ts_mean(news_mins_10_pct_dn,15)) + 0.5*ts_zscore(unsystematic_risk_last_360_days,60)",
    "0.4*rank(ts_mean(news_mins_10_pct_dn,20)) + 0.6*ts_zscore(unsystematic_risk_last_90_days,60)",
    "0.6*rank(ts_mean(news_mins_10_pct_dn,10)) + 0.4*ts_quantile(unsystematic_risk_last_360_days,60)",
    "0.5*rank(ts_mean(news_atr14,10)) + 0.5*ts_zscore(unsystematic_risk_last_360_days,60)",
    "0.5*rank(ts_mean(news_tot_ticks,10)) + 0.5*ts_zscore(unsystematic_risk_last_360_days,60)",
    "0.5*rank(ts_mean(news_mov_vol,10)) + 0.5*ts_zscore(unsystematic_risk_last_360_days,60)",
    # NEWS + OPTIONS
    "0.5*rank(ts_mean(news_mins_10_pct_dn,15)) + 0.5*rank(pcr_oi_270)",
    "0.4*rank(ts_mean(news_mins_10_pct_dn,20)) + 0.6*rank(best_fit_implied_announcement_effect)",
    "0.5*rank(ts_mean(news_mins_10_pct_dn,15)) + 0.5*rank(pcr_oi_180)",
    "0.5*rank(ts_mean(news_atr14,10)) + 0.5*rank(pcr_oi_270)",
    "0.5*rank(ts_mean(news_tot_ticks,10)) + 0.5*rank(pcr_oi_270)",
    "0.4*rank(ts_mean(news_mins_10_pct_dn,15)) + 0.6*zscore(aggregate_option_open_interest)",
    "0.5*rank(ts_mean(news_mins_10_pct_dn,15)) + 0.5*rank(forecasted_put_call_slope)",
    "0.4*rank(ts_mean(news_atr14,15)) + 0.6*rank(best_fit_implied_announcement_effect)",
    # NEWS + FUNDAMENTAL
    "0.5*rank(ts_mean(news_mins_10_pct_dn,15)) + 0.5*zscore(anl4_fcf_flag)",
    "0.4*rank(ts_mean(news_mins_10_pct_dn,15)) + 0.6*zscore(anl4_cfo_flag)",
    "0.5*rank(ts_mean(news_mins_10_pct_dn,15)) + 0.5*zscore(anl4_ebitda_flag)",
    "0.5*rank(ts_mean(news_mins_10_pct_dn,15)) + 0.5*zscore(anl4_netdebt_flag)",
    "0.5*rank(ts_mean(news_mins_10_pct_dn,15)) + 0.5*rank(deferred_tax_assets_net_value)",
    "0.4*rank(ts_mean(news_atr14,10)) + 0.6*zscore(anl4_fcf_flag)",
    "0.4*rank(ts_mean(news_tot_ticks,10)) + 0.6*zscore(anl4_cfo_flag)",
    # NEWS + SENTIMENT
    "0.5*rank(ts_mean(news_mins_10_pct_dn,15)) + 0.5*zscore(snt_buzz)",
    "0.5*rank(ts_mean(news_atr14,10)) + 0.5*zscore(snt_buzz)",
    "0.4*rank(ts_mean(news_mins_10_pct_dn,15)) + 0.6*zscore(snt_buzz_ret)",
    # RISK + OPTIONS
    "0.5*ts_zscore(unsystematic_risk_last_360_days,60) + 0.5*rank(pcr_oi_270)",
    "0.5*ts_zscore(unsystematic_risk_last_360_days,60) + 0.5*rank(best_fit_implied_announcement_effect)",
    "0.4*ts_zscore(unsystematic_risk_last_360_days,60) + 0.6*rank(pcr_oi_180)",
    "0.5*ts_quantile(unsystematic_risk_last_360_days,60) + 0.5*rank(forecasted_put_call_slope)",
    "0.5*ts_zscore(unsystematic_risk_last_90_days,60) + 0.5*rank(pcr_oi_270)",
    "0.4*ts_zscore(unsystematic_risk_last_360_days,60) + 0.6*zscore(aggregate_option_open_interest)",
    # RISK + FUNDAMENTAL
    "0.5*ts_zscore(unsystematic_risk_last_360_days,60) + 0.5*zscore(anl4_fcf_flag)",
    "0.5*ts_zscore(unsystematic_risk_last_360_days,60) + 0.5*zscore(anl4_netdebt_flag)",
    "0.5*ts_zscore(unsystematic_risk_last_360_days,60) + 0.5*zscore(anl4_cfo_flag)",
    "0.5*ts_zscore(unsystematic_risk_last_360_days,60) + 0.5*rank(deferred_tax_assets_net_value)",
    "0.4*ts_zscore(unsystematic_risk_last_90_days,60) + 0.6*zscore(anl4_ebitda_flag)",
    "0.5*ts_quantile(unsystematic_risk_last_360_days,60) + 0.5*zscore(anl4_fcf_flag)",
    # OPTIONS + FUNDAMENTAL
    "0.5*rank(pcr_oi_270) + 0.5*zscore(anl4_fcf_flag)",
    "0.5*rank(pcr_oi_270) + 0.5*zscore(anl4_cfo_flag)",
    "0.5*rank(pcr_oi_180) + 0.5*zscore(anl4_netdebt_flag)",
    "0.4*rank(best_fit_implied_announcement_effect) + 0.6*zscore(anl4_fcf_flag)",
    "0.4*rank(best_fit_implied_announcement_effect) + 0.6*zscore(anl4_netdebt_flag)",
    "0.5*rank(pcr_oi_270) + 0.5*rank(deferred_tax_assets_net_value)",
    "0.5*rank(forecasted_put_call_slope) + 0.5*zscore(anl4_cfo_flag)",
    # mdl177 + NEWS
    "0.3*rank(ts_mean(news_mins_10_pct_dn,15)) + 0.7*rank(mdl177_garpanalystmodel_qgp_relvalue)",
    "0.3*rank(ts_mean(news_mins_10_pct_dn,15)) + 0.7*rank(mdl177_garpanalystmodel_qgp_relmomentum)",
    "0.3*rank(ts_mean(news_atr14,10)) + 0.7*rank(mdl177_garpanalystmodel_qgp_relvalue)",
    "0.3*rank(ts_mean(news_tot_ticks,10)) + 0.7*rank(mdl177_garpanalystmodel_qgp_relmomentum)",
    # mdl177 + RISK
    "0.5*rank(mdl177_garpanalystmodel_qgp_relvalue) + 0.5*ts_zscore(unsystematic_risk_last_360_days,60)",
    "0.5*rank(mdl177_garpanalystmodel_qgp_relmomentum) + 0.5*ts_zscore(unsystematic_risk_last_360_days,60)",
    "0.5*rank(mdl177_garpanalystmodel_qgp_relvalue) + 0.5*ts_quantile(unsystematic_risk_last_360_days,60)",
    # mdl177 + OPTIONS
    "0.5*rank(mdl177_garpanalystmodel_qgp_relvalue) + 0.5*rank(pcr_oi_270)",
    "0.5*rank(mdl177_garpanalystmodel_qgp_relmomentum) + 0.5*rank(pcr_oi_270)",
    "0.5*rank(mdl177_garpanalystmodel_qgp_relvalue) + 0.5*rank(best_fit_implied_announcement_effect)",
    # mdl177 + FUNDAMENTAL
    "0.5*rank(mdl177_garpanalystmodel_qgp_relvalue) + 0.5*zscore(anl4_fcf_flag)",
    "0.5*rank(mdl177_garpanalystmodel_qgp_relmomentum) + 0.5*zscore(anl4_cfo_flag)",
    "0.5*rank(mdl177_garpanalystmodel_qgp_relvalue) + 0.5*zscore(anl4_netdebt_flag)",
    # TRIPLES
    "0.33*rank(ts_mean(news_mins_10_pct_dn,15)) + 0.33*rank(pcr_oi_270) + 0.34*ts_zscore(unsystematic_risk_last_360_days,60)",
    "0.33*rank(mdl177_garpanalystmodel_qgp_relvalue) + 0.33*rank(pcr_oi_270) + 0.34*zscore(anl4_fcf_flag)",
    "0.33*rank(ts_mean(news_mins_10_pct_dn,15)) + 0.33*zscore(anl4_cfo_flag) + 0.34*ts_zscore(unsystematic_risk_last_360_days,60)",
    "0.33*rank(mdl177_garpanalystmodel_qgp_relmomentum) + 0.33*rank(best_fit_implied_announcement_effect) + 0.34*zscore(anl4_netdebt_flag)",
    # QUAD
    "0.25*rank(ts_mean(news_mins_10_pct_dn,15)) + 0.25*rank(pcr_oi_270) + 0.25*zscore(anl4_fcf_flag) + 0.25*ts_zscore(unsystematic_risk_last_360_days,60)",
]

ALL_COMBOS = list(product(ALPHAS, UNIVERSES, NEUTRALIZATIONS, DECAYS, TRUNCATIONS))

# ─────────────────────────────────────────
# CSV SETUP
# ─────────────────────────────────────────
def init_csv():
    headers = ["timestamp","expr","universe","neutralization","decay",
               "truncation","sharpe","fitness","turnover","self_corr",
               "failed_checks","grade","alpha_id"]
    with open(RESULTS_FILE, "w", newline="") as f:
        csv.writer(f).writerow(headers)
    with open(PASS_FILE, "w", newline="") as f:
        csv.writer(f).writerow(headers)

def log_result(expr, universe, neutralization, decay, truncation,
               sharpe, fitness, turnover, self_corr, failed_checks, grade, alpha_id):
    ts = datetime.now().strftime("%H:%M:%S")
    row = [ts, expr, universe, neutralization, decay, truncation,
           round(sharpe,3), round(fitness,3), round(turnover,4),
           self_corr, failed_checks, grade, alpha_id]
    with open(RESULTS_FILE, "a", newline="") as f:
        csv.writer(f).writerow(row)
    if grade in ("EXCELLENT", "GOOD"):
        with open(PASS_FILE, "a", newline="") as f:
            csv.writer(f).writerow(row)

# ─────────────────────────────────────────
# GRADE — shows exactly which check failed
# ─────────────────────────────────────────
def grade_alpha(sharpe, fitness, turnover, checks):
    for c in checks:
        name   = c.get("name", "")
        result = c.get("result", "")
        if result == "FAIL" and name != "SELF_CORRELATION":
            return "FAIL"
    if sharpe < 1.25 or fitness < 1.0:
        return "FAIL"
    if turnover < 0.01 or turnover > 0.70:
        return "FAIL_TURNOVER"
    for c in checks:
        if c.get("name") == "SELF_CORRELATION":
            val = c.get("value")
            if isinstance(val, (int, float)) and val >= 0.70:
                return "FAIL_CORR"
    if sharpe >= 2.25 and fitness >= 1.80:
        return "EXCELLENT"
    if sharpe >= 1.25 and fitness >= 1.0:
        return "GOOD"
    return "FAIL"

def get_failed_checks(checks):
    failed = [c["name"] for c in checks if c.get("result") == "FAIL"]
    return ", ".join(failed) if failed else "none"

# ─────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────
async def main():
    s = wqb.WQBSession((
        os.getenv("BRAIN_CREDENTIAL_EMAIL"),
        os.getenv("BRAIN_CREDENTIAL_PASSWORD")
    ))
    retry_strategy = Retry(total=3, backoff_factor=2)
    adapter = HTTPAdapter(max_retries=retry_strategy)
    s.mount("https://", adapter)
    s.mount("http://", adapter)

    resp = s.auth_request()
    print(f"Login status: {resp.status_code}")
    time.sleep(10)

    init_csv()

    total  = len(ALL_COMBOS)
    done   = 0
    passed = 0

    print(f"\nTotal combos to test: {total}")
    print(f"  {len(ALPHAS)} alphas x {len(UNIVERSES)} universes x {len(NEUTRALIZATIONS)} neutralizations x {len(DECAYS)} decays x {len(TRUNCATIONS)} truncations")
    print(f"\nResults  → {RESULTS_FILE}")
    print(f"Passes   → {PASS_FILE}\n")
    print("=" * 100)

    for expr, universe, neutralization, decay, truncation in ALL_COMBOS:
        done += 1
        tag = f"U={universe:<8} N={neutralization:<12} D={decay} T={truncation}"

        settings = {
            "instrumentType": "EQUITY",
            "region":         "USA",
            "universe":       universe,
            "delay":          1,
            "decay":          decay,
            "neutralization": neutralization,
            "truncation":     truncation,
            "pasteurization": "OFF",
            "unitHandling":   "VERIFY",
            "nanHandling":    "OFF",
            "language":       "FASTEXPR",
            "visualization":  False,
        }

        try:
            alpha_payload = {"type": "REGULAR", "settings": settings, "regular": expr}
            resp = await s.simulate(alpha_payload)
            result = resp.json()
            alpha_id = result.get("alpha", "N/A")
            time.sleep(8)

            results_resp = s.get(f"https://api.worldquantbrain.com/alphas/{alpha_id}")
            results = results_resp.json()

            is_data  = results.get("is", {})
            sharpe   = is_data.get("sharpe",   0) or 0
            fitness  = is_data.get("fitness",  0) or 0
            turnover = is_data.get("turnover", 0) or 0
            checks   = is_data.get("checks",   [])

            self_corr     = "N/A"
            for c in checks:
                if c.get("name") == "SELF_CORRELATION":
                    self_corr = c.get("value", "PENDING")

            failed_checks = get_failed_checks(checks)
            grade         = grade_alpha(sharpe, fitness, turnover, checks)

            # Full expression always shown
            if grade == "EXCELLENT":
                passed += 1
                print(f"\n[{done}/{total}] ✅✅ EXCELLENT | {tag}")
                print(f"   Sharpe:{sharpe:.2f} | Fitness:{fitness:.2f} | Turnover:{turnover:.1%} | Corr:{self_corr}")
                print(f"   Alpha: {expr}")

            elif grade == "GOOD":
                passed += 1
                print(f"\n[{done}/{total}] ✅  GOOD      | {tag}")
                print(f"   Sharpe:{sharpe:.2f} | Fitness:{fitness:.2f} | Turnover:{turnover:.1%} | Corr:{self_corr}")
                print(f"   Alpha: {expr}")

            elif grade == "FAIL_CORR":
                print(f"[{done}/{total}] 🔴 CORR_FAIL | {tag} | Corr:{self_corr} | S:{sharpe:.2f} F:{fitness:.2f}")
                print(f"   Alpha: {expr}")

            elif grade == "FAIL_TURNOVER":
                print(f"[{done}/{total}] ⚠️  TO_FAIL   | {tag} | TO:{turnover:.1%} | S:{sharpe:.2f} F:{fitness:.2f}")
                print(f"   Alpha: {expr}")

            else:
                # Show exactly which checks failed
                print(f"[{done}/{total}] ❌ FAIL      | {tag} | S:{sharpe:.2f} F:{fitness:.2f} | FAILED:[{failed_checks}]")
                print(f"   Alpha: {expr}")

            log_result(expr, universe, neutralization, decay, truncation,
                       sharpe, fitness, turnover, self_corr, failed_checks, grade, alpha_id)

        except Exception as e:
            print(f"[{done}/{total}] ERROR | {tag} | {e}")
            print(f"   Alpha: {expr}")
            log_result(expr, universe, neutralization, decay, truncation,
                       0, 0, 0, "ERROR", "ERROR", "ERROR", "N/A")
            time.sleep(5)

        time.sleep(3)

    print("\n" + "=" * 100)
    print(f"DONE. Tested: {total} | Passed (GOOD + EXCELLENT): {passed}")
    print(f"Submission candidates saved to: {PASS_FILE}")

asyncio.run(main())