# 00-vehicle — F550 Chassis Model

Master geometry for the Ford F550 4x4 crew cab cab-and-chassis. This
is the reference everything else attaches to.

## Inputs needed

- Frame rail width, height, top-of-frame Z, length to back of cab.
- Wheelbase (decision pending; 169" / 176" / 192").
- Cab roof height + roof corners (for cabover pass-through).
- Rear-axle centerline location (origin reference, see `/cad/README.md`).
- Tire OD (41") and track width.
- Liquid Springs ride height range.

## Files (planned)

- `f550-chassis-master.FCStd` — sketch-only master with ground plane,
  axle centerlines, frame top plane, cab volume, tire envelopes.
- `f550-chassis-master.step` — neutral export.

## Sources

- Ford body builder's guide for current MY F550.
- Liquid Springs CLASS install dimensions.
- Photogrammetry / tape measurement once chassis is on-hand.
