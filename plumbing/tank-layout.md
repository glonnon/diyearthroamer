# Fresh Tank Layout — 2× 60 gal (split) (closes O8)

## Decision

Use **two 60 gal polyethylene tanks plumbed in parallel** with a
cross-feed valve, mounted **forward of the rear axle, low and
inboard of the frame rails**, one on each side of the centerline.

This was the proposed split in REQUIREMENTS.md §8 — confirming it
here as a locked decision (ADR-0015) because it has cascading
effects on the subframe, plumbing manifold, and weight model.

## Why split

| Criterion | 1× 120 gal | 2× 60 gal (chosen) |
|---|---|---|
| Fits between frame rails | Marginal — needs custom poly | Easy — off-the-shelf 60 gal tanks fit |
| Side-to-side balance | Whatever the tank shape allows | **Perfect** — symmetric pair |
| Redundancy if tank damaged | None (lose all water) | Isolate one, keep 60 gal |
| Plumbing complexity | Simpler (one fill, one outlet) | +1 cross-feed valve, +1 fill manifold |
| CG control | Mass at one location | Flexibility on mounting points |
| Cost | Comparable | Slight premium for second tank |

The redundancy and balance benefits decisively favor the split.

## Tank specifications

| Param | Value |
|---|---|
| Quantity | 2 |
| Capacity each | 60 gal (227 L) |
| Material | Polyethylene (or HDPE), FDA potable |
| Mounting | Tank straps to subframe outriggers, rubber pads |
| Heating | 24V silicone heating pad on each tank, thermostat |
| Insulation | 25 mm closed-cell foam wrap |
| Fill | Single gravity fill manifold + city-water inlet |
| Outlet | Each tank: 1/2" outlet to common manifold; ball valve isolation |
| Vent | Each tank: 1/2" vent through wall above max waterline |
| Sender | Garnet SeeLevel capacitive (no fouling probes) |
| Drain | Bottom drain, accessible from underside |

## Cross-feed valve

```
   Tank A 60g                Tank B 60g
       |                         |
    [ball valve]              [ball valve]
       |                         |
       +----------[tee]----------+
                    |
                    | (common feed)
                    v
              [pump suction]
```

Cross-feed means: with both ball valves open, the tanks self-level
via the tee. With one closed, you isolate that tank (e.g., for
service or contamination event).

## Mounting envelope

| Tank | X (forward of rear axle) | Y (above ground) | Z (offset from centerline) |
|---|---|---|---|
| Tank A (driver / port) | +1,800 mm | +400 mm | -600 mm |
| Tank B (passenger / curb) | +1,800 mm | +400 mm | +600 mm |

Both tanks **forward of the rear axle**, in the cavity below the shell
floor and outboard of the frame rails (mounted to subframe outriggers),
inboard of the wheel wells.

Update `weight/master.csv`: replace single `Fresh water full` row with
two rows at +1,800 mm station (port/curb).

## Vendor stock sizes — pick from off-the-shelf RV tanks

Custom poly tanks are an option but expensive and slow. Most of these
suppliers stock 30–80 gal RV-grade tanks; we want a 60 gal (or near)
that fits the envelope above.

| Vendor | Model / size hint | Approx dim (in) | Notes |
|---|---|---|---|
| **Class A Customs** | various 60 gal water tanks | many shapes | broad stock; configure on site |
| **RecPro** | 60 gal fresh water tank | ~36×24×18 | RV grade, FDA potable |
| **Icon Direct** | 60 gal water | varies | OEM RV supplier |
| **Plastic-Mart** | RV60 series ~60 gal | ~36×24×18 | poly, FDA potable |
| **Plastic Direct** | RV-FW60 | ~36×24×18 | RV-specific lineup |
| **Ronco Plastics** | various 60 gal | many | poly tanks; configure to fit |
| **Plastic Tank Industries (PTI)** | RV water tanks (Canada) | various | good for cold-weather rated grades |
| **eBay / RV salvage** | OEM removed tanks | various | last resort; verify FDA |

### Selection criteria (apply to whatever stock size we lock)

- FDA-grade poly (do not use tanks rated for chemicals only).
- Total height ≤ 460 mm (18") to fit between subframe and shell floor.
- Outlet at the **bottom** (not side) for full draw.
- 1/2" or 3/4" NPT bulkhead fittings (not glued spuds).
- Vent boss at the top, ≥ 1/2" diameter.
- Fill boss with screen.
- Manufacturer warranty ≥ 5 yr.

### Procurement note

Match the **two tanks to the same model/SKU** so plumbing fittings
and dimensions are interchangeable. Order both tanks from the same
batch so wall thickness and color are consistent.

## Captured in

- **ADR-0015** — Fresh tank split.
