@echo off
set "PROJECT_ROOT=%~dp0..\.."
echo BG Calculators - manual official source review
echo.
start "" "https://nra.bg/wps/wcm/connect/agency/site/zakonodatelstvo/osiguryavane/stanovishta.ukazaniya.naruchnici/a10b7cdf-bc6b-4983-b604-1b7b593eb378"
start "" "https://www.nssi.bg/dohod01082026/"
start "" "https://www.nra.bg/wps/wcm/connect/nra.bg25863/agency/site/taxes/danak-vurhu-dohodite-na-fizicheski-lica/naem/"
start "" "https://nra.bg/wps/portal/nra/taxes/dds-v-balgariya/"
echo.
echo Review every value in rates.json before changing metadata.lastVerified.
echo See tools\python\check_rates_simple.py for the value checklist.
python "%PROJECT_ROOT%\tools\python\check_rates_simple.py"
pause
