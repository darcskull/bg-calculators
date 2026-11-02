/**
 * Load rates from rates.json
 * This file loads the rates from the JSON file and makes them available globally
 */

let RATES = {};

// Function to load rates from JSON
async function loadRates() {
    try {
        const response = await fetch('../rates.json');
        if (!response.ok) {
            throw new Error('Failed to load rates.json');
        }
        RATES = await response.json();
        console.log('Rates loaded successfully:', RATES.metadata);
        return RATES;
    } catch (error) {
        console.error('Error loading rates:', error);
        // Fallback to default rates if JSON fails to load
        RATES = {
            metadata: {
                lastUpdated: 'ERROR',
                lastVerified: 'ERROR',
                currency: 'EUR',
                exchangeRate: 1.95583
            },
            insurance: {
                employee: {
                    pension: 0.022,
                    unemployment: 0.015,
                    general: 0.015,
                    total: 0.039
                },
                employer: {
                    pension: 0.074,
                    unemployment: 0.01,
                    accidents: 0.04,
                    general: 0.015,
                    total: 0.139
                },
                minimumThreshold: 475,
                maximumThreshold: 1918
            },
            incomeTax: {
                rate: 0.10,
                nonTaxableMinimum: 0
            },
            vat: {
                standard: 0.20,
                reduced: 0.09
            },
            propertyTax: {
                baseRate: 0.0015,
                wasteTax: {
                    Sofia: 31,
                    Plovdiv: 25,
                    Varna: 28,
                    Burgas: 26,
                    Ruse: 23,
                    StaraZagora: 21,
                    Pleven: 20,
                    Dobrich: 19,
                    Sliven: 18,
                    Shumen: 19
                }
            },
            rentalTax: {
                rate: 0.10,
                maxDeductiblePercent: 0.25,
                allowActualExpenses: true
            },
            selfEmployed: {
                minimumIncome: 475,
                pension: true,
                unemployment: false,
                general: true
            }
        };
        console.warn('Using fallback rates');
        return RATES;
    }
}

// Load rates immediately
loadRates();
