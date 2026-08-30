
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import math



fig, ax = plt.subplots(figsize=(10, 10))


BG = "#ffffff"

fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)

ax.set_aspect("equal")
ax.axis("off")

ax.set_xlim(-11, 11)
ax.set_ylim(-11, 11)


GREEN  = "#2e7d1f"
RED    = "#d71912"
YELLOW = "#f5c400"
ORANGE = "#f57c00"
PINK   = "#e8339e"
VIOLET ="#7b2d8e"

ax.add_patch(
    patches.Circle(
        (0, 0),
        10,
        facecolor=GREEN,
        edgecolor="none",
        zorder=0
    )
)


def base_ring(inner, outer, colour):

    ax.add_patch(
        patches.Wedge(
            (0, 0),
            outer,
            0,
            360,
            width=outer - inner,
            facecolor=colour,
            edgecolor="none",
            zorder=1
        )
    )


base_ring(8.9, 10.0, GREEN)
base_ring(7.9, 8.9, RED)
base_ring(6.9, 7.9, YELLOW)
base_ring(5.9, 6.9, GREEN)
base_ring(4.9, 5.9, RED)
base_ring(3.9, 4.9, YELLOW)
base_ring(2.9, 3.9, GREEN)
base_ring(1.9, 2.9, ORANGE)
base_ring(0.0, 1.9, RED)


def petals(inner, outer, n, colour, phase=0, zorder=3):

    step = 360 / n

    for i in range(n):

        center = phase + i * step

        a1 = math.radians(center - step / 2)
        a2 = math.radians(center)
        a3 = math.radians(center + step / 2)

        p1 = (
            inner * math.cos(a1),
            inner * math.sin(a1)
        )

        p2 = (
            outer * math.cos(a2),
            outer * math.sin(a2)
        )

        p3 = (
            inner * math.cos(a3),
            inner * math.sin(a3)
        )

        ax.add_patch(
            patches.Polygon(
                [p1, p2, p3],
                closed=True,
                facecolor=colour,
                edgecolor="none",
                zorder=zorder
            )
        )


petals(
    8.55,
    10.0,
    28,
    PINK,
    phase=0,
    zorder=4
)


base_ring(8.0, 8.55, VIOLET)


petals(
    7.1,
    8.0,
    24,
    RED,
    phase=7.5,
    zorder=5
)



petals(
    6.2,
    7.1,
    24,
    ORANGE,
    phase=0,
    zorder=5
)


petals(
    5.3,
    6.2,
    24,
    YELLOW,
    phase=7.5,
    zorder=5
)


base_ring(
    4.5,
    5.3,
    VIOLET
)



petals(
    3.6,
    4.5,
    20,
    RED,
    phase=0,
    zorder=5
)




petals(
    2.8,
    3.6,
    18,
    PINK,
    phase=10,
    zorder=5
)



petals(
    2.1,
    2.8,
    16,
    GREEN,
    phase=0,
    zorder=6
)




petals(
    1.4,
    2.1,
    14,
    ORANGE,
    phase=0,
    zorder=6
)



petals(
    0.75,
    1.4,
    12,
    YELLOW,
    phase=15,
    zorder=7
)



ax.add_patch(
    patches.Circle(
        (0, 0),
        0.75,
        facecolor=RED,
        edgecolor="none",
        zorder=7
    )
)




for i in range(8):

    angle = math.radians(i * 45)

    tip = (
        0.62 * math.cos(angle),
        0.62 * math.sin(angle)
    )

    left_angle = math.radians(i * 45 - 10)
    right_angle = math.radians(i * 45 + 10)

    p1 = (
        0.13 * math.cos(left_angle),
        0.13 * math.sin(left_angle)
    )

    p2 = (
        0.13 * math.cos(right_angle),
        0.13 * math.sin(right_angle)
    )

    ax.add_patch(
        patches.Polygon(
            [p1, tip, p2],
            closed=True,
            facecolor=VIOLET,
            edgecolor="none",
            zorder=8
        )
    )



ax.add_patch(
    patches.Circle(
        (0, 0),
        0.18,
        facecolor=YELLOW,
        edgecolor="none",
        zorder=9
    )
)



plt.tight_layout()

plt.savefig(
    "pookalam_coloured_base.png",
    dpi=300,
    facecolor="white",
    bbox_inches="tight"
)

plt.show()