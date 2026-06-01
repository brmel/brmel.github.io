# Ibraverse — Motion

Motion is a print magazine that happens to be on a screen: **calm, brief, and purposeful.** Things
ease in like a page settling, not like a UI showing off. If a motion draws attention to itself, cut it.

---

## 1. Motion tokens

### Duration
| Token | ms | Use |
|---|---|---|
| `dur-1` | 120 | hover color, link underline, small state |
| `dur-2` | 200 | buttons, chips, focus, toggles |
| `dur-3` | 320 | card hover-lift, play-button, reveals |
| `dur-4` | 480 | page-load section reveal, image fade-in |
| `dur-5` | 640 | hero / cover entrance (rare) |

### Easing
| Token | cubic-bezier | Feel |
|---|---|---|
| `ease-standard` | `cubic-bezier(0.2, 0, 0, 1)` | default — settle in |
| `ease-out` | `cubic-bezier(0.16, 1, 0.3, 1)` | reveals, entrances (expo-out) |
| `ease-in-out` | `cubic-bezier(0.65, 0, 0.35, 1)` | moves that leave and return |
| `ease-spring` | `cubic-bezier(0.34, 1.36, 0.64, 1)` | the play-button only — one gentle overshoot |

### Distance
| Token | value |
|---|---|
| `move-sm` | 4px |
| `move-md` | 8px |
| `lift` | translateY(−2px) |
| `reveal-rise` | translateY(12px) → 0 |

```css
:root{
  --dur-1:120ms; --dur-2:200ms; --dur-3:320ms; --dur-4:480ms; --dur-5:640ms;
  --ease-standard:cubic-bezier(.2,0,0,1);
  --ease-out:cubic-bezier(.16,1,.3,1);
  --ease-in-out:cubic-bezier(.65,0,.35,1);
  --ease-spring:cubic-bezier(.34,1.36,.64,1);
}
```

---

## 2. Micro-interactions

### Link / hover
- Inline links sit in `--accent`. On hover the **underline draws in** left→right over `--dur-1` with
  `ease-standard`; color lifts to `--accent-soft`. On dark, the underline is always present (the
  Event-accent accessibility rule) and only thickens on hover.

```css
a.link{color:var(--accent);text-decoration:none;background-image:linear-gradient(var(--accent),var(--accent));
  background-size:0% 1.5px;background-repeat:no-repeat;background-position:0 100%;
  transition:background-size var(--dur-1) var(--ease-standard),color var(--dur-1)}
a.link:hover{background-size:100% 1.5px;color:var(--accent-soft)}
[data-theme="dark"] a.link{background-size:100% 1.5px} /* underline always on */
```

### Button
- Background/border shift over `--dur-2`; press = `scale(0.98)` for 80ms then back. No bounce.

### The reel card play-button
- Idle: a paper circle with the accent triangle, `shadow-card`.
- Hover: scales `1.0 → 1.06` over `--dur-3` with **`ease-spring`** (one gentle overshoot), `shadow-pop`,
  the ring draws around it. This is the only spring in the system.
- Click → load: the button fades/scales out over `--dur-2`, the thumbnail crossfades to the embedded
  player. Click-to-load (no autoplay) keeps the page calm and fast.

```css
.reel .play{transition:transform var(--dur-3) var(--ease-spring),box-shadow var(--dur-3)}
.reel:hover .play{transform:scale(1.06)}
.reel .play:active{transform:scale(.98)}
```

### Page-load reveal
- Sections rise on enter: `opacity 0→1` + `reveal-rise` (translateY 12px→0) over `--dur-4` with
  `ease-out`, **staggered 60ms** per block (mark → eyebrow → title → photo → body). The compass mark
  may rotate its ticks in by 8° as it settles — subtle, once, never looping.
- Driven by `IntersectionObserver`; runs once per element.

```css
.reveal{opacity:0;transform:translateY(12px);transition:opacity var(--dur-4) var(--ease-out),transform var(--dur-4) var(--ease-out)}
.reveal.in{opacity:1;transform:none}
/* stagger via inline --i: transition-delay:calc(var(--i)*60ms) */
```

---

## 3. The compass mark, in motion

- **Load:** ticks settle by rotating 8° → 0 once, over `--dur-4`, `ease-out`. The rings fade in. Never
  spins fully, never loops.
- **Hover (interactive mark / logo link):** the center dot pulses scale `1 → 1.15 → 1` over `--dur-3`.
- **Loading state:** if ever needed, the outer ring becomes a 0.75-turn `stroke-dasharray` spinner at
  1.2s linear — used only for genuine waits, accent-colored.

---

## 4. Restraint rules

- **Respect `prefers-reduced-motion`:** disable rises, lifts, and the mark rotation; keep opacity
  fades only, ≤ 200ms.
- No parallax, no autoplay video, no looping background motion, no scroll-jacking.
- One spring in the whole system (the play-button). Everything else eases.
- Total entrance choreography on any page ≤ ~800ms. Calm is the brand.

```css
@media (prefers-reduced-motion:reduce){
  *{animation:none!important;transition-duration:.01ms!important}
  .reveal{opacity:1;transform:none}
}
```

*End of foundations. Next phase: the logo system — `../02-logo/`.*
