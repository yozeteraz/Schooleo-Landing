# Schooleo — Design System

Źródło prawdy dla tokenów: [`tokens.css`](./tokens.css). Ten dokument jest tylko widokiem dla człowieka — jeśli edytujesz tokeny, rób to w `.css`, a tabele tutaj aktualizuj ręcznie dla zgodności.

## Jak używać

W każdym HTML-u dołącz `tokens.css` przed własnymi stylami:

```html
<link rel="stylesheet" href="tokens.css">
<style>
  .button-primary {
    background: var(--brand);
    color: var(--color-white);
    padding: var(--space-2) var(--space-4);
    border-radius: var(--radius-sm);
    font: var(--font-label);
  }
  .button-primary:focus-visible {
    outline: none;
    box-shadow: var(--ring-focus);
  }
</style>
```

**Zasada:** w kodzie używaj aliasów semantycznych (`--brand`, `--text`, `--border`) zamiast surowych tokenów (`--color-primary-500`) — dzięki temu zmiana brandingu to jedno podmienienie w jednym miejscu.

---

## Font

**Inter** — Regular (400), Medium (500), Semi Bold (600), Bold (700), Extra Bold (800), Black (900).

---

## Logo

- Tekst: "Schooleo", Inter Black, 24px, letter-spacing -1.44px (6%)
- Na jasnym tle: tło białe, tekst `#164037` (ciemna zieleń)
- Na ciemnym tle: tło `#164037`, tekst biały
- Na brand tle: tło `#E84B20`, tekst biały

---

## Kolory (zsynchronizowane z Figma Variables)

**Źródło prawdy:** kolekcja `Schooleo / Colors` w pliku Figma `T3MkG8vqRgLc5BzM3DA1aS` (19 zmiennych) + `tokens.css` w kodzie. Brand Foundation (node `9:7`) i landing (node `16:2`) mają fills/strokes podpięte do tych zmiennych.

**Konwencja nazw:** każdy kolor ma nazwę „ludzką" (peach, orange, cream, fog…) — w Figmie z numerem skali w sufiksie (`primary/orange-500`), w CSS dwa równoległe tokeny: skalowy (`--color-primary-500`) i ludzki (`--color-orange-500`). **Można używać zamiennie**, oba wskazują na ten sam kolor.

### Primary (orange-red)

| Figma Variable | Token CSS (skalowy) | Alias ludzki | Hex | Użycie |
|----------------|---------------------|--------------|-----|--------|
| `primary/peach-100`  | `--color-primary-100` | `--color-peach-100`  | `#FDEEE9` | tła selected, focus, brand-subtle |
| `primary/amber-300`  | `--color-primary-300` | `--color-amber-300`  | `#F5A623` | akcent ostrzegawczy/żółty |
| `primary/orange-500` | `--color-primary-500` | `--color-orange-500` | `#E84B20` | **główny brand** — primary button, focus border |
| `primary/rust-700`   | `--color-primary-700` | `--color-rust-700`   | `#C13A15` | hover/pressed primary button |
| `primary/brick-900`  | `--color-primary-900` | `--color-brick-900`  | `#8B2510` | text na brand-subtle bg |

### Neutral

| Figma Variable | Token CSS (skalowy) | Alias ludzki | Hex | Alias semantyczny | Użycie |
|----------------|---------------------|--------------|-----|-------------------|--------|
| `neutral/cream-50`     | `--color-neutral-50`  | `--color-cream-50`     | `#F7F4EE` | `--bg-warm`       | główne tło |
| `neutral/sand-100`     | `--color-neutral-100` | `--color-sand-100`     | `#F0EDE7` | `--bg-subtle`     | hover ghost, disabled bg |
| `neutral/stone-200`    | `--color-neutral-200` | `--color-stone-200`    | `#E8E4DA` | `--border`        | hairline borders |
| `neutral/fog-400`      | `--color-neutral-400` | `--color-fog-400`      | `#B0AAA0` | `--text-subtle`, `--border-strong` | disabled text, hover border |
| `neutral/smoke-600`    | `--color-neutral-600` | `--color-smoke-600`    | `#6B6560` | `--text-muted`    | placeholder, helper text |
| `neutral/charcoal-800` | `--color-neutral-800` | `--color-charcoal-800` | `#2E2A26` | —                 | — |
| `neutral/ink-900`      | `--color-neutral-900` | `--color-ink-900`      | `#1A1714` | `--text`          | główny tekst |

