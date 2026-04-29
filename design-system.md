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

## Kolory — Primary (orange-red)

| Token CSS | Hex | Użycie |
|-----------|-----|--------|
| `--color-primary-100` | `#FDEEE9` | tła selected, focus background, brand-subtle |
| `--color-primary-300` | `#F5A623` | — |
| `--color-primary-500` | `#E84B20` | **główny brand** — primary button, focus border |
| `--color-primary-700` | `#C13A15` | hover/pressed primary button |
| `--color-primary-900` | `#8B2510` | text na brand-subtle bg |

## Kolory — Neutral

| Token CSS | Hex | Alias | Użycie |
|-----------|-----|-------|--------|
| `--color-neutral-50`  | `#F7F4EE` | `--bg-warm`       | główne tło |
| `--color-neutral-100` | `#F0EDE7` | `--bg-subtle`     | hover ghost, disabled bg |
| `--color-neutral-200` | `#E8E4DA` | `--border`        | hairline borders |
| `--color-neutral-400` | `#B0AAA0` | `--text-subtle`, `--border-strong` | disabled text, hover border |
| `--color-neutral-600` | `#6B6560` | `--text-muted`    | placeholder, helper text |
| `--color-neutral-800` | `#2E2A26` | —                 | — |
| `--color-neutral-900` | `#1A1714` | `--text`          | główny tekst |

## Kolory — Green (logo) i Accent

| Token CSS | Hex | Użycie |
|-----------|-----|--------|
| `--color-green-900` | `#164037` | logo |
| `--color-accent-highlight` | `#FDE68A` | żółte podkreślenie nagłówków |
| `--color-white` | `#FFFFFF` | tło inputów, karty na scenie |

## Kolory — Semantic

| Token CSS | Hex | Użycie |
|-----------|-----|--------|
| `--color-success` | `#2ECC71` | powodzenie |
| `--color-error`   | `#E74C3C` | błędy walidacji |
| `--color-warning` | `#F39C12` | ostrzeżenia |
| `--color-info`    | `#3498DB` | informacje |

---

## Typografia (z Figma text styles)

| Token CSS | Rozmiar | Waga | LH | Tracking | Użycie |
|-----------|---------|------|----|----------|--------|
| `--font-display-statement` | 72px | 800 | 1.05 | -6% | Statement headline |
| `--font-display-hero`      | 64px | 800 | 1.08 | -6% | Hero h1 |
| `--font-display-xl`        | 52px | 800 | 1.08 | -5% | Sign-off, FAQ heading |
| `--font-display-l`         | 40px | 800 | 1.10 | -5% | Feature/section headings |
| `--font-h1`                | 36px | 800 | 1.20 | -3% | Section titles |
| `--font-h2`                | 24px | 600 | 1.33 | -0.2px | — |
| `--font-h3`                | 20px | 600 | 1.40 | 0 | — |
| `--font-body-large`        | 18px | 400 | 1.75 | 0 | Główny body text |
| `--font-body`              | 16px | 400 | 1.50 | 0 | Opisy, wartości inputów |
| `--font-body-small`        | 14px | 400 | 1.43 | 0 | Feature list, dense input |
| `--font-label`             | 14px | 600 | 1.43 | +0.1px | Label formularza |
| `--font-label-small`       | 12px | 600 | 1.33 | +0.2px | Label mały (uppercase opcjonalnie) |
| `--font-eyebrow`           | 11px | 400 | 1.45 | +14% | Eyebrow (uppercase) |
| `--font-caption`           | 12px | 400 | 1.33 | +0.1px | Helper, error, notki |

> Letter-spacing trackingów: `--tracking-display` (-6%), `--tracking-heading` (-3%), `--tracking-label` (+2%), `--tracking-eyebrow` (+14%).

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
