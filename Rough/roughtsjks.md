import wqb
import os
import asyncio
import time
from dotenv import load_dotenv
load_dotenv()

async def main():
    s = wqb.WQBSession((
        os.getenv("BRAIN_CREDENTIAL_EMAIL"),
        os.getenv("BRAIN_CREDENTIAL_PASSWORD")
    ))

    resp = s.auth_request()
    print(f"Login status: {resp.status_code}")
    time.sleep(3)

    settings = {
        "instrumentType": "EQUITY",
        "region": "USA",
        "universe": "TOP3000",
        "delay": 1,
        "decay": 0,
        "neutralization": "SUBINDUSTRY",
        "truncation": 0.08,
        "pasteurization": "OFF",
        "unitHandling": "VERIFY",
        "nanHandling": "OFF",
        "language": "FASTEXPR",
        "visualization": False,
    }

    alphas_to_test = [
     "anl4_adjusted_netincome_ft",
        "anl4_adjusted_eps_ft",
    "anl4_adjusted_eps_qt",
    "anl4_adjusted_netincome_qt",
    "anl4_revenue_ft",
    "anl4_revenue_qt",
    "anl4_ebitda_ft",
    "anl4_ebitda_qt",
    "anl4_dps_ft",
    "anl4_dps_qt",
    "anl4_capex_ft",
    "anl4_capex_qt",
    "anl4_fcf_ft",
    "anl4_fcf_qt",
    "anl4_ebit_ft",
    "anl4_ebit_qt",
    ]

    print("\nTesting alphas...\n")

    for expr in alphas_to_test:
        try:
            alpha = {
                "type": "REGULAR",
                "settings": settings,
                "regular": expr
            }
            resp = await s.simulate(alpha)
            result = resp.json()
            alpha_id = result.get("alpha")

            time.sleep(2)

            results_resp = s.get(f"https://api.worldquantbrain.com/alphas/{alpha_id}")
            results = results_resp.json()
            print(f"DEBUG: {results.get('is', {})}")

            sharpe = results.get("is", {}).get("sharpe", 0)
            fitness = results.get("is", {}).get("fitness", 0)
            turnover = results.get("is", {}).get("turnover", 0)

            if sharpe > 1.25 and fitness > 1.0:
                print(f"✅ PASS | {expr}")
                print(f"   Sharpe: {sharpe:.2f} | Fitness: {fitness:.2f} | Turnover: {turnover:.1%}")
            else:
                print(f"❌ FAIL | {expr} | Sharpe: {sharpe:.2f} | Fitness: {fitness:.2f}")

            time.sleep(2)

        except Exception as e:
            print(f"ERROR | {expr} | {e}")

    print("\nDone!")

asyncio.run(main())