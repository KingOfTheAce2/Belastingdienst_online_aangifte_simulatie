# Belastingdienst Online Aangifte Simulatie

This project contains compiled JavaScript modules that simulate Dutch tax forms. The code was produced with Google Web Toolkit and covers tax years 2017 through 2025.

## Available Modules

All compiled tax form modules are stored in the `modules` directory:

- `modules/cross-border_aangifte-24.js` – Cross-border income tax return 2024
- `modules/ib_opgaaf_werkelijk_rendement-17.js` – Actual investment returns declaration 2017
- `modules/ib_opgaaf_werkelijk_rendement-18.js` – Actual investment returns declaration 2018
- `modules/ib_opgaaf_werkelijk_rendement-19.js` – Actual investment returns declaration 2019
- `modules/ib_opgaaf_werkelijk_rendement-20.js` – Actual investment returns declaration 2020
- `modules/ib_opgaaf_werkelijk_rendement-21.js` – Actual investment returns declaration 2021
- `modules/ib_opgaaf_werkelijk_rendement-22.js` – Actual investment returns declaration 2022
- `modules/ib_opgaaf_werkelijk_rendement-23.js` – Actual investment returns declaration 2023
- `modules/ib_opgaaf_werkelijk_rendement-24.js` – Actual investment returns declaration 2024
- `modules/migratie_aangifte-24.js` – Migration tax return 2024
- `modules/Particuliere_aangifte-24.js` – Resident income tax return 2024
- `modules/voorlopige_aanslag-25-buitenlands_belastingplichtige.js` – Provisional assessment for non-resident taxpayers 2025
- `modules/voorlopige_aanslag-25-binnenlands_belastingplichtige.js` – Provisional assessment for resident taxpayers 2025

The `analysis`, `documentation`, `integration`, and `plans` directories provide architectural analysis, modernization roadmaps and related documentation.

## Translation Resources

The `i18n` directory contains Dutch to English translation files. These files use the `{year}` placeholder for interchangeable tax years; when a string refers to a specific year, the year is hardcoded in the translation.

## License

Use of this code is restricted. All content is copyright © Belastingdienst Online Aangifte Simulatie project. Redistribution or reuse of any portion of the code or documents is prohibited without prior written permission. See the [LICENSE](LICENSE) file for full details.
