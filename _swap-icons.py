#!/usr/bin/env python3
"""
Swap legacy SVG icons w plikach HTML na nowy iOS-style:
  - viewBox: 0 0 24 24
  - stroke-width: 1.8
  - stroke-linecap/linejoin: round
  - fill: none

Strategia: match cały <svg ...>...</svg> po sygnaturze d="..." (path content
jest unikalny per ikona). Zachowuje atrybuty wrappera (class, width, height,
aria-*). Podmienia viewBox, stroke-width, oraz wewnętrzne paths/circles/rects.

Skrypt jest IDEMPOTENT — jeśli ikona już jest w nowym formacie (vb 24), pomija.
"""

import re
import sys
import pathlib

ROOT = pathlib.Path(__file__).parent

# Lista plików do podmiany. icons.html pomijamy (to jest sama biblioteka).
FILES = [
    'index.html',
    'demo-calendar.html',
    'course-form-preview.html',
    'kontakt.html',
    'signup.html',
    'login.html',
    'forgot-password.html',
    'forgot-password-sent.html',
    'reset-password.html',
    'case-study.html',
    'landing-v2.html',
]

# ---------------------------------------------------------------------------
# Mapping: signature (current d=) → new SVG inner (viewBox, stroke-width 1.8,
# nowe paths). Każdy entry ma:
#   match_d: string (lub regex z opcjonalnym wildcardem) — content path
#            do rozpoznania ikony
#   match_extra: dodatkowy snippet wymagany w starym svg (np. circle radius)
#                żeby rozróżnić ikony o podobnym path
#   new_inner: HTML do wstawienia jako wnętrze <svg>...</svg>
#   new_attrs: dict mergowany do atrybutów <svg>; minimum:
#              viewBox, stroke-width
# ---------------------------------------------------------------------------

# Nowe inner content (każda ikona = string z paths/circles/rects).
NEW = {
    'chevron-down':         '<path d="M6 9l6 6 6-6"/>',
    'chevron-right':        '<path d="M9 6l6 6-6 6"/>',
    'chevron-left':         '<path d="M15 6l-6 6 6 6"/>',
    'chevron-double-left':  '<path d="M13 6l-6 6 6 6"/><path d="M19 6l-6 6 6 6"/>',
    'chevron-double-right': '<path d="M11 6l6 6-6 6"/><path d="M5 6l6 6-6 6"/>',
    'plus':                 '<path d="M12 5v14"/><path d="M5 12h14"/>',
    'xmark':                '<path d="M6 6l12 12"/><path d="M18 6L6 18"/>',
    'trash':                '<path d="M4 7h16"/><path d="M10 4h4a1 1 0 0 1 1 1v2H9V5a1 1 0 0 1 1-1z"/><path d="M6 7l1 13a2 2 0 0 0 2 2h6a2 2 0 0 0 2-2l1-13"/><path d="M10 11v7"/><path d="M14 11v7"/>',
    'checkmark':            '<path d="M5 12.5l5 5L19 7"/>',
    'calendar':             '<rect x="3" y="5" width="18" height="16" rx="2.5"/><path d="M3 10h18"/><path d="M8 3v4"/><path d="M16 3v4"/>',
    'clock':                '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3.5 2"/>',
    'phone':                '<path d="M5.5 4.5C5.5 3.95 5.95 3.5 6.5 3.5h2.36a1 1 0 0 1 .97.76l1.07 4.29a1 1 0 0 1-.27.95L8.86 11.18a13 13 0 0 0 5.96 5.96l1.68-1.77a1 1 0 0 1 .95-.27l4.29 1.07a1 1 0 0 1 .76.97V19.5c0 .55-.45 1-1 1H19.5C11.77 20.5 4.5 13.23 4.5 5.5z"/>',
    'envelope':             '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 8l9 6 9-6"/>',
    'bolt':                 '<path d="M13 3L4 14h7l-1 7 9-11h-7l1-7z"/>',
    'info-circle':          '<circle cx="12" cy="12" r="9"/><path d="M12 10.5v6"/><path d="M12 7.5h.01"/>',
    'question-circle':      '<circle cx="12" cy="12" r="9"/><path d="M9.5 9.5a2.5 2.5 0 0 1 5 0c0 1.5-2.5 2-2.5 4"/><path d="M12 17.5v.01"/>',
    'filter':               '<path d="M4 6h16"/><path d="M7 12h10"/><path d="M10 18h4"/>',
}

