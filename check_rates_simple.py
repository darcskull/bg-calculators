#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BG Calculators - Simple Rate Checker
Generates a report with current rates and verification checklist.
No external dependencies required - uses only standard library.

Usage:
    python check_rates_simple.py
"""

import sys
import io
import json
from datetime import datetime

# Fix UTF-8 encoding for Windows
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def load_rates():
    """Load current rates from rates.json"""
    try:
        with open('rates.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print("rates.json not found. Using default values.")
        return None
    except json.JSONDecodeError:
        print("Error reading rates.json. Using default values.")
        return None

def save_rates(rates):
    """Save rates to rates.json"""
    with open('rates.json', 'w', encoding='utf-8') as f:
        json.dump(rates, f, indent=2, ensure_ascii=False)
    print("Rates saved to rates.json")

def generate_report(rates):
    """Generate a rate verification report"""

    if rates:
        min_threshold = rates['insurance']['minimumThreshold']
        max_threshold = rates['insurance']['maximumThreshold']
        waste_tax = rates['propertyTax']['wasteTax']
        last_verified = rates['metadata']['lastVerified']
    else:
        min_threshold = 475
        max_threshold = 1918
        waste_tax = {
            'Sofia': 31, 'Plovdiv': 25, 'Varna': 28, 'Burgas': 26,
            'Ruse': 23, 'StaraZagora': 21, 'Pleven': 20,
            'Dobrich': 19, 'Sliven': 18, 'Shumen': 19
        }
        last_verified = "NEVER"

    report = f"""
{'=' * 60}
BG Calculators - Rate Verification Report
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
{'=' * 60}

CURRENT RATES (EUR):
-------------------
Insurance Rates:
  - Employee total: 3.9% (pension 2.2% + unemployment 1.5% + general 1.5%)
  - Employer total: ~13.9% (excluding accidents which vary)
  - Minimum threshold: {min_threshold} € (NEEDS VERIFICATION)
  - Maximum threshold: {max_threshold} € (NEEDS VERIFICATION)
  - Last verified: {last_verified}

Income Tax:
  - Flat rate: 10% (NEEDS VERIFICATION)

VAT:
  - Standard rate: 20%
  - Reduced rate: 9%

Rental Income Tax:
  - Rate: 10% of net income
  - Max deductible expenses: 25% of gross rent

Waste Tax (Yearly - NEEDS VERIFICATION):
  - Sofia: {waste_tax.get('Sofia', 31)} €
  - Plovdiv: {waste_tax.get('Plovdiv', 25)} €
  - Varna: {waste_tax.get('Varna', 28)} €
  - Burgas: {waste_tax.get('Burgas', 26)} €
  - Ruse: {waste_tax.get('Ruse', 23)} €
  - Stara Zagora: {waste_tax.get('StaraZagora', 21)} €
  - Pleven: {waste_tax.get('Pleven', 20)} €
  - Dobrich: {waste_tax.get('Dobrich', 19)} €
  - Sliven: {waste_tax.get('Sliven', 18)} €
  - Shumen: {waste_tax.get('Shumen', 19)} €

{'=' * 60}
VERIFICATION CHECKLIST:
{'=' * 60}

REQUIRED CHECKS (Monthly):
--------------------------
[ ] Check НАП (https://nap.bg/) for:
    - Minimum insurance threshold for 2026
    - Maximum insurance threshold for 2026
    - Income tax rate confirmation

[ ] Check НОИ (https://www.noi.bg/) for:
    - Employee insurance rates
    - Employer insurance rates

[ ] Check Ministry of Finance (https://www.minfin.bg/) for:
    - VAT rates (should be 20% and 9%)

[ ] Check municipal websites for waste tax:
    - Sofia: https://sofia.bg/
    - Plovdiv: https://plovdiv.bg/
    - Varna: https://varna.bg/
    - And other municipalities as needed

[ ] Check Ministry of Labour for child benefits (if applicable)

{'=' * 60}
MANUAL UPDATE OPTION:
{'=' * 60}

To manually update rates in rates.json:
1. Open rates.json in a text editor
2. Update the values as needed
3. Save the file
4. The website will automatically use the new values

Or use this script with interactive mode (future feature).

{'=' * 60}
AFTER VERIFICATION:
{'=' * 60}

1. If any rates have changed, update rates.json
2. Update the 'lastVerified' date in rates.json metadata
3. Test the calculators with new rates
4. Commit and push changes to GitHub

{'=' * 60}
QUICK REFERENCE:
{'=' * 60}

Exchange Rate: 1 EUR = 1.95583 BGN (fixed)
Bulgaria adopted Euro: January 1, 2025

Official Sources:
- НАП: https://nap.bg/
- НОИ: https://www.noi.bg/
- Ministry of Finance: https://www.minfin.bg/
- Ministry of Labour: https://mlsp.government.bg/

{'=' * 60}
"""

    return report

def main():
    # Load current rates
    rates = load_rates()

    # Update metadata
    if rates:
        rates['metadata']['lastUpdated'] = datetime.now().strftime('%Y-%m-%d')
        save_rates(rates)

    # Generate and print report
    print(generate_report(rates))

    # Save report to file
    filename = f"rate_check_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(generate_report(rates))

    print(f"\nReport saved to: {filename}")
    print("\nNext steps:")
    print("1. Review the report")
    print("2. Open the official websites listed above")
    print("3. Verify the rates manually")
    print("4. If rates changed, update rates.json")
    print("5. Update the 'lastVerified' date in rates.json metadata")
    print("6. The website will automatically use the updated rates")

if __name__ == "__main__":
    main()
