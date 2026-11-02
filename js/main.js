/**
 * Common utility functions for calculators
 */

/**
 * Format number as Euro (EUR)
 * @param {number} amount - Amount to format
 * @param {number} decimals - Number of decimal places (default: 2)
 * @returns {string} Formatted EUR amount
 */
function formatEUR(amount, decimals = 2) {
    if (isNaN(amount)) return '0.00 €';
    return amount.toFixed(decimals).replace('.', ',') + ' €';
}

// Keep formatBGN for backward compatibility (deprecated)
function formatBGN(amount, decimals = 2) {
    return formatEUR(amount, decimals);
}

/**
 * Format number as percentage
 * @param {number} value - Decimal value (e.g., 0.10 for 10%)
 * @returns {string} Formatted percentage
 */
function formatPercent(value) {
    if (isNaN(value)) return '0%';
    return (value * 100).toFixed(2) + '%';
}

/**
 * Validate if input is a positive number
 * @param {string|number} value - Input value
 * @returns {boolean} True if valid
 */
function isValidNumber(value) {
    const num = parseFloat(value);
    return !isNaN(num) && num >= 0;
}

/**
 * Show error message
 * @param {string} elementId - ID of error element
 * @param {string} message - Error message
 */
function showError(elementId, message) {
    const errorEl = document.getElementById(elementId);
    if (errorEl) {
        errorEl.textContent = message;
        errorEl.style.display = 'block';
    }
}

/**
 * Hide error message
 * @param {string} elementId - ID of error element
 */
function hideError(elementId) {
    const errorEl = document.getElementById(elementId);
    if (errorEl) {
        errorEl.style.display = 'none';
    }
}

/**
 * Clamp value between min and max
 * @param {number} value - Value to clamp
 * @param {number} min - Minimum value
 * @param {number} max - Maximum value
 * @returns {number} Clamped value
 */
function clamp(value, min, max) {
    return Math.min(Math.max(value, min), max);
}

/**
 * Round to decimal places
 * @param {number} value - Value to round
 * @param {number} decimals - Decimal places
 * @returns {number} Rounded value
 */
function roundTo(value, decimals = 2) {
    const factor = Math.pow(10, decimals);
    return Math.round(value * factor) / factor;
}
