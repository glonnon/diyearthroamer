# Cabover Livability — King vs Queen (closes O2)

## Constraint envelope

From `cad/00-vehicle/SPECS.md`:

- Shell exterior width: 2,438 mm (96")
- Shell interior width (after composite skins + insulation):
  ~2,235 mm (88")
- Cabover overhang past back-of-cab: 760 mm (30")
- Cabover front face at: cab back X − overhang
- Cabover height (interior, mattress to ceiling): 760 mm (30")
- Crew cab roof: ~80" wide × 64" long, 2,180 mm (86") off ground

## Mattress dimensions

| Size | Width | Length |
|---|---|---|
| Queen | 1,524 mm (60") | 2,032 mm (80") |
| King | 1,930 mm (76") | 2,032 mm (80") |
| Olympic queen | 1,676 mm (66") | 2,032 mm (80") |

## Width fit (interior 2,235 mm = 88")

| Size | Mattress | Side cabinets allowance | Verdict |
|---|---|---|---|
| Queen | 1,524 | 711 mm = 28" total (≈14" per side) | **Easy fit.** Big side wardrobes both sides. |
| King | 1,930 | 305 mm = 12" total (≈6" per side) | **Tight.** Only narrow shelves; wardrobes move down to main floor. |
| Olympic queen | 1,676 | 559 mm = 22" (≈11" per side) | **Sweet spot.** Decent side cubbies. |

## Length fit (front-to-back)

The mattress lies **across the truck** (driver-to-passenger), 80" long
across the **width** of the camper. Width direction is the constraint
above; **length is not constrained** by cabover depth — it's
constrained by interior shell width.

Wait — interior shell width is 88", and a queen is 60" wide × 80"
long. Layout has the **80" length running side-to-side** (occupants
sleep transverse). 80" ≤ 88" → fits.

A king is 76" wide × 80" long → still 80" running side-to-side, with
mattress depth (front-to-rear of vehicle) of 76". Cabover overhang
gives 30" past back-of-cab; the rest of the 76" sits **forward of the
cabover front face** … which doesn't exist — there's nothing forward
of the cabover front. So **king depth must fit within the cabover
platform itself** = overhang + portion behind back-of-cab inside the
shell.

Let depth budget = overhang (760 mm) + (cabover floor going rearward
into the shell until the headboard wall). Shell length 6,400 mm with
typical headboard wall ~1,200–1,400 mm aft of the cabover front:

```
Cabover floor depth = 760 mm (over cab) + 1,200 mm (rearward into shell)
                    = 1,960 mm (≈ 77")
```

So:

| Size | Required depth | Cabover depth | Verdict |
|---|---|---|---|
| Queen (depth 60") | 1,524 mm | 1,960 mm | **Fits with 17" of margin** for nightstand or step. |
| Olympic queen (66") | 1,676 mm | 1,960 mm | Fits with 11" margin. |
| King (76") | 1,930 mm | 1,960 mm | **Just barely fits** (1" margin) — no room for headboard storage. |

## Headroom (mattress to ceiling)

Cabover interior height 760 mm (30"). With a 200 mm (8") mattress on
50 mm (2") slatted base, sitting headroom = 760 − 250 = **510 mm
(20")**. Acceptable for sitting up to read; not for standing. Standard
cabover.

## Pass-through

Pass-through opens at the cabover front bulkhead (the wall facing the
back of the truck cab). Required clear opening ~600 × 600 mm
(24" × 24"). Fits in either layout.

## Recommendation

**Olympic queen (66" × 80")** — best of both worlds:

- Real per-side cabinets (~11" each side) for clothes / small items.
- 11" of depth margin behind the headboard for shelves, USB, lights.
- More comfortable than queen for two adults, without giving up
  storage like the king does.

Fallback: standard queen (60" × 80") if the Olympic-queen mattress
sourcing is awkward (it's a less common size; latex / hybrid custom
makers do offer it).

**Avoid king** — the 1" depth margin leaves no real headboard
storage and no room for radiused corners on the cabover, and storage
relocates to the main floor.

## Files

- This study informs `cad/20-shell/cabover.FCStd` (TBD).
- Once mattress size is locked, update `weight/master.csv` (mattress
  weight differs by ~10 lb between queen and king) and `bom/master.csv`.
