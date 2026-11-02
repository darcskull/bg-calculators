/** Shared formatting and validation helpers for the calculators. */

function formatEUR(amount, decimals = 2) {
    if (!Number.isFinite(amount)) return '—';
    return new Intl.NumberFormat('bg-BG', {
        style: 'currency',
        currency: 'EUR',
        minimumFractionDigits: decimals,
        maximumFractionDigits: decimals
    }).format(amount);
}

function formatPercent(value) {
    if (!Number.isFinite(value)) return '—';
    return `${(value * 100).toLocaleString('bg-BG', { maximumFractionDigits: 2 })}%`;
}

function isValidNumber(value) {
    if (typeof value === 'string' && value.trim() === '') return false;
    const number = Number(value);
    return Number.isFinite(number) && number >= 0;
}

function showError(elementId, message) {
    const errorElement = document.getElementById(elementId);
    if (errorElement) {
        errorElement.textContent = message;
        errorElement.style.display = 'block';
    }
}

function hideError(elementId) {
    const errorElement = document.getElementById(elementId);
    if (errorElement) errorElement.style.display = 'none';
}

function clamp(value, minimum, maximum) {
    return Math.min(Math.max(value, minimum), maximum);
}

function roundTo(value, decimals = 2) {
    const factor = 10 ** decimals;
    return Math.round((value + Number.EPSILON) * factor) / factor;
}
