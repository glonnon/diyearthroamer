# DIY Earthroamer / Storyteller HILT-Class Build Requirements

A working requirements document for a DIY expedition vehicle inspired by the
Earthroamer LTi/HD and Storyteller Overland HILT. The intent is to produce
buildable specs, CAD assemblies, and shop drawings sufficient for a competent
fabricator and outfitter to execute.

## 1. Project Goals & Constraints

- **Mission profile:** 4-season off-grid use, 14+ days fully self-contained,
  remote dirt/forest service roads, snow/desert/mountain. Not rock-crawling.
- **Occupancy:** 2 adults sleeping, 4 seated DOT-compliant for travel.
- **Range targets:**
  - Fuel: 600+ mi (aux tank)
  - Fresh water: 10–14 days at 6 gal/person/day
  - Power: 5+ days no-sun, indefinite with sun
- **Build philosophy:** Marine/aviation-grade systems, all subsystems
  serviceable by owner, no proprietary lock-in where avoidable.
- **Budget envelope target:** to be set; track BOM cost per subsystem.
- **Curb weight ceiling:** stay under F550 GVWR (19,500 lb) with 20%
  payload reserve. Track running CG.
- **Weight distribution rule:** **bias mass to the forward half of the
  camper / flatbed.** Heavy items (battery bank, fresh water, fridge,
  inverter, tools) live ahead of the rear axle whenever physically
  possible. The rear half is reserved for lighter living volume,
  garage, and bikes. Goal: keep front axle within rated load and
  prevent rear-heavy handling on the F550 (long rear overhang +
  flatbed amplifies rear-bias issues). Every component in the §4
  weight model is tagged with its longitudinal station (X-coord from
  rear axle) so per-axle loads are computed continuously.

## 2. Base Vehicle — Ford F550 Flatbed

- **Chassis:** Ford F550 4x4 **flatbed (cab & chassis)**, **crew cab
  baseline** (locked) — provides 4 DOT seats and rear-cab pass-through
  geometry. Super cab or single cab remain on the table only if the
  cab-to-house pass-through analysis (§3) shows crew cab interferes
  with the cabover bed; in that case super cab is the fallback. Diesel
  (6.7L Power Stroke).
- **Flatbed:** custom aluminum flatbed (treadplate or smooth) sized to
  the chosen Globe Trekker shell length plus optional rear garage box
  (see §20). Bed integrates:
  - Subframe interface (3-point / torsion-free, see §3).
  - Side toolboxes / utility lockers along underbed rails.
  - Mud flaps, marker lights, license plate relocate.
  - Trailer wiring + 7-pin to rear.
  - Tie-down rails (8020 or aluminum extrusion) front and rear of
    shell footprint for cargo and accessory mounting.
  - Material/weight target: aluminum to keep tare low; budgeted in §4.
- **Tires:** 41" (e.g., 41x13.5R17 or 395/85R20). Verify load rating ≥
  4,400 lb/tire at vehicle weight.
- **Wheels:** 17" or 20" forged, hub-centric, correct offset for clearance.
- **Suspension:** Liquid Springs CLASS (Compressible Liquid Adaptive
  Suspension System) front and rear. Self-leveling, ride-height control.
- **Steering/brakes:** Verify brake upgrade compatible with 41s; consider
  hydroboost. Steering stabilizer.
- **Drivetrain:**
  - Re-gear axles for 41" tires (target 4.88 or 5.38 — calc from final
    drive RPM at 65 mph).
  - Verify transmission tune.
- **Fuel:** 40 gal OEM + 50–65 gal aux (Transfer Flow or Titan replacement).
- **Cab:**
  - Heated/cooled seats retained.
  - CarPlay head unit, backup + side cameras.
  - Cab-to-house pass-through? (decide; affects door design and cab seal).
- **Front bumper:** Winch-rated (16,500 lb), recovery points, integrated
  lighting, aux fuel/coolant clearance.