### Green (logo) i Accent

| Figma Variable | Token CSS (skalowy) | Alias ludzki | Hex | Użycie |
|----------------|---------------------|--------------|-----|--------|
| `green/forest-900` | `--color-green-900`        | `--color-forest-900` | `#164037` | logo |
| `accent/butter`    | `--color-accent-highlight` | `--color-butter`     | `#FDE68A` | żółte podkreślenie nagłówków |
| `accent/paper`     | `--color-white`            | `--color-paper`      | `#FFFFFF` | tło inputów, karty na scenie |

### Semantic

| Figma Variable | Token CSS (skalowy) | Alias ludzki | Hex | Użycie |
|----------------|---------------------|--------------|-----|--------|
| `semantic/leaf`     | `--color-success` | `--color-leaf`     | `#2ECC71` | powodzenie |
| `semantic/tomato`   | `--color-error`   | `--color-tomato`   | `#E74C3C` | błędy walidacji |
| `semantic/marigold` | `--color-warning` | `--color-marigold` | `#F39C12` | ostrzeżenia |
| `semantic/sky`      | `--color-info`    | `--color-sky`      | `#3498DB` | informacje |

---

## Typografia (zsynchronizowane z Figma Text Styles)

Źródło prawdy: style tekstowe w pliku Figma `T3MkG8vqRgLc5BzM3DA1aS`. Wszystkie role pochodzą z faktycznego użycia w landingu — landing łapie display/heading/body, formularz/kalendarz łapią body-small/label/caption. **Jeden zbiór, oba światy.**

| Token CSS | Figma | Rozmiar | Waga | LH | Tracking | Użycie |
|-----------|-------|---------|------|----|----------|--------|
| `--font-display-statement`  | Display / Statement   | 78px | 800 (Extra Bold) | 1.02 | -3.5% | Statement headline |
| `--font-display-hero`       | Display / Hero        | 64px | 800 (Extra Bold) | 1.05 | -3.5% | Hero h1 |
| `--font-display-xl`         | Display / XL          | 52px | 800 (Extra Bold) | 1.10 | -3% | Sign-off, FAQ heading |
| `--font-display-l`          | Display / L           | 46px | 800 (Extra Bold) | 1.10 | -3% | Feature/section headings |
| `--font-h1`                 | Heading / H1          | 36px | 800 (Extra Bold) | 1.20 | -3% | Section titles |
| `--font-h2`                 | Heading / H2          | 24px | 800 (Extra Bold) | 1.20 | -2% | Subsekcje, kafelki |
| `--font-h3`                 | Heading / H3          | 20px | 700 (Bold) | 1.40 | -1% | Tytuły kart, akapitów |
| `--font-body-large`         | Body / Large          | 19px | 400 (Regular) | 1.50 | 0 | Marketing body, lead |
| `--font-body`               | Body / Default        | 17px | 400 (Regular) | 1.55 | 0 | Główny body landingu |
| `--font-body-small`         | Body / Small          | 14px | 400 (Regular) | 1.45 | 0 | **Wartości inputów, dense UI (formularz/kalendarz)** |
| `--font-label`              | Label / Default       | 14px | 600 (Semi Bold) | 1.43 | +2% | **Label formularza** |
| `--font-label-small`        | Label / Small         | 12px | 600 (Semi Bold) | 1.33 | +2% | Label mały, mikroprzyciski |
| `--font-eyebrow`            | Eyebrow               | 11px | 400 (Regular) | 1.45 | +14% | Eyebrow (uppercase) |
| `--font-caption`            | Caption               | 12px | 400 (Regular) | 1.33 | 0 | **Helper, error, meta** |
| `--font-accent-handwritten` | Accent / Handwritten  | 24px | 400 (Regular, Caveat) | 1.30 | 0 | Pojedyncze akcenty „odręczne" w landingu |

