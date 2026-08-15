import ezdxf

from constants import *
from blocks import create_all_blocks
from draw import draw_floor, get_global_scale


# ==========================================================
# CREATE DRAWING
# ==========================================================

doc = ezdxf.new(DXF_VERSION)

create_all_blocks(doc)

msp = doc.modelspace()


# ==========================================================
# USER INPUT
# ==========================================================

print("=" * 60)
print("          FIRE ALARM SLD GENERATOR")
print("=" * 60)

floors = int(
    input("\nNumber of Floors (excluding Ground): ")
)

floor_data = []


# ==========================================================
# COLLECT DATA
# ==========================================================

for i in range(floors + 1):

    print("\n" + "-" * 50)

    if i == 0:
        floor_name = "GROUND FLOOR"
    else:
        floor_name = f"FLOOR {i}"

    print(floor_name)

    smoke = int(input("Smoke Detectors        : "))
    heat = int(input("Heat Detectors         : "))
    multi = int(input("Multi Sensor Detectors : "))
    mcp = int(input("Manual Call Points     : "))
    hooter = int(input("Hooters               : "))
    monitor = int(input("Monitor Modules        : "))
    control = int(input("Control Modules        : "))
    relay = int(input("Relay Modules          : "))

    total = (
        smoke
        + heat
        + multi
        + mcp
        + hooter
        + monitor
        + control
        + relay
    )

    floor_data.append(
        {
            "name": floor_name,
            "smoke": smoke,
            "heat": heat,
            "multi": multi,
            "mcp": mcp,
            "hooter": hooter,
            "monitor": monitor,
            "control": control,
            "relay": relay,
            "total": total,
        }
    )


# ==========================================================
# GLOBAL SCALE
# ==========================================================

counts = [floor["total"] for floor in floor_data]

global_scale = get_global_scale(counts)

print(f"\nGlobal Symbol Scale : {global_scale:.2f}")


# ==========================================================
# DRAW FLOORS
# ==========================================================

y = 0

for floor in floor_data:

    draw_floor(

        msp,

        floor["name"],

        y,

        floor["smoke"],

        floor["heat"],

        floor["multi"],

        floor["mcp"],

        floor["hooter"],

        floor["monitor"],

        floor["control"],

        floor["relay"],

        global_scale,

    )

    y += FLOOR_HEIGHT


# ==========================================================
# SAVE
# ==========================================================

doc.saveas(OUTPUT_FILE)

print("\n" + "=" * 60)
print("Drawing Generated Successfully!")
print("=" * 60)

print(f"\nSaved As : {OUTPUT_FILE}")