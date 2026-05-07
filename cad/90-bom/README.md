# 90-bom — Per-Subsystem BOM CSVs

Each subsystem maintains its own BOM CSV here, which feeds the master
`/bom/master.csv` at the project root.

## Files (planned)

- `bom-chassis.csv`
- `bom-shell.csv`
- `bom-electrical.csv`
- `bom-plumbing.csv`
- `bom-hvac.csv`
- `bom-cabinetry.csv`
- `bom-exterior.csv`

## Schema (matches `/bom/master.csv`)

```
id,subsystem,part,vendor,part_number,qty,unit_cost_usd,extended_cost_usd,status,notes
```

A small script (TBD, in `/scripts/`) will concatenate per-subsystem
files into the master. Until then, edit the master directly.
