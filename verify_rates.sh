#!/usr/bin/env sh
# Open official sources for manual verification; this script does not edit rates.

open_url() {
    if command -v xdg-open >/dev/null 2>&1; then
        xdg-open "$1" >/dev/null 2>&1 &
    elif command -v open >/dev/null 2>&1; then
        open "$1"
    else
        printf '%s\n' "$1"
    fi
}

open_url "https://nra.bg/wps/wcm/connect/agency/site/zakonodatelstvo/osiguryavane/stanovishta.ukazaniya.naruchnici/a10b7cdf-bc6b-4983-b604-1b7b593eb378"
open_url "https://www.nssi.bg/dohod01082026/"
open_url "https://www.nra.bg/wps/wcm/connect/nra.bg25863/agency/site/taxes/danak-vurhu-dohodite-na-fizicheski-lica/naem/"
open_url "https://nra.bg/wps/portal/nra/taxes/dds-v-balgariya/"

printf '%s\n' "Review all values in rates.json; the script does not verify or change them."
printf '%s\n' "Run python check_rates_simple.py for the manual checklist."
