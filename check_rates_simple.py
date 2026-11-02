#!/usr/bin/env python3
"""Print a manual review checklist for the values used by BG Calculators.

This script does not fetch sources, verify legislation, or edit rates.json.
It uses only Python's standard library.
"""

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent
RATES_FILE = ROOT / "rates.json"


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    with RATES_FILE.open(encoding="utf-8") as source_file:
        rates = json.load(source_file)

    metadata = rates["metadata"]
    print("BG Calculators — manual rate review")
    print(f"Last updated: {metadata.get('lastUpdated', 'not set')}")
    print(f"Last verified: {metadata.get('lastVerified', 'not verified')}")
    print("\nValues used by the calculators:")
    print(f"- Employee contribution (typical employment case): {rates['insurance']['employeeRate']:.2%}")
    period_labels = {
        "throughJuly2026": "through 31 July 2026",
        "fromAugust2026": "from 1 August 2026"
    }
    for period, amount in rates["insurance"]["maximumThreshold"].items():
        print(f"- Maximum insurance income ({period_labels.get(period, period)}): {amount:.2f} EUR")
    print(f"- Income tax: {rates['incomeTax']['rate']:.2%}")
    print(f"- VAT standard / reduced / zero: {rates['vat']['standard']:.0%} / {rates['vat']['reduced']:.0%} / {rates['vat']['zero']:.0%}")
    print(f"- Rental income tax: {rates['rentalTax']['rate']:.0%}")
    print(f"- Rental recognized expenses: {rates['rentalTax']['recognizedExpensesPercent']:.0%}")

    print("\nManual checks before changing lastVerified:")
    print("[ ] НАП: income tax, rental income expenses, tax deadlines, VAT rates and eligible categories")
    print("[ ] НАП: 2026 employee contribution table for standard employment")
    print("[ ] НОИ: maximum insurance income by period and minimum thresholds by activity/qualification")
    print("[ ] Municipality: waste fee, if a future calculator adds it")
    print("[ ] Update rates.json sources and dates only after checking each value against the official source")

    print("\nOfficial sources:")
    for name, url in metadata.get("sources", {}).items():
        print(f"- {name}: {url}")


if __name__ == "__main__":
    main()
