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

## 2. Base Vehicle — Ford F550

- **Chassis:** Ford F550 4x4, regular or crew cab (decide; affects shell
  length and pass-through). Diesel (6.7L Power Stroke).
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

## 3. Habitat Shell — Globe Trekker 19' or 21'

- **Decision pending:** 19' vs 21'.
  - 19': better departure angle, lighter, tighter interior.
  - 21': permanent bed + dinette possible without conversion.
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
- **Subframe / mounting system:**
  - Three-point or torsion-free pivot mount (e.g., Multidrive, GTV,
    Earthcruiser-style) to decouple chassis flex from box.
  - Material: 3" x 5" rectangular tube, A500 Gr B or aluminum (weight calc).
  - Outriggers for storage boxes and steps.
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

- **Architecture:** 12V DC house bus, 120V AC inverter sub-panel, 48V
  optional for AC + induction (decide based on load study).
- **House batteries:**
  - LiFePO4, 600–1,000 Ah @ 12V (or 200–400 Ah @ 24/48V).
  - Heated cells (self-heating BMS) for cold-weather charging.
  - Battery box: vented, insulated, shock-mounted, accessible.
- **Inverter/charger:** Victron MultiPlus-II 12/3000 (or 48/5000 if 48V).
  Pure sine, transfer switch, power assist.
- **Solar:**
  - 800–1,200 W rooftop monocrystalline (rigid panels).
  - Mounting: bonded standoffs (3M VHB + sika), no roof penetrations
    where possible.
  - Controllers: Victron MPPT, sized per array (e.g., 100/50 or 150/70).
- **Alternator charging:** DC-DC (Victron Orion-Tr Smart 12/12-30 ×2 or
  Wakespeed regulator + high-output alternator for ≥120A house charging).
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

- **Heating:**
  - Primary: diesel air heater (Webasto Air Top 2000 STC or Autoterm
    Air 2D), tapped from main fuel tank or dedicated 2.5 gal day tank.
  - Ducted to: living, bath, bed, wet bay (freeze protection).
  - Combi unit option: Truma Combi D6 (heat + DHW one box) — strongly
    consider for space and BTU efficiency.
- **Cooling:**
  - Rooftop: Nomadic Cooling 24V or Rigid Marine RV3000 12V (low-profile,
    runs on battery).
  - Alternative: marine split (Mabru, Webasto FCF) for quieter, lower
    profile, but heavier install.
  - Sized for ~9,000–13,500 BTU; verify against shell heat-load calc.
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
- **DHW:** Truma Combi D6 (preferred) or Isotemp 6gal (engine + 120V).
  On-demand options (PrecisionTemp RV-550) if propane allowed.
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
- **Floor:** non-slip vinyl or rubber, fully coved up walls 4".
- **Heating:** ducted from main heater + small toe-kick vent.

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

- **Configuration:** permanent east-west queen (60"x74") in 21'; or
  north-south + dinette conversion in 19'.
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

- **Floor:** luxury vinyl plank (waterproof) over thin underlayment;
  full perimeter sealed.
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

## 20. Rear Bike Garage / Bike Carry System

A primary design driver, not an afterthought. The vehicle must carry
**2–3 high-end mountain or gravel bikes** safely off-road, secure from
theft, and protected from weather and dust when desired.

- **Two-mode capability — the build supports both:**
  1. **Internal "garage" mode:** bikes carried *inside* the rear of the
     habitat, behind/under the bed platform, in a sealed dust-/weather-
     protected compartment with a large rear hatch.
  2. **External motorized rack mode:** swing-out / lift-assist rack
     similar to **Aluminess motorized bike rack** or **1UP USA Equip-D
     w/ StableLoad lift**, mounted to the rear bumper / hitch, capable
     of carrying 2–3 bikes when garage is otherwise loaded.
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

## 21. Open Decisions (Track in /decisions log)

1. Cab style: regular vs crew (affects shell length and pass-through).
2. Shell length: 19' vs 21'.
3. Bus voltage: 12V vs 24V vs 48V.
4. AC: rooftop vs split.
5. Heat: standalone diesel air + separate DHW vs Truma Combi.
6. Toilet: traditional flush + black tank (current baseline) vs
   composting vs cassette.
7. Cab-to-house pass-through: yes/no.
8. Subframe vendor/design: build vs buy.
9. Solar capacity target (W) and panel count.
10. Convertible dinette vs fixed bed (dictated by 19/21 choice).

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
