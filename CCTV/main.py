import ezdxf

from constants import *
from blocks import create_all_blocks
from draw import draw_floor, get_global_scale


# ==========================================================
# CREATE DRAWING
# ==========================================================

doc = ezdxf.new("R2018")

create_all_blocks(doc)

msp = doc.modelspace()


# ==========================================================
# USER INPUT
# ==========================================================

print("=" * 55)
print("          CCTV SLD GENERATOR v1.0")
print("=" * 55)

floors = int(
    input(
        "\nNumber of Floors (excluding Ground): "
    )
)

# ==========================================================
# COLLECT ALL FLOOR DATA FIRST
# ==========================================================

floor_data = []

for i in range(floors + 1):
    print("\n" + "-" * 45)
    
    if i == 0:
        floor_name = "GROUND FLOOR"
    else:
        floor_name = f"FLOOR {i}"
    
    print(floor_name)
    
    while True:
        dome = int(input("Dome Cameras   : "))
        bullet = int(input("Bullet Cameras : "))
        total = dome + bullet
        
        if total > MAX_CAMERAS:
            print(
                f"\nMaximum cameras per floor is {MAX_CAMERAS}."
            )
            print("Please enter the floor again.\n")
            continue
        
        floor_data.append({
            "name": floor_name,
            "dome": dome,
            "bullet": bullet,
            "total": total
        })
        break

# ==========================================================
# CALCULATE GLOBAL SCALE
# ==========================================================

camera_counts = [f["total"] for f in floor_data]
global_scale = get_global_scale(camera_counts)

print(f"\nGlobal Camera Scale: {global_scale:.2f}")

# ==========================================================
# DRAW FLOORS
# ==========================================================

y = 0

for idx, floor in enumerate(floor_data):
    draw_floor(
        msp,
        floor["name"],
        y,
        floor["dome"],
        floor["bullet"],
        global_scale,
        idx
    )
    y += FLOOR_HEIGHT


# ==========================================================
# SAVE DRAWING
# ==========================================================

filename = "CCTV_LAYOUT.dxf"

doc.saveas(filename)

print("\n" + "=" * 55)
print("Drawing Generated Successfully!")
print("=" * 55)

print(f"\nSaved as : {filename}")