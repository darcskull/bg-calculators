#!/bin/bash
# BG Calculators - Quick Rate Verification Script
# Opens official Bulgarian government sites for manual verification

echo "=========================================="
echo "BG Calculators - Rate Verification"
echo "=========================================="
echo ""
echo "Opening official sources for manual verification..."
echo ""

# Check OS and open browser accordingly
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    # Linux
    xdg-open "https://nap.bg/" &
    xdg-open "https://www.noi.bg/" &
    xdg-open "https://www.minfin.bg/" &
elif [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS
    open "https://nap.bg/"
    open "https://www.noi.bg/"
    open "https://www.minfin.bg/"
elif [[ "$OSTYPE" == "msys" ]] || [[ "$OSTYPE" == "win32" ]]; then
    # Windows
    start "https://nap.bg/"
    start "https://www.noi.bg/"
    start "https://www.minfin.bg/"
else
    echo "Unsupported OS. Please manually visit:"
    echo "https://nap.bg/"
    echo "https://www.noi.bg/"
    echo "https://www.minfin.bg/"
fi

echo ""
echo "=========================================="
echo "CHECKLIST FOR VERIFICATION:"
echo "=========================================="
echo ""
echo "1. НАП (nap.bg):"
echo "   [ ] Minimum insurance threshold for 2026"
echo "   [ ] Maximum insurance threshold for 2026"
echo "   [ ] Income tax rate (should be 10%)"
echo ""
echo "2. НОИ (noi.bg):"
echo "   [ ] Employee insurance rates (should be 3.9% total)"
echo "   [ ] Employer insurance rates"
echo ""
echo "3. Ministry of Finance (minfin.bg):"
echo "   [ ] VAT rates (should be 20% standard, 9% reduced)"
echo ""
echo "4. Municipal websites (for waste tax):"
echo "   [ ] Sofia municipality - waste tax"
echo "   [ ] Plovdiv municipality - waste tax"
echo "   [ ] Varna municipality - waste tax"
echo "   [ ] Other municipalities as needed"
echo ""
echo "5. Ministry of Labour:"
echo "   [ ] Child benefits amounts"
echo ""
echo "=========================================="
echo "After verification, update js/rates.js"
echo "=========================================="