# Sygnatury starych ikon (d= content lub charakterystyczny snippet wnętrza
# starego SVG). Lista par (regex, icon_name). Regex jest matchowany na całym
# WNĘTRZU (innerHTML) starego SVG (między <svg ...> a </svg>).
SIGNATURES = [
    # chevron-down (12x12)
    (r'^\s*<path d="M3 4l3 3 3-3"\s*/>\s*$',                                                          'chevron-down'),
    # chevron-right (16x16)
    (r'^\s*<path d="M6 3l5 5-5 5"\s*/>\s*$',                                                          'chevron-right'),
    # chevron-left (16x16)
    (r'^\s*<path d="M10 3L5 8l5 5"\s*/>\s*$',                                                         'chevron-left'),
    # chevron-double-left
    (r'^\s*<path d="M9 3L4 8l5 5M14 3L9 8l5 5"\s*/>\s*$',                                             'chevron-double-left'),
    # chevron-double-right
    (r'^\s*<path d="M7 3l5 5-5 5M2 3l5 5-5 5"\s*/>\s*$',                                              'chevron-double-right'),
    # plus (12x12)
    (r'^\s*<path d="M6 2v8M2 6h8"\s*/>\s*$',                                                          'plus'),
    # plus krzyżyk (24x24 FAQ)
    (r'^\s*<path d="M12 5v14M5 12h14"\s*/>\s*$',                                                      'plus'),
    # X / close (16x16)
    (r'^\s*<path d="M3.5 3.5l9 9M12.5 3.5l-9 9"\s*/>\s*$',                                            'xmark'),
    # Trash (14x14)
    (r'^\s*<path d="M3 4h8M5\.5 4V2\.5h3V4M4\.5 4l\.5 7\.5h4l\.5-7\.5M6 6v4M8 6v4"\s*/>\s*$',         'trash'),
    # Check thin (14x14 sw 2.2)
    (r'^\s*<path d="M2 7\.5l3 3 7-7"\s*/>\s*$',                                                       'checkmark'),
    # Check thick (24x24 sw 3 FAQ)
    (r'^\s*<path d="M5 13l5 5L20 7"\s*/>\s*$',                                                        'checkmark'),
    # Check w selektorze (audyt: vb 20x20 lub 12x12, path "M4 10.5l4 4 8-9")
    (r'^\s*<path d="M4 10\.5l4 4 8-9"\s*/>\s*$',                                                      'checkmark'),
    # Calendar (16x16)
    (r'^\s*<rect x="2\.5" y="3\.5" width="11" height="10" rx="1\.5"\s*/>\s*<path d="M2\.5 6\.5h11M5\.5 2v3M10\.5 2v3"\s*/>\s*$', 'calendar'),
    # Clock (12x12)
    (r'^\s*<circle cx="6" cy="6" r="4\.5"\s*/>\s*<path d="M6 3\.5V6l2 1"\s*/>\s*$',                   'clock'),
    # Envelope (24x24)
    (r'^\s*<rect x="2" y="4" width="20" height="16" rx="2"\s*/>\s*<polyline points="22,6 12,13 2,6"\s*/>\s*$', 'envelope'),
    # Lightning bolt (24x24)
    (r'^\s*<path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"\s*/>\s*$',                                       'bolt'),
    # Info (i) — 12x12
    (r'^\s*<circle cx="6" cy="6" r="5"\s*/>\s*<path d="M6 5\.5v3M6 3\.5v\.01"\s*/>\s*$',              'info-circle'),
    # Question (?) — 16x16
    (r'^\s*<circle cx="8" cy="8" r="6"\s*/>\s*<path d="M8 7v4"\s*/>\s*<path d="M8 5\.2v\.1"\s*/>\s*$', 'question-circle'),
    # Filter (12x12)
    (r'^\s*<path d="M2 3h8M3 6h6M4\.5 9h3"\s*/>\s*$',                                                 'filter'),
]

# Regex matchujący kompletny <svg ... >...</svg> (non-greedy, single-line z DOTALL)
SVG_RE = re.compile(r'(<svg\b)([^>]*)>(.*?)(</svg>)', re.DOTALL)

