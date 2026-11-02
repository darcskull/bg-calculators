# BG Calculators

Безплатен статичен сайт с калкулатори за българския пазар. Използва HTML, CSS и vanilla JavaScript; няма бекенд, база данни или външни runtime библиотеки.

Всички резултати са ориентировъчни и може да са непълни или остарели. Те не представляват професионален съвет. Преди решение или плащане проверявайте конкретния случай с компетентен специалист и официален източник.

## Калкулатори

- **Нетна заплата** — опростен стандартен трудов договор.
- **ДДС** — добавяне, извличане от крайна сума с включен ДДС или изчисляване само на размера на ДДС.
- **Доход от наем** — опростен данъчен случай за физическо лице.

## Структура

```text
bg-calculators/
├── index.html
├── calculators/
│   ├── net-salary.html
│   ├── vat-calculator.html
│   ├── rent-tax-calculator.html
├── css/style.css
├── js/main.js
├── js/rates_loader.js
├── rates.json
├── tools/python/
│   ├── check_rates_simple.py
│   ├── verify_rates.bat
│   └── verify_rates.sh
├── robots.txt
└── sitemap.xml
```

## Локално преглеждане

От корена на проекта стартирай:

```bash
python -m http.server 8000
```

Отвори `http://localhost:8000/`, за да може браузърът да зареди `rates.json` чрез `fetch`.

## Данни и поддръжка

Стойностите за основните калкулатори са в `rates.json`; източниците и датите на последна ръчна проверка са в `metadata`. Скриптът `tools/python/check_rates_simple.py` показва чеклист и не проверява автоматично законодателството, нито променя стойностите. За чеклист и официални връзки стартирай `tools/python/verify_rates.bat` в Windows или `sh tools/python/verify_rates.sh` в Linux/macOS.

## Публикуване

GitHub Pages публикува сайта от `main` branch, `/` (root):

<https://darcskull.github.io/bg-calculators/>