> Letter-spacing per token: `--tracking-display-statement` / `-hero` (-3.5%), `--tracking-display-xl` / `-l` / `--tracking-h1` (-3%), `--tracking-h2` (-2%), `--tracking-h3` (-1%), `--tracking-label` (+2%), `--tracking-eyebrow` (+14%). Body i caption — bez trackingu.

**Wyjątki spoza systemu Inter:**
- Logo „Schooleo" — Lato Black (oddzielny komponent brandowy, nie token tekstowy)
- Wielki cytat na landingu — Georgia Bold (jednorazowy akcent redakcyjny)

---

## Spacing (4px base)

| Token CSS | Wartość | Typowe użycie |
|-----------|---------|---------------|
| `--space-1`  | 4px  | gap ikona + label |
| `--space-2`  | 8px  | padding Y w inputach (dense), gap między przyciskami |
| `--space-3`  | 12px | padding X w inputach, row gap w formularzu |
| `--space-4`  | 16px | gap między grupami pól |
| `--space-5`  | 20px | padding wewnątrz karty |
| `--space-6`  | 24px | gap między sekcjami formularza |
| `--space-8`  | 32px | padding modala |
| `--space-10` | 40px | — |
| `--space-12` | 48px | — |
| `--space-16` | 64px | odstępy dużych bloków |

**Reguły dla formularzy:**
- Input padding: `var(--space-2) var(--space-3)` — wysokość kontrolki ≈ 32–34px
- Label → input: `6px`
- Row gap: `var(--space-3)`
- Section gap: `var(--space-6)`

---

## Radius

| Token CSS | Wartość | Użycie |
|-----------|---------|--------|
| `--radius-xs`   | 4px   | tagi, pille, mikro-badge |
| `--radius-sm`   | 6px   | **kontrolki** — input, button, select, checkbox, chip |
| `--radius-md`   | 8px   | karty, dropdowny, popovery |
| `--radius-lg`   | 12px  | modale, panele, sheety |
| `--radius-full` | 999px | avatary, switches, niektóre segment controls |

---

## Stany kontrolek (na tle `--bg-warm`)

Pochodne z istniejącej palety — bez dodawania nowych kolorów.

| Stan | Tło | Border | Tekst | Ring / dodatkowe |
|------|-----|--------|-------|------------------|
| **Default (input)** | `--bg-surface` (#FFF) | 1px `--border` | `--text` | — |
| **Default (ghost)** | transparent | 1px `--border` | `--text` | — |
| **Hover** | `--bg-subtle` (ghost) / bez zmian (input) | `--border-strong` | — | — |
| **Focus** | bez zmian | 1px `--brand` | — | `box-shadow: var(--ring-focus)` |
| **Active / pressed** (button) | `--brand-hover` | — | `--color-white` | brak translate |
| **Disabled** | `--bg-subtle` | `--border` | `--text-subtle` | `cursor: not-allowed` |
| **Selected / checked** | `--brand-subtle` | `--brand` | `--text` | — |
| **Error** | bez zmian | `--color-error` | — | przy focusie: `var(--ring-error)` |
| **Read-only** | `--bg-warm` | `--border` lub transparent | `--text` | — |

**Zasady stanów:**
- Zero cieni na default — warstwy budujemy borderem + tłem
- Focus **zawsze widoczny** (ring 2px, WCAG)
- Disabled nie używa `opacity` — kolory robią robotę (czytelniej dla czytnika ekranu)
- Placeholder: `--text-muted`

---

## Ogólny styl

- **Landing page** — ciepły, organiczny, Basecamp-inspired: dominuje `--bg-warm`, akcent `--brand`, ciemnozielony `--color-green-900` w logo. Nagłówki Extra Bold z ciasnym kernigiem.
- **UI aplikacji (formularze, panele)** — "Linear w light mode": gęsta typografia, hairline borders, subtelny radius (`--radius-sm` dla kontrolek, `--radius-md` dla kontenerów), `--bg-warm` jako tło sceny, hierarchia przez wagę i spacing zamiast koloru i cienia.

---

## Figma

Plik `h3wb2BzWZYJ7SQVMhpi8SG`, strona "Landing Page": Nav → Hero → Statement → Features (3) → Demo → Trusted By → Online Signups → Portal → FAQ → Sign-off → Footer.