# Atrybuty do nadpisania w nowym SVG
TARGET_VB = '0 0 24 24'
TARGET_SW = '1.8'


def update_attrs(attrs_str):
    """Zmień viewBox + stroke-width w łańcuchu atrybutów svg.
       Zachowuje class, width, height, aria-*, xmlns. Wymusza
       fill="none", stroke="currentColor", stroke-linecap/join="round".
    """
    # viewBox
    if re.search(r'\bviewBox="[^"]*"', attrs_str):
        attrs_str = re.sub(r'\bviewBox="[^"]*"', f'viewBox="{TARGET_VB}"', attrs_str)
    else:
        attrs_str = f' viewBox="{TARGET_VB}"' + attrs_str

    # stroke-width
    if re.search(r'\bstroke-width="[^"]*"', attrs_str):
        attrs_str = re.sub(r'\bstroke-width="[^"]*"', f'stroke-width="{TARGET_SW}"', attrs_str)
    else:
        attrs_str = attrs_str.rstrip() + f' stroke-width="{TARGET_SW}"'

    # fill="none" — wymuszamy
    if re.search(r'\bfill="[^"]*"', attrs_str):
        attrs_str = re.sub(r'\bfill="[^"]*"', 'fill="none"', attrs_str)
    else:
        attrs_str = attrs_str.rstrip() + ' fill="none"'

    # stroke="currentColor" — wymuszamy
    if re.search(r'\bstroke="[^"]*"', attrs_str):
        attrs_str = re.sub(r'\bstroke="[^"]*"', 'stroke="currentColor"', attrs_str)
    else:
        attrs_str = attrs_str.rstrip() + ' stroke="currentColor"'

    # stroke-linecap round
    if re.search(r'\bstroke-linecap="[^"]*"', attrs_str):
        attrs_str = re.sub(r'\bstroke-linecap="[^"]*"', 'stroke-linecap="round"', attrs_str)
    else:
        attrs_str = attrs_str.rstrip() + ' stroke-linecap="round"'

    # stroke-linejoin round
    if re.search(r'\bstroke-linejoin="[^"]*"', attrs_str):
        attrs_str = re.sub(r'\bstroke-linejoin="[^"]*"', 'stroke-linejoin="round"', attrs_str)
    else:
        attrs_str = attrs_str.rstrip() + ' stroke-linejoin="round"'

    return attrs_str


def replace_svg(match):
    open_tag, attrs, inner, close_tag = match.group(1), match.group(2), match.group(3), match.group(4)

    # Skip — to jest logo / wordmark / animacja / hero illustration (oznaczone
    # po znacznikach albo po viewBox > 32). Nie ruszamy.
    if re.search(r'\bviewBox="0 0 (?:[3-9]\d|\d{3,})', attrs):
        return match.group(0)
    # Logo Schooleo (czapka) ma viewBox 0 0 72 72 — łapie się powyżej, OK.
    # Wordmark 0 0 239 48 — też powyżej.

    inner_stripped = inner.strip()

    # Try each signature
    for sig_pattern, icon_name in SIGNATURES:
        if re.search(sig_pattern, inner_stripped, re.DOTALL):
            new_attrs = update_attrs(attrs)
            new_inner = NEW[icon_name]
            return f'{open_tag}{new_attrs}>{new_inner}{close_tag}'

    return match.group(0)


def process(filename):
    path = ROOT / filename
    if not path.exists():
        print(f'  skip: {filename} (brak pliku)')
        return 0, 0
    src = path.read_text()
    total_svgs = 0
    swapped = 0

    def counter(match):
        nonlocal total_svgs, swapped
        total_svgs += 1
        result = replace_svg(match)
        if result != match.group(0):
            swapped += 1
        return result

    new_src = SVG_RE.sub(counter, src)
    if new_src != src:
        path.write_text(new_src)
    return swapped, total_svgs


def main():
    grand_swapped = 0
    grand_total = 0
    for fn in FILES:
        swapped, total = process(fn)
        grand_swapped += swapped
        grand_total += total
        marker = '✓' if swapped else '·'
        print(f'  {marker} {fn:<35}  swapped {swapped}/{total} SVG')
    print()
    print(f'SUMA: podmienione {grand_swapped} ikon w {len([fn for fn in FILES])} plikach (na {grand_total} SVG ogółem)')


if __name__ == '__main__':
    main()
