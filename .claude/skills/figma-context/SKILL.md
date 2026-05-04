---
name: figma-context
description: Pobierz kontekst designu (kod, tokeny, layout, typografia, kolory) z Figmy dla wskazanego node'a i odwzoruj go w kodzie z maksymalną wiernością — bez screenshotów. Użyj gdy Marcin wkleja link do Figmy, prosi "weź z figmy", "zaimplementuj ten ekran", "odtwórz sekcję", "pobierz design", lub podaje sam node-id. Cel: pixel-perfect HTML/CSS/JS odpowiadający temu, co jest w Figmie.
---

# Figma — get design context (no screenshots, max fidelity)

Skill do wyciągania **strukturalnego kontekstu** z konkretnego node'a w pliku Schooleo i odwzorowania go w kodzie z maksymalną wiernością. Zero screenshotów — pracujemy wyłącznie na tym, co zwraca `get_design_context` (kod referencyjny, tokeny, layout, typografia, hinty, annotacje).

**Cel nadrzędny:** to, co jest w Figmie = to, co ląduje w kodzie. Spacing, rozmiary, wagi, letter-spacing, line-height, kolory, radiusy, kolejność elementów — wszystko 1:1.

## Plik domyślny

- **fileKey:** `T3MkG8vqRgLc5BzM3DA1aS`
- **URL bazowy:** https://www.figma.com/design/T3MkG8vqRgLc5BzM3DA1aS/Schooleo
- **Default root node:** `94:14` (z `?node-id=94-14`)

Jeśli Marcin nie poda node'a — pytaj. Nie zgaduj.

## Parsowanie URL-a

Z `figma.com/design/:fileKey/:fileName?node-id=:nodeId`:
- `fileKey` → wprost
- `nodeId` → w URL `94-14`, w API `94:14` (zamień `-` na `:`)

## Procedura

1. **Sparsuj** URL lub input (fileKey + nodeId).
2. **Wywołaj** `mcp__plugin_figma_figma__get_design_context` z:
   - `nodeId` (po konwersji `-` → `:`)
   - `clientFrameworks: "html"`
   - `clientLanguages: "css,js"`
3. **NIE wywołuj** `get_screenshot`, `get_metadata`, `get_variable_defs` — chyba że Marcin wprost poprosi.
4. **Wyciągnij z odpowiedzi WSZYSTKIE wartości liczbowe** i zachowaj je dosłownie:
   - rozmiary (width, height, font-size)
   - spacing (padding, margin, gap)
   - typografia (font-weight, letter-spacing, line-height)
   - kolory (hex / variables)
   - radius, border, shadow
   - kolejność i zagnieżdżenie elementów
5. **Zaimplementuj** w vanilla HTML/CSS/JS — patrz reguły niżej.

## Reguły odwzorowania (pixel-perfect)

### Wartości liczbowe
- **Bierz dokładnie z Figmy.** Jeśli Figma mówi `padding: 18px 26px` — to ma być `18px 26px`, nie zaokrąglone do `16px 24px`.
- **Letter-spacing w `em`/`%`** — przelicz dokładnie (np. `-6%` przy 64px = `-3.84px`, używaj wartości z Figma response, nie zaokrąglaj).
- **Line-height** — jeśli Figma daje liczbę pikseli (`70`), użyj `70px`; jeśli mnożnik (`1.08`), użyj `1.08`.

### Tokeny vs raw hex
- **Pierwszeństwo:** jeśli Figma zwraca CSS variable (np. `var(--brand)`) i landing ma już taki token z tą samą wartością → użyj tokenu.
- **Jeśli Figma daje raw hex i wartość pasuje do istniejącego tokenu** w landing CSS → użyj tokenu (spójność).
- **Jeśli wartość się różni od istniejących tokenów** → użyj raw hex z Figmy. NIE podmieniaj na "podobny" token. Wierność > spójność.

Tokeny landing (sprawdź w `index.html` / `style.css` zanim zmapujesz):
- `--bg-warm` `#F7F4EE`, `--bg-subtle` `#F0EDE7`, `--border` `#E8E4DA`
- `--text` `#1A1714`, `--muted` `#6B6560`, `--subtle` `#B0AAA0`
- Brand `#E84B20`, hover `#C13A15`
- Akcent `#fde68a`, zieleń logo `#164037`

### Layout
- **Auto-layout z Figmy** → flex z dokładnym `gap`, `padding`, `align-items`, `justify-content` z response.
- **Absolute positioning** w Figmie → odwzoruj `position: absolute` z dokładnymi `top/left/right/bottom`.
- **Constraints** (left/right, top/bottom, scale) → przekuj na flex/grid/percent zgodnie z intencją.
- **Kolejność** elementów w HTML = kolejność w Figmie (z-index, czytelność, accessibility).

### Typografia
- Font: Inter (jeśli Figma używa innego — zaalarmuj Marcina).
- Waga: dokładnie taka jak w Figmie (`Extra Bold` = 800, `Black` = 900, `Semi Bold` = 600).
- Wszystkie text styles z Figma response zachowuj jako oddzielne klasy/style (np. `.display-hero`, `.label-eyebrow`).

### Stany i interakcje
- Jeśli Figma ma warianty (hover/focus/active/disabled) → zaimplementuj je z dokładnymi wartościami.
- Jeśli nie ma — dodaj minimalny stan focus (2px ring `rgba(232,75,32,0.15)`) dla a11y i powiedz Marcinowi że dodałeś, bo Figma nie definiowała.

### Code Connect / annotacje
- Jeśli Figma zwraca **Code Connect** mapowanie → użyj wskazanego komponentu/klasy z kodu, NIE generuj nowego.
- Jeśli są **annotacje designerskie** (notatki w Figmie) → traktuj jak instrukcje, wymień Marcinowi co znalazłeś.

## Format odpowiedzi dla Marcina

Po wywołaniu `get_design_context`:

1. **Co jest w node'zie** — 1-2 zdania (typ: ekran/sekcja/komponent, kluczowe bloki).
2. **Kluczowe wartości** wyciągnięte z Figmy (rozmiary, spacing, fonty, kolory) — krótka lista.
3. **Plan implementacji** — gdzie w `index.html` wpiąć, jakie nowe klasy CSS, jakie skrypty JS.
4. **Rozbieżności względem landingu** — np. "Figma używa `#FFA500`, landing ma `--brand` `#E84B20` — w tym node'zie zostawiam Figma value bo to inny kolor".
5. **Czego brakuje w Figmie** — stany, responsywność, copy itd. — żeby Marcin świadomie zdecydował.

Mów językiem projektanta: hierarchia, rytm, skanowalność, afordancje — ale przy decyzjach implementacyjnych priorytet to **wierność designowi**.

## Czego NIE robić

- ❌ Nie pobieraj screenshotów (`get_screenshot`).
- ❌ Nie zaokrąglaj wartości "do ładnych liczb" (`18px` ≠ `16px`).
- ❌ Nie podmieniaj kolorów Figmy na "najbliższy token" jeśli wartość się różni.
- ❌ Nie upraszczaj layoutu "bo tak jest czyściej" — jeśli Figma ma 3 wrappery, to mają być 3 wrappery (chyba że są jawnie redundantne i Marcin to akceptuje).
- ❌ Nie generuj React/Tailwind 1:1 z response — przepisuj na vanilla HTML/CSS, ale wartości liczbowe i strukturę zachowaj.
- ❌ Nie wymyślaj node-id — pytaj jeśli nie ma w URL.