- **Rear bumper:** Receiver hitch (10k tow), recovery points, swing-out tire
  carrier (41" spare).
- **Skid plates:** Engine, transmission, transfer case, aux fuel.
- **Lighting:** LED headlight upgrade, ditch lights, roof bar, scene
  lighting (sides + rear).

## 3. Habitat Shell — Global Trekker 21'

- **Length (locked):** **21' habitat shell** with rear-end departure-
  angle taper, target **total exterior length ≈ 23'** including the
  tapered tail (the angled aft wall sheds frame to preserve departure
  angle and gives a small rear cargo wedge). Cabover nose extends over
  the F550 crew cab roof for the master bed (see §13).
- **Construction:** composite sandwich panels (XPS/PU core, FRP/GRP skins),
  bonded, frameless. Vendor-supplied.
- **Insulation:** R-value target ≥ R-15 walls/floor, R-20 roof. Verify
  vendor spec; supplement at penetrations.
- **Penetrations to plan in CAD before order:**
  - Entry door (location, hand)
  - Windows (count, size, locations) — dual-pane acrylic (Tern, Seitz)
  - Roof: vents, AC, solar gland(s), antennas, satellite dome
  - Walls: shore power inlet, city water, gravity fill, tank vents,
    propane locker (if any), fuel fill for diesel heater, cable glands
  - Floor: tank drains, grey/black/macerator outlets, heater intake/exhaust,
    wiring chases
- **Subframe / mounting system (locked):** **purchase the Global
  Trekker OEM subframe** matched to the 21' shell and F550 crew-cab
  flatbed. Vendor subframe handles three-point / torsion-free pivot
  mounting and is engineered to the shell. We will:
  - Confirm vendor subframe dimensions, mount-point spacing, and
    outrigger options before locking flatbed length.
  - Add owner-side outriggers / brackets for side toolboxes, steps,
    and accessory mounts where the OEM frame doesn't already provide.
  - Bonded/bolted interface with shell per vendor spec.
- **Door:** composite plug door, deadbolt + 3-point latch, screen,
  integrated steps (electric retract).
- **Awning:** 12V powered (Fiamma F80s or Thule HideAway), 12'–14',
  wind sensor, LED strip.

## 4. CAD & Documentation Requirements

- **Primary CAD requirement:** must do both world-class parametric 3D
  assembly modeling (for ergonomics, clearance, and "is this actually
  livable" walkthroughs) **and** produce production-ready CNC toolpaths
  (G-code or post-processed) for routing plywood, cutting aluminum sheet,
  and waterjet/laser parts. Single source of truth from sketch to chip.
- **Software options (ranked):**
  1. **Fusion 360 (recommended).** Strong parametric solid + sheet-metal
     + surface; integrated CAM (2.5D, 3D, multi-axis) outputs G-code for
     virtually any router/mill via post-processor library; assemblies w/
     joints; rendering + interior walkthrough; cloud collab; affordable.
  2. **SolidWorks + SolidWorks CAM / HSMWorks.** Best-in-class assemblies
     and sheet-metal; CAM is solid; expensive; weak walkthrough/render.
  3. **Onshape + partner CAM (Kiri:Moto, CAMWorks).** Browser-native,
     great for distributed teams; CAM via add-ins.
  4. **FreeCAD + Path workbench.** Free; usable for parts; weaker for
     large livability assemblies; acceptable as fallback.
- **CAM / CNC outputs required per part:**
  - Tool list, stock setup, fixturing notes
  - G-code (post-processed for the actual machine: Shaper Origin,
    Avid/ShopBot, Onefinity, Tormach, etc.)
  - DXF/SVG flat patterns for sheet aluminum (for waterjet/laser bureau)
  - PDF setup sheet w/ origin, tool changes, run time
- **Livability / human-factors deliverables:**
  - Manikin (5th–95th percentile) placed in galley, dinette, bath, bed.
  - Headroom heatmap in walking zones (≥ 76" target where reasonable).
  - Reach studies for upper cabinets (≤ 72" to top shelf usable rim).
  - Door swing + drawer pull clearance animations.
  - VR/screen walkthrough export (FBX/GLB) for client review before cut.
- **Native files + STEP exports committed to repo.** Binary CAD via
  Git LFS.
- **Top-level assembly hierarchy:**
  ```
  /cad
    /00-vehicle              F550 chassis model (vendor or scanned)
    /10-subframe             Subframe + mounts
    /20-shell                Globe Trekker shell w/ penetrations
    /30-exterior             Bumpers, racks, boxes, awning, ladder
    /40-electrical           Battery box, panels, conduit runs
    /50-plumbing             Tanks, pump bay, manifold, fixtures
    /60-hvac                 Heater, AC, ducting, vents
    /70-interior-cabinetry   Galley, dinette, bath, bed, wardrobe
    /80-finish               Flooring, wall panels, ceiling
    /90-bom                  Master BOM, weight + CG report
  ```
- **Deliverables per subsystem:**
  - 3D assembly + parts (STEP)
  - Shop drawings (PDF) with tolerances for CNC/waterjet/laser parts
  - Wiring diagrams (KiCad or similar) for electrical
  - P&ID for plumbing and HVAC
  - Cut lists for cabinetry (CSV)
- **Weight & CG model:** every component tagged with mass; running tally
  vs GVWR and per-axle limits; CG height tracked for rollover margin.
- **Clearance / interference checks:** door swings, drawer pulls, tank
  fill access, service panels, suspension travel envelope.

## 5. Electrical System

- **Architecture (locked):** **48V DC primary house bus** with a
  **24V DC sub-bus** (via 48→24V DC-DC converter, e.g., Victron Orion
  XS 48/24 or equivalent, sized ≥ 50 A continuous) for the bulk of
  house loads (lighting, fans, pumps, MaxxAirs, fridge if 24V model
  selected, control gear). A small 24→12V converter feeds any
  remaining 12V-only accessories (radio, some marine fixtures).
  120/240V AC is produced by the 48V inverter for induction cooktop,
  microwave, AC/heat pump, and shore-side appliances. The 48/24V
  split keeps conductors small on the high-power side while letting
  most cabin gear run at 24V — a sweet spot of available marine
  hardware, lower current than 12V, and no need for a giant 48→12V
  converter on every circuit.
- **House batteries (preferred):** **Epoch 48V LiFePO4 server-rack
  / wall-mount modules.**
  - Target capacity: **15–20 kWh usable** (e.g., 3–4× Epoch 48V
    100Ah modules ≈ 15.36–20.48 kWh).
  - Self-heating BMS (Epoch heated variant) for sub-freezing charging.
  - CAN/RS-485 comms to Victron Cerbo GX (closed-loop with inverter
    and MPPTs).
  - Mounted in a **vented, insulated, shock-isolated battery bay
    located in the front half of the camper / flatbed** (see weight
    distribution rule in §1) — accessible for service from an
    exterior hatch.
  - Battery bay must include: lockable disconnect, Class-T main fuse,
    bus bars, temp probes, pre-charge resistor for inverter, drip
    pan, and a fire-rated liner.
- **Fallback architecture:** 12V house bus w/ 600–1,000 Ah LiFePO4
  if 48V Epoch path is value-engineered out (track in §21 decisions).
- **Inverter/charger:** **Victron MultiPlus-II 48/5000** (preferred,
  matches 48V Epoch bank) or Quattro 48/5000 if dual AC inputs (shore
  + future generator) wanted. Pure sine, transfer switch, power assist,
  parallel-capable for future expansion.
- **Solar:**
  - **1,000–1,300 W** rooftop monocrystalline (rigid panels).
  - Mounting: bonded standoffs (3M VHB + sika), no roof penetrations
    where possible.
  - Controllers: Victron SmartSolar MPPT sized for 48V bank (e.g.,
    250/60 or 250/100 depending on array Voc/Isc).
- **Alternator charging:** high-output 12V alternator (Nations, Mechman,
  or dual-alternator) feeding a **48V DC-DC** path — either
  Wakespeed WS500 + alternator + 12→48V converter chain, or a
  purpose-built 12→48V charger (e.g., Victron Orion XS 12/48 series
  when capacity sufficient, otherwise multiple in parallel). Target
  ≥3 kW (≈60A @ 48V) of charging while driving.
- **Shore power:** 30A inlet (Smartplug), surge protector, EMS
  (Progressive Industries), galvanic isolator.
- **Distribution:**
  - DC: Blue Sea fuse blocks, ANL/MRBF battery-side fusing per ABYC.
  - AC: 120V load center, GFCI on all wet locations + exterior outlets.
- **Monitoring:** Victron Cerbo GX + GX Touch, SmartShunt, temperature
  sensors on batteries and inverter.
- **Wiring spec:**
  - Marine-grade tinned copper, ABYC color code.
  - Conduit/loom in chases; no wires touching shell skins or hot pipes.
  - Wire sizing per ABYC E-11 (3% drop critical, 10% non-critical).
  - All terminations: heat-shrink crimp, no wire nuts.
- **Grounding/bonding:** single-point DC ground at battery negative;
  AC neutral-ground bond at inverter when off shore.
- **Loads to budget (typical daily Wh):**
  - Fridge/freezer (12V, 2 cu ft + 4 cu ft): 600–900
  - Lighting (LED throughout): 100
  - Water pump, fans, controls: 200
  - Heater (diesel) blower + glow: 150
  - AC (compressor + condenser): 1,500–4,000 (when running)
  - Induction cooktop: 1,000–2,000
  - Electronics (Starlink, router, laptop): 500–1,000
- **Outlets/USB:**
  - USB-C PD (45W) at every seat, bedside, galley.
  - 120V duplex GFCI: galley (2), bath, dinette, bedside, exterior.
  - 12V cigarette/Anderson at galley and exterior.

## 6. Solar (Detail)

- **Panel layout:** model in CAD against roof penetrations; preserve
  walking lanes and AC/vent shadow-free zones.
- **Wiring:** MC4 to combiner box, 10 AWG min, fused at combiner, single
  roof gland (Scanstrut) for entry.
- **Series/parallel topology:** match MPPT Voc/Isc limits; document.
- **Tilt option:** decide; tilting brackets add ~30% winter yield but
  cost weight and complexity.
- **Portable panel input:** Anderson SB50 exterior port for 200W ground
  panel during deep canopy.

## 7. HVAC

- **Heating (preferred — hydronic):** integrated **diesel hydronic
  system** (Webasto Dual Top Evo 6/8, Espar/Eberspächer Hydronic S3
  D5E, or Timberline / Aqua-Hot 250D) providing in one loop:
  1. **Cabin furnace:** hydronic-to-air fan-coil heat exchangers
     ("hydronic furnaces") in living, bedroom, and bath, ducted via
     short runs; thermostat per zone.
  2. **Domestic hot water (DHW):** on-demand or small-tank (≈ 4 gal)
     hot water tied to galley, bath, exterior shower; mixing valve
     for scald prevention; recirculation loop optional.
  3. **Radiant floor heat:** PEX-Al-PEX tubing in the floor under
     living, galley, and bath, in aluminum heat-transfer plates
     above floor insulation, fed from the hydronic loop via a small
     manifold w/ zone valves and a thermostatic mixing valve
     (target floor surface temp 75–82 °F).
  4. **Heated towel rack:** hydronic towel warmer in the bathroom
     plumbed off the radiant loop (or a dedicated low-watt 12V/120V
     electric rail if 48V conversion losses dominate — decide in §21).
  5. **Engine pre-heat (optional):** loop tap to engine block for
     cold-start assist when plugged into shore.
  6. **Tank / wet-bay freeze protection:** small bypass loop runs warm
     fluid through wet bay in winter setback mode.
- **Fuel:** diesel from main tank (with anti-siphon + protected
  pickup) or a dedicated day tank in the service bay.
- **Backup / shoulder season:** 120V AC element in the hydronic
  reservoir for shore-power-only DHW + light radiant without firing
  the burner.
- **Air-only fallback:** standalone diesel air heater (Webasto Air Top
  2000 STC or Autoterm Air 2D) retained as a redundant cabin heat
  source if hydronic system is value-engineered out — track in §21.
- **Controls:** single touchscreen thermostat (Truma CP Plus, RV-C, or
  custom on Cerbo GX) with per-zone setpoints, schedule, and
  vacation/freeze modes; remote control via app over Starlink/cell.
- **Cooling (preferred — mini-split heat pump):** **12/24/48V DC
  mini-split heat pump** (Mabru SCS 12000 BTU 48V, Velit 24V mini-split,
  or marine split such as Webasto FCF Platinum 16,000) — quieter,
  lower roof profile, dual-mode (cooling + supplemental heat in
  shoulder seasons), and low DC draw at part-load. Indoor head wall-
  or ceiling-mounted in living area; outdoor condenser in a vented
  external locker on the flatbed or in a recessed exterior bay.
  - Sized for ~9,000–13,500 BTU; verify against shell heat-load calc.
- **Cooling (fallback):** 48V or 24V rooftop unit (Nomadic Cooling 24V,
  RecPro RPAC-12V, or similar low-profile RV unit) if the mini-split
  install footprint or condenser placement doesn't pencil out.
- **Ventilation:**
  - MaxxAir Deluxe fans ×2 (over galley and bed), reversible, rain cover.
  - Cross-flow openable windows.
  - Bathroom exhaust fan ducted to roof.
- **Engine heat reuse (optional):** coolant loop heat exchanger to DHW
  tank when driving.
- **Combustion air & exhaust:** all heater intakes/exhausts properly
  isolated from cabin; CO detector mandatory.
- **Insulation augmentation:** thermal break at all penetrations,
  thermal curtain at cab pass-through.

## 8. Plumbing (Fresh Water)

- **Fresh tank:** **100–120 gal**, polyethylene (or welded poly/HDPE
  custom-shape), baffled, bottom drain, vented, mounted low and
  centered for CG. Heated pad + insulation. May be split across two
  tanks (e.g., 60 + 60) plumbed in parallel with cross-feed valve to
  fit chassis envelope and balance side-to-side weight.
  - **Weight note:** 120 gal fresh ≈ 1,000 lb. Account for full vs
    empty CG shift in §4 weight model; mount as low and as close to
    the rear-axle / centerline as possible.
- **Fill:** gravity (lockable) + pressurized city inlet w/ regulator
  (45 psi). Anti-siphon/check valve.
- **Pump:** variable-speed Shurflo Aqua King II or Remco Aquajet RV,
  accumulator tank, mounted on vibration isolators in service bay.
- **Filtration:**
  - Inlet: sediment 5 µm.
  - Under-galley: carbon block + UV (Acuva) for potable.
- **DHW:** sourced from the hydronic system in §7 (preferred). Tank
  or on-demand fallback options: Isotemp 6 gal (engine + 120V) or
  PrecisionTemp RV-550 if hydronic value-engineered out.
- **Distribution:** PEX-A with expansion fittings, color-coded (red/blue),
  manifold w/ shutoffs per fixture, freeze drain at low points.
- **Fixtures:**
  - Galley: single-lever w/ pull-down sprayer, separate filtered tap.
  - Bath: thermostatic shower valve, hand-held wand, pause valve.
  - Exterior shower: hot/cold quick-connect, locking door.
- **Winterization:** heated bays for tanks/pump; heat trace on exterior
  runs; blow-out fitting; antifreeze loop.

## 9. Sewer / Waste

- **Toilet:** porcelain or china RV-style flush toilet (Dometic 320
  or Thetford Aqua-Magic Style II Plus) plumbed to a real black tank.
  (Composting toilet retained as an open option in §19 — current
  baseline is a black-tank system per owner direction.)
- **Black tank:** **30–40 gal**, polyethylene, heated pad + insulation,
  3" outlet to common dump valve, full-size cleanout, sensor (Garnet
  SeeLevel — capacitive, no probes that foul), tank rinse / spray
  wand, vent through roof (true vent, not AAV), high enough above
  toilet to avoid trap pull.
- **Grey tank:** **30–40 gal**, heated, baffled, bottom drain to 3"
  sewer termination + macerator option (Sani-Con / SewerSolution) for
  remote dump and uphill / pressurized discharge.
- **Dump station:** common termination panel w/ separate gate valves
  for black and grey, lockable hatch, 3" bayonet + macerator quick-
  connect, hose storage in adjacent service bay.
- **Galley + bath grey:** P-traps at every fixture, true roof vents
  preferred; AAVs only where a roof vent is geometrically impossible.
- **Black water best practices:**
  - Always-closed black valve, dump grey *after* black to flush hose.
  - Tank treatment dispenser bay (enzymes, no formaldehyde).
  - Toilet supplied with on-demand water from fresh system; spray
    wand on dedicated valve, vacuum breaker per code.
- **Tank weight note:** 40 gal black + 40 gal grey ≈ 670 lb when full.
  Combined with 120 gal fresh, plan for ~1,700 lb of fluids. Include
  full-tank case in §4 weight + CG model.
- **Trash/recycling:** dedicated bins under galley, vented.

## 10. Kitchen (Galley)

- **Layout:** galley-aisle along curb side; counter run 6–8 ft.
- **Cooktop:** 2-burner induction (Empava or True Induction), 120V from
  inverter; no propane on board. Vented range hood (recirculating + duct).
- **Oven (optional):** 120V convection microwave (Contoure) above cooktop
  or in island.
- **Refrigeration:**
  - Main: 12V compressor fridge 5–7 cu ft (Isotherm Cruise 130, Vitrifrigo
    DP150i drawer, or Dometic CRX).
  - Freezer: separate drawer 1.6 cu ft (Isotherm) or combo unit.
- **Sink:** single deep stainless (16" x 18"), undermount, with cover
  insert that doubles as cutting board.
- **Faucet:** marine pull-down + dedicated filtered tap.
- **Countertop:** solid surface (Corian) or compact laminate (Fenix);
  avoid stone (weight).
- **Storage:**
  - Drawers (Blum Tandembox w/ Tip-On or full-extension w/ latches).
  - Pantry tower w/ pull-out bins.
  - Spice drawer near cooktop.
  - Knife block magnetic, recessed.
  - Trash + recycling pull-outs.
- **Lighting:** under-cabinet LED, dimmable, 2700K + 4000K dual.

## 11. Bathroom

- **Type:** dry bath if 21' shell allows; wet bath in 19'.
- **Shower:**
  - Pan: molded composite or fiberglass, 30"x30" min, low-threshold drain.
  - Walls: FRP or composite panel, sealed seams.
  - Door/curtain: bi-fold or magnetic curtain.
- **Toilet:** composting (see §9).
- **Sink:** small vessel or molded counter, 12"–14".
- **Vanity:** drawers + open towel bar.
- **Mirror:** medicine cabinet w/ LED.
- **Ventilation:** dedicated exhaust fan, humidity-triggered.
- **Floor:** non-slip vinyl or rubber, fully coved up walls 4"; **heated
  via hydronic radiant loop (§7)** with its own zone valve.
- **Heating:** hydronic fan-coil + radiant floor; **heated towel rack**
  (hydronic preferred, electric fallback) on the wall opposite the
  shower.

## 12. Living Area

- **Dinette:**
  - U-shape or face-to-face for 4, table on lagun or pedestal mount.
  - Two seats DOT-rated w/ 3-point belts (forward-facing) — coordinate
    with shell vendor for hard points.
  - Storage under all benches, top-loading + front access.
- **Table:** removable, drops to form bed extension (if convertible).
- **Windows:** insulated shades (MCD or Lippert dual-pane shade), one
  large curb-side picture window.
- **Lighting:** dimmable warm-white overhead + accent + reading lights at
  every seat.
- **Entertainment:**
  - 24"–32" 12V TV on swivel/lift mount.
  - Sonos or marine soundbar, in-ceiling speakers (×4).
- **Connectivity:**
  - Starlink Mini or Standard, motorized stow option.
  - Pepwave or Peplink router w/ cellular (dual SIM), Wi-Fi 6.
  - Cat6 to TV, router, workstation.

## 13. Bed / Sleeping

- **Configuration (locked):** **fixed cabover bed** in the nose of the
  shell, mounted **over the F550 crew cab roof**, classic Earthroamer-
  style. Target **king (76"x80") if the cabover footprint allows**,
  otherwise queen (60"x80"). Permanent — no conversion. Headroom
  ≥ 28" above mattress at the rear edge, sloping forward as needed.
  - Pass-through to the cab from the front of the cabover, gasketed
    and insulated, opens onto the rear bench area of the crew cab.
  - Bed access: 2-step plus grab handles from the main floor; lower
    edge ≈ 36–40" off finish floor.
- **Mattress:** custom latex or hybrid, 8"–10", removable cover, vented
  base (slats or coir mat) to prevent condensation.
- **Storage under:** garage access from rear hatch + interior lift-top.
- **Headboard:** padded, with USB-C, switches, reading lights, small
  shelf, fan control.
- **Wardrobe:** full-height hanging + drawers, ≥ 18" depth.
- **Window over bed:** opening, screened, insulated cover.

## 14. Exterior Storage & Accessories

- **Service bay:** curb-side exterior locker housing pump, manifold,
  shore inlet, filters, hose storage.
- **Generator bay:** none planned (battery + solar). Reserve space for
  future EcoFlow/portable.
- **Storage boxes:** outriggers + side boxes for recovery gear, tools,
  leveling blocks, hose, electrical cords.
- **Roof rack / deck:** walkable composite deck w/ rail, ladder access,
  mounts for traction boards, awning, antennas.
- **Bike/gear:** see §23 — rear bike garage is a primary design driver.
- **Spare tire:** rear swing-out for 41" spare; verify CG and door clearance.
- **Recovery:** Maxtrax ×2, kinetic rope, soft shackles, tree saver,
  bottle jack rated to GVWR, recovery board mounts.

## 15. Lighting (Whole Vehicle)

- **Interior:** 12V LED, dimmable, scene presets (cook / dine / movie /
  night / red).
- **Exterior:**
  - Porch light at door, motion-trigger option.
  - Awning LED strip, RGBW.
  - Scene lighting both sides + rear (white + amber).
  - Off-road bar (forward), pod lights (sides), reverse pods.
- **Control:** centralized via switched panel + app (Garnet SeeLevel +
  Victron + Firefly G15 or simple Blue Sea panel — decide complexity).

## 16. Safety, Detection, Compliance

- **Detectors:** smoke, CO, propane (if any), fresh-water leak (under
  pump and manifolds).
- **Fire suppression:** ABC extinguisher at door + galley; consider
  automatic system in battery and engine bays.
- **Egress:** entry door + emergency egress window over bed (RVIA spec).
- **Seatbelts:** 3-point at all designated travel seats, anchored to
  shell hard points per FMVSS 209/210.
- **Electrical compliance:** ABYC E-11, NEC 551 for AC.
- **LP (if used):** NFPA 1192. Recommend none — go all-electric.
- **Plates/registration:** RV / motorhome conversion docs, weight
  certificate, possibly self-certification as motorhome per state.

## 17. Connectivity & Electronics

- **Comms:** Starlink + dual-carrier cellular failover; ham/GMRS radio
  with external antenna.
- **Navigation:** dash tablet (Gaia, OnX) w/ GPS puck.
- **Cameras:** front, rear, side (blind-spot), interior pet cam.
- **Security:** door/window contacts, motion, GPS tracker w/ geofence,
  remote disable.

## 18. Materials & Finishes

- **Floor:** luxury vinyl plank (waterproof) rated for radiant heat,
  laid over the hydronic radiant assembly (heat-transfer plates +
  PEX-Al-PEX in grooved subfloor) per §7; full perimeter sealed.
- **Walls:** painted FRP or upholstered panels at impact zones.
- **Ceiling:** acoustic fabric or FRP, integrated lighting tracks.
- **Cabinetry:** **hybrid aluminum + plywood construction** (see §22).
- **Hardware:** Southco compression latches, Blum hinges, Accuride
  locking slides for travel.
- **Fasteners:** stainless throughout; Loctite per spec.
- **Adhesives/sealants:** Sikaflex 252/295 for structural/glazing,
  3M 5200 marine for through-hulls equivalents.

## 19. Cabinetry — Hybrid Aluminum + Plywood System

Cabinets are built as a **hybrid system**: aluminum structural skeleton
+ plywood panels and faces. Goal is marine durability, low weight,
serviceability, and a warm interior look — without the brittleness of
all-ply RV cabinets or the cold/industrial feel of all-aluminum.

- **Aluminum members:**
  - **Frames & ladders:** 6061-T6 1.5"x1.5"x1/8" angle or 8020-style
    structural extrusion (1515 or 1530 series) for cabinet boxes that
    take dynamic loads (galley, wardrobe, bed base, garage walls).
  - **Sheet:** 0.080"–0.125" 5052 H32 aluminum for backs of high-load
    boxes, mounting plates, drawer bottoms in heavy-use locations
    (tool drawer, fridge slide).
  - **Connections:** rivet-nuts + machine screws (serviceable), bonded
    w/ Sika 252 at structural joints; no permanent welds where service
    access matters.
  - **Mounting to shell:** L-brackets through aluminum frame to
    composite-panel inserts (no fasteners directly into foam core);
    floating attachment to allow for thermal expansion + chassis flex.
- **Plywood members:**
  - **Material:** Baltic birch (12-ply, 18 mm) for structural panels;
    9 mm or 12 mm for non-structural backs, dividers, drawers.
  - **Lightweight option:** poplar-core or okoume marine ply where
    weight matters and load is low.
  - **Faces & doors:** plywood with HPL/PPL laminate, veneer + waterborne
    poly, or Fenix NTM for premium areas.
  - **Edges:** PVC or solid hardwood edge banding; all exposed edges
    sealed against moisture.
- **Assembly conventions:**
  - Aluminum frame carries the load; plywood is captured in the frame
    via T-slot nuts (8020) or in dadoes/rabbets clamped by aluminum
    angle. Plywood is replaceable without disassembling the frame.
  - All hardware is removable (no glue-locked plywood-only joints in
    structural cabinets).
  - Drawers: plywood boxes on Accuride 3832 or Blum Movento w/ Tip-On
    + travel-rated locks (push-latch + secondary detent for off-road).
  - Doors: Blum Clip-Top hinges w/ blumotion + secondary catch.
- **CNC strategy:** all plywood parts cut on CNC router from nested
  sheets (DXF + G-code from CAD); aluminum extrusion cut on miter
  saw or CNC-cut to length; sheet aluminum laser/waterjet from
  exported DXF (see §4). Cut lists + nesting plans live in
  `/cad/70-interior-cabinetry/cnc/`.
- **Fire/finish:** plywood interiors sealed to limit off-gassing;
  finishes low-VOC, food-safe in galley.
- **Serviceability target:** any drawer slide, door, or panel
  replaceable in < 30 min with hand tools.

## 20. Bike Carry — Enclosed Lift-Box

Locked: the bike carry system is an **enclosed, weather-tight,
exterior bike box** mounted on a **motorized lift mechanism** that
raises and lowers the box for loading/unloading. Carries **2–3 high-
end mountain or gravel bikes**. No flatbed garage box.

- **Mounting:** rear of the vehicle, on a hitch-class structural
  carrier tied into the frame and (if needed) the subframe outriggers.
  Reference designs: **StowAway / Lippert lift-style cargo carriers**,
  **Hydralift motorcycle lift** (scaled), and **Aluminess motorized
  rack** kinematics adapted to a fully enclosed box.
- **Lift mechanism:**
  - **Drive:** dual 24V or 48V linear actuators (Progressive Auto
    1500-lb class) or a 12V/24V hydraulic micro-pack — choose based
    on duty cycle and silence. Manual override crank required.
  - **Travel:** ground-level loading position to ≥ 18" road clearance
    in stowed/travel position; fully retracted bike box must clear
    departure-angle envelope of the 23' total length.
  - **Safety:** mechanical travel locks engage in stowed and loaded
    positions (do not rely on actuators alone); end-of-travel
    limit switches; pinch sensors; key/PIN to operate.
  - **Interlocks:** vehicle-in-park required to deploy; rear lights
    repeated on the box; box latched closed before lift travel.
- **Box construction:**
  - Aluminum frame (1.5"–2" square tube) clad in 0.090" 5052 sheet,
    insulated lid, gas-strut top-hinged hatch (or twin barn doors
    for full bike load-in).
  - Interior: aluminum L-track on floor + walls; floor rubber/Line-X
    over diamond plate; drain ports.
  - Sealing: marine compression gasket at hatch; vehicle-side
    weather skirt where the box meets the vehicle in stowed
    position.
  - Lighting: LED dome + work light. 12V/24V outlets and USB-C PD
    for chargers (e-bike chargers powered when shore-tied; box
    isolates load from house bus on battery to limit drain).
- **Capacity / interior dimensions:** ≥ 75" L x 50" W x 36" H clear,
  load capacity ≥ 250 lb (3 bikes + accessories).
- **Maintenance access:** removable side panel for actuator/hydraulic
  service; grease points labeled.
- **Failure mode:** a stuck lift in the travel position must still
  allow the vehicle to be driven safely; a stuck lift in the load
  position must allow manual cranking to travel position with hand
  tools only.
- **Internal garage requirements:**
  - **Capacity:** 2–3 bikes, wheel base up to 1,250 mm, tire up to
    29x2.6 (MTB) or 700x50 (gravel), bar width up to 800 mm.
  - **Interior dimensions target:** ≥ 75" L x 50" W x 36" H clear in
    the garage zone.
  - **Door:** rear barn or single hatch, gas-strut assisted, weather
    seal, lockable from inside and outside; door rated for awning /
    work-shelf use (gas struts hold it open as a workspace).
  - **Bike retention:** wall-mounted fork mounts (Kuat / Yakima
    HighRoller-style) or floor-mounted thru-axle anchors w/ rear
    wheel straps. Bikes ride wheels-on or fork-mounted, owner choice.
  - **Floor:** aluminum diamond plate or Line-X over ply, with drain
    channels and ramped threshold.
  - **Ventilation:** dedicated 12V fan, vented to outside, separate
    from cabin air to keep mud/dust out of the living space.
  - **Lighting:** LED strip + work light, motion-on.
  - **Power:** 12V outlet + 120V GFCI for chargers (e-bikes, lights),
    ANT+/USB for bike computers.
  - **Wash-down:** outdoor shower hose can reach garage threshold for
    rinsing bikes before loading.
  - **Garage / cabin separation:** insulated bulkhead with gasketed
    pass door so bikes/dirt don't migrate into the living area.
- **External motorized rack requirements:**
  - **Reference designs:** Aluminess motorized swing-arm bike rack,
    Owl Vans bike rack, custom 8020 + linear actuator solution.
  - **Drive:** 12V linear actuator or motorized hinge, 1,000+ lb
    rated, with manual override crank.
  - **Capacity:** 2–3 bikes, 60–75 lb each (e-bike-capable: 80 lb
    each w/ tray-style platforms).
  - **Mount:** to rear bumper / 2.5" hitch + secondary support
    arm; must clear 41" spare carrier and rear door swing.
  - **Stowed position:** within vehicle width (96" max) and not
    blocking lights, license plate, or rear door (or interlocked so
    the door cannot open until rack swings out).
  - **Locks:** integral cable + tray lock, plus rack-to-vehicle lock.
  - **Departure angle:** stowed rack must not reduce departure angle
    below 28°.
  - **Lighting:** repeater tail/brake/turn LEDs on rack itself.
- **Bike-related ancillary requirements:**
  - **Tools/workstand:** dedicated drawer for bike tools (multi-tool,
    chain tool, pump, tubeless plug kit, torque wrench), and an
    external mount for a portable workstand (Feedback Sports Pro Elite).
  - **Charging:** 4x USB-C PD outlets in garage for lights/Garmin/Di2,
    plus 2x 120V for e-bike chargers (sized for 750W e-MTB charger).
  - **Helmet/shoe storage:** ventilated cubbies near garage door.
  - **Wet kit:** drying line + heated rail in garage for chamois/jerseys.
- **Weight budget impact:** 3 bikes ≈ 90–240 lb + rack/garage
  hardware ≈ 80–150 lb. Track in §4 weight model.

## 21. Decisions Log

### Locked (this round)

| # | Decision | Choice |
|---|---|---|
| D1 | Cab style | **Crew cab** (super cab fallback only if cabover/pass-through analysis fails) |
| D2 | Shell length | **21' habitat** + tapered tail, **23' total exterior** |
| D3 | Subframe | **Buy Global Trekker OEM subframe** |
| D4 | Cab-to-house pass-through | **Yes** |
| D5 | Bus voltage | **48V primary + 24V sub-bus** (12V only for legacy accessories) |
| D6 | House batteries | **Epoch 48V LiFePO4**, 15–20 kWh usable |
| D7 | Heating | **Diesel hydronic** providing both **air heat and water heat** (Webasto Dual Top / Aqua-Hot class) |
| D8 | Heated towel rack | **Hydronic, off the diesel heater** |
| D9 | Heated floors | **Yes — hydronic radiant** in living/galley/bath |
| D10 | Toilet | **Flush toilet + black tank** (30–40 gal) |
| D11 | Fresh water | **100–120 gal** |
| D12 | Grey water | **30–40 gal** |
| D13 | AC | **Mini-split heat pump preferred**, rooftop fallback |
| D14 | Solar target | **1,000–1,300 W** rooftop |
| D15 | Bed | **Fixed cabover bed**, king if fits else queen |
| D16 | Cabinetry | **Hybrid aluminum + Baltic birch plywood** |
| D17 | Bike carry | **Enclosed motorized lift-box** at the rear (no flatbed garage) |
| D18 | CAD stack | **Stack A — FreeCAD + KiCad + Blender + Inkscape + draw.io** (all OSS) |

### Still open

All headline architectural decisions O1–O8 are now closed:

1. ~~O1 — Flatbed material~~ **Closed: aluminum (6061-T6 + 5052-H32).
   See ADR-0013 and `cad/10-subframe/flatbed-material.md`.**
2. ~~O2 — King vs queen cabover bed~~ **Closed: Olympic queen
   (66" × 80"). See ADR-0011 and `cad/20-shell/cabover-fit.md`.**
3. ~~O3 — Mini-split~~ **Closed: Mabru SCS 12000 (48 V DC).
   See ADR-0010 and `hvac/heat-load.md`.**
4. ~~O4 — Hydronic unit~~ **Closed: Webasto Dual Top Evo 8.
   See ADR-0009 and `hvac/heat-load.md`.**
5. ~~O5 — Lift mechanism drive~~ **Closed: dual electric linear
   actuators (Linak LA36 / Progressive Auto PA-04 class). See
   ADR-0012 and `cad/30-exterior/liftbox-kinematics.md`.**
6. ~~O6 — Roof solar layout / tilt~~ **Closed: 4× 320W flat 2×2,
   no tilt. See ADR-0014 and `cad/30-exterior/solar-layout.md`.**
7. ~~O7 — CAD tooling~~ **Closed: Stack A (FreeCAD + KiCad + Blender +
   Inkscape + draw.io). See §24 and `/decisions/0008-cad-stack.md`.**
8. ~~O8 — Fresh water tank split~~ **Closed: 2× 60 gal in parallel.
   See ADR-0015 and `plumbing/tank-layout.md`.**

Remaining picks are vendor / fab-shop selections (final mattress
maker, flatbed vendor or fab shop, exact Webasto sub-options, etc.).
Those land as ADRs when chosen.

## 22. Build Phases (Suggested)

1. **Design freeze:** CAD complete, weight model green, BOM costed.
2. **Chassis prep:** tires, suspension, regear, bumpers, aux fuel.
3. **Subframe fab + install.**
4. **Shell delivery + mount + penetrations sealed.**
5. **Rough-in:** wiring chases, plumbing runs, HVAC ducts, tanks.
6. **Insulation augmentation + vapor strategy.**
7. **Cabinetry CNC + dry-fit.**
8. **Wet systems commissioning + pressure tests.**
9. **Electrical commissioning + load tests.**
10. **Finish carpentry, upholstery, trim.**
11. **Shakedown trips (3 progressively longer) + punch list.**
12. **Final weigh + CG verification + registration.**

## 23. Repository Layout (Proposed)

```
/REQUIREMENTS.md          this document
/decisions/               numbered ADRs for each open decision
/cad/                     see §4
/electrical/              schematics, panel schedules, load calc
/plumbing/                P&ID, fixture schedule, tank specs
/hvac/                    heat-load calc, ducting, BOM
/bom/                     master BOM CSV + per-subsystem
/weight/                  CG and weight-tracking spreadsheet
/build-log/               photos and notes per phase
/vendor-docs/             datasheets, install manuals
```

## 24. CAD Tooling & File Format Strategy

### 24.1 Tool comparison (free / low-cost / OSS focus)

| Tool | License | Strengths | Weaknesses | Fit |
|---|---|---|---|---|
| **FreeCAD 1.0+** | Free, OSS (LGPL) | True parametric solid + sheet metal + assembly (Assembly4/Ondsel); integrated **Path workbench** for CAM/G-code; KiCad-friendly; runs offline; no IP lock-in | Steeper learning curve; large assemblies need discipline; CAM postprocessors per machine | **Primary OSS path.** Fully capable of this build with care. |
| **Ondsel ES** *(now sunset, code merged into FreeCAD)* | OSS | Polished FreeCAD distribution + cloud collab | Project ended 2024 — features migrating into mainline FreeCAD | Use mainline FreeCAD; track Ondsel's contributions. |
| **Fusion 360 Personal Use** | Free (gratis) for hobby/non-commercial | Industry-grade parametric + sheet metal + **integrated CAM** + rendering; large post-processor library; cloud collab | Not OSS; recent restrictions (10 active editable docs, limited rapid-stop/feed CAM, no nesting in free); license can change; commercial use requires paid tier | Strong if hobby-eligible and Autodesk's restrictions are tolerable. |
| **Onshape Free** | Free (gratis) | Full parametric assemblies in browser; great collab | **Free tier makes documents PUBLIC** — major IP issue for a custom build; no integrated CAM (use Kiri:Moto add-in) | Avoid unless you accept public docs. |
| **SolidWorks for Makers** | $48/yr, makers-only | Industry standard; great assemblies + sheet metal + CAM (HSMWorks/SW-CAM available) | Non-commercial only at this price; Windows-only; no Linux | Reasonable middle path if you stay non-commercial. |
| **Plasticity** | Paid one-time (~$149 indie) | Fast direct/sub-D modeling; great for furniture-shape exploration | No real CAM; weaker on engineering drawings; Windows/Mac | Useful as a *concept* tool feeding STEP into FreeCAD/Fusion. |
| **Blender** | Free, OSS (GPL) | Best-in-class **rendering and walkthroughs** (Cycles/Eevee, VR via add-ons); good mesh tools | Not parametric; not for production engineering | **Use as the visualization stage** for livability review. |
| **OpenSCAD** | Free, OSS (GPL) | Script-driven, great for parametric brackets/jigs | Not assembly-grade for large interiors | Niche, for parametric small parts only. |
| **LibreCAD / QCAD CE** | Free, OSS | Solid 2D drafting, DXF clean output | 2D only | Useful for shop drawings if FreeCAD's TechDraw is awkward. |
| **KiCad** | Free, OSS | Best-in-class **electrical schematics and PCB**; rich symbol/footprint libraries | Not for vehicle wiring harness diagrams natively (works fine for schematics + we draw harness in FreeCAD/Inkscape) | **Use for §5 electrical schematics and any custom PCBs.** |
| **Kiri:Moto** | Free, OSS (browser) | Quick **CAM** for routers/lasers/mills; reads STL/STEP; runs in browser | Less powerful than Fusion/HSMWorks for complex 3D toolpaths | Good companion CAM if main CAD lacks it. |
| **CAMotics** | Free, OSS | G-code **simulator** (verify before machining) | Not a CAM authoring tool | Sanity-check every run. |
| **Inkscape** | Free, OSS | SVG/DXF authoring for laser/waterjet | Not 3D | Vector cleanup for sheet-aluminum nesting. |
| **draw.io / diagrams.net** | Free | P&ID, block diagrams, network/AV layout | Not engineering-grade | Use for system diagrams (plumbing P&ID, network, AC distribution one-line). |

### 24.2 Recommended tool stack (decision: O7 — proposed)

Choose **one of two coherent stacks** and commit to it:

- **Stack A — fully open-source (recommended for IP control, no
  vendor lock):**
  - **FreeCAD 1.x** for all 3D mechanical: shell penetrations, subframe,
    cabinetry assemblies, plumbing routing, brackets.
  - **FreeCAD Path** + **Kiri:Moto** for CAM/G-code per machine.
  - **CAMotics** to simulate every G-code file before cutting.
  - **KiCad** for electrical schematics (§5).
  - **Inkscape** for DXF/SVG cleanup of sheet parts.
  - **Blender** for renders, walkthroughs, VR review of livability.
  - **draw.io** for plumbing P&ID, AC one-line, network diagram.
  - **LibreOffice Calc** (or Google Sheets) for BOM and weight model.

- **Stack B — Fusion 360 Personal + OSS satellites (recommended if
  hobby-license eligibility holds and Autodesk's terms are acceptable):**
  - **Fusion 360 Personal Use** as the primary CAD + CAM (one tool).
  - **KiCad** for electrical (Fusion's electrical is less mature for
    vehicle wiring).
  - **Blender** for cinematic renders/walkthroughs (import via STEP→GLTF).
  - **draw.io** for system diagrams.
  - **LibreOffice Calc** for BOM/weight.

Either stack must produce the same canonical export set (§24.3).

### 24.3 File format strategy

- **Source of truth (per part/assembly):** native CAD file
  (`.FCStd` for FreeCAD, `.f3d` for Fusion). Stored in Git via
  **Git LFS** (binary, large).
- **Neutral 3D exchange:** **STEP AP242** for every released part and
  assembly. Committed alongside the native file. STEP AP214 acceptable
  if AP242 unavailable in the chosen tool. Avoid IGES.
- **Mesh exchange (visualization, 3D print, marketing renders):**
  **glTF 2.0 (.glb)** preferred for web/Blender; **STL** only for 3D
  printing.
- **Drawings:** **PDF** (vector) for shop drawings; **DXF (R2018)** for
  2D source feeding lasers/waterjet/CNC routers.
- **CAM:** **G-code** files committed per machine, named
  `<part>__<machine>__<post>.nc`. Setup sheet PDF alongside.
- **Electrical:** KiCad project committed natively + **PDF schematic**
  + **CSV BOM** + Gerbers (if any PCBs).
- **Diagrams:** draw.io `.drawio` source + exported **PDF** + **PNG**.
- **Spreadsheets:** **CSV** is canonical (diff-friendly); `.ods`/`.xlsx`
  optional.
- **Documents:** Markdown (`.md`) for everything human-readable
  (this document, ADRs, build log).

### 24.4 Versioning & repo conventions

- **Source-only repo, no Git LFS.** Only text-form sources are
  committed (`.FCMacro`, `.mmd`, `.kicad_pro`, `.kicad_sch`,
  `.kicad_sym`, `sym-lib-table`, `*.csv`, `*.md`, `*.py`, `*.sh`,
  `*.ps1`, `Makefile`). Every binary or rendered artifact (`.FCStd`,
  `.step`, `.glb`, `.dxf`, `.pdf`, `.svg`, `MASTER.*`) is regenerated
  on demand via the top-level `Makefile` and helper scripts under
  `scripts/`. See `HOWTO.md` for the workflow.
- **Branching:** `main` is releasable; design work on
  `design/<area>` branches; merge via PR with CAD review.
- **Tagging:** semantic-ish tags per design freeze, e.g.
  `cad-2026.05-design-freeze-1`.
- **Decision records (ADRs):** one Markdown file per locked decision
  in `/decisions/NNNN-<slug>.md` capturing context, options, and
  rationale (mirrors §21 table at point-in-time).

### 24.5 Export checklist (every part release)

For each part or assembly cut release, the repo must contain:

- [ ] Native CAD file (LFS)
- [ ] STEP AP242 export
- [ ] PDF shop drawing (dimensioned)
- [ ] DXF (if 2D-cut part) or G-code + setup PDF (if CNC part)
- [ ] Mass + station-X entry in `/weight/master.csv`
- [ ] BOM line in `/bom/master.csv`
- [ ] glTF preview for review
