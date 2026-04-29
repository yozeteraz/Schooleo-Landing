# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Język komunikacji

Rozmawiamy i piszemy wyłącznie po polsku — odpowiedzi, komentarze, commit messages, nazwy zmiennych semantycznych (labele w UI), treści pomocnicze. Wyjątek: kod (składnia, API, frameworkowe stringi) zostaje w oryginale.

## O projekcie

**Schooleo** to aplikacja webowa do zarządzania szkołami prywatnymi, franczyzami edukacyjnymi i freelancerami prowadzącymi zajęcia. Strona produktu: https://www.schooleo.io/en/

### Główne moduły funkcjonalne

- **Planowanie lekcji** — harmonogramowanie, anulowanie i zmiana terminów zajęć
- **Zarządzanie kadrą i uczniami** — centralna baza danych pracowników i studentów
- **Obsługa płatności** — transakcje online od uczniów
- **Komunikacja** — powiadomienia dla personelu i uczniów
- **Raporty** — analiza danych i monitoring wydajności
- **Portal ucznia** — samoobsługowy dostęp do płatności i zajęć

### Grupy użytkowników

- Administratorzy szkoły
- Nauczyciele / kadra
- Uczniowie / rodzice

## Landing page

Repo na GitHub: https://github.com/yozeteraz/Schooleo-Landing.git
Projekt: nowy landing w HTML/CSS/JS, deployowany na Vercel.

Strona live: https://schooleo-landing.vercel.app

## Deploy

Żeby wdrożyć zmiany na Vercel, wpisz w terminalu:

```
deploy "opis zmiany"
```

Alias `deploy` uruchamia skrypt `deploy.sh`, który robi git add + commit + push. Vercel automatycznie wykrywa push i deployuje stronę (~30 sekund).

Przed pushem możesz podejrzeć zmiany otwierając `index.html` bezpośrednio w przeglądarce (dwuklik w Finderze).
