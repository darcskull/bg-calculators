/**
 * Load rates maintained in the repository's rates.json file.
 * There is intentionally no fallback: stale hard-coded rates could produce
 * misleading financial results when the data file fails to load.
 */

let RATES = null;
let ratesPromise = null;

function loadRates() {
    if (!ratesPromise) {
        const scriptUrl = document.currentScript && document.currentScript.src;
        const ratesUrl = new URL('../rates.json', scriptUrl || window.location.href);
        ratesPromise = fetch(ratesUrl)
            .then(response => {
                if (!response.ok) {
                    throw new Error(`Could not load rates.json (${response.status})`);
                }
                return response.json();
            })
            .then(rates => {
                RATES = rates;
                return RATES;
            });
    }
    return ratesPromise;
}
