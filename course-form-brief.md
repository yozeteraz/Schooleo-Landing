# Brief — redesign kontrolek formularza kursu (v2)

Plik roboczy. Edytuj bezpośrednio — to jest nasza umowa, do której wracam przy implementacji.

Referencja do odtworzenia: [`References/Kurs - Schooleo Demo.html`](./References/Kurs%20-%20Schooleo%20Demo.html)
Design system: [`design-system.md`](./design-system.md) + [`tokens.css`](./tokens.css)
Deliverable: `course-form-preview.html` w roocie (otwieralny dwuklikiem, działający prototyp)

---

## Zakres i priorytet

- **Skupiamy się wyłącznie na UI kontrolek** — wygląd pól, przycisków, selectów, checkboxów, datepickerów, etykiet, stanów (default / hover / focus / active / disabled / error).
- UX (kolejność pól, logika formularza, walidacje, flow) **nie jest teraz przedmiotem pracy** — zostaje taki jak w referencji.

---

## Kierunek wizualny — "Linear w light mode"

Minimalistyczny, gęsty interfejs zoptymalizowany pod klawiaturę, z jasną, off-white paletą i hierarchią budowaną typografią zamiast dekoracji.

**Zasady estetyki:**
- Estetyka à la Linear, ale light mode — funkcjonalny minimalizm, zero ozdobników
- Tło off-white (`--bg-warm` = `#F7F4EE`, spójne z brandem Schooleo), wysoki kontrast typografii
- Gęste rozmieszczenie informacji, kompaktowa typografia (Inter — już w design systemie)
- Hierarchia przez **wagę, rozmiar i odstępy**, nie przez kolor czy cień
- **Konsekwentny, subtelny radius: 6px dla kontrolek, 8px dla kontenerów, 12px dla modali.** Charakter "engineering-grade" bierze się z hairline borders, typograficznego kontrastu i oszczędności — nie z ostrych kątów.
- Hairline borders (1px, niski kontrast — `--border` = `#E8E4DA`), minimalne cienie (maks. jeden subtelny), zero gradientów i dekoracji
- Siatka i whitespace w duchu szwajcarskiego minimalizmu — ale spacing **gęsty**, nie rozrzedzony
- Komponenty pod power-usera: wsparcie skrótów klawiszowych, gotowość pod command palette (⌘K), szybkie akcje

**Unikamy:**
- Dark mode
- Dekoracyjnych ilustracji, glassmorphism, neumorfizmu
- Dużych cieni, mocnych gradientów, zbyt zaokrąglonych "friendly" form (pill-shape'y tam, gdzie powinien być delikatny radius)
- Rozrzedzonych, marketingowych layoutów z pustymi sekcjami

**Referencje:** Linear (light), Height, Raycast (landing), Cron / Notion Calendar, Pitch.

---

## Filozofia prototypu — "real feel, nie laboratorium"

- **Jeden działający ekran** — nie wystawa komponentów z pinowanymi popoverami.
- Kontrolki **działają na klik** — date picker otwiera się, select rozwija, time picker reaguje.
- Stany (hover / focus / error) widoczne naturalnie, przez interakcję — nie ustawione jako dekoracja.
- Custom date/time picker (napisane od zera) — natywne nie dają się ostylować pod ten język wizualny.
- Realistyczna treść: polskie labele, prawdziwe nazwy pól jak w aplikacji.

---

## Deliverable

- Plik `course-form-preview.html` w roocie (spójnie z istniejącymi `eyebrow-preview.html`, `features-preview.html`).
- Importuje `tokens.css`.
- Samodzielny, działający prototyp — otwieralny dwuklikiem w przeglądarce, bez build-stepu.
- Vanilla HTML/CSS/JS — bez frameworków.
- Po akceptacji kierunku **deploy na Vercel** (`deploy "preview: redesign kontrolek formularza kursu"`) — live URL: `schooleo-landing.vercel.app/course-form-preview.html`.
