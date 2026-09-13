import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(12, 7))

fig.patch.set_facecolor("#F7F8FC")
ax.set_facecolor("#F7F8FC")

colors = [
    "#5B8FF9", "#61DDAA", "#65789B", "#F6BD16", "#7262FD",
    "#78D3F8", "#9661BC", "#F6903D", "#E8684A", "#6DC8EC"
]

bars = ax.bar(
    top_10_animals['Животное'], 
    top_10_animals['Популярность'], 
    color=colors,
    width=0.68,
    edgecolor='white',
    linewidth=1.2
)

ax.set_title(
    "Топ-10 популярных животных",
    fontsize=22,
    fontweight="bold",
    loc="center",
    pad=25
)

ax.text(
    0, 1.02,
    "Сравнение животных по уровню популярности",
    transform=ax.transAxes,
    fontsize=11,
    color="#6B7280"
)

ax.set_xlabel(
    "Животное",
    fontsize=12,
    fontweight="bold",
    labelpad=15
)

ax.set_ylabel(
    "Популярность",
    fontsize=12,
    fontweight="bold",
    labelpad=15
)

plt.xticks(
    rotation=35, 
    ha='right',
    fontsize=10
)

ax.tick_params(
    axis="y",
    labelsize=10,
    colors="#555555"
)

ax.tick_params(
    axis="x",
    length=0,
    colors="#333333"
)

ax.grid(
    axis="y",
    linestyle="--",
    alpha=0.20,
    linewidth=0.8
)

ax.set_axisbelow(True)

for side in ['top', "right", 'left']:
    ax.spines[side].set_visible(False)

ax.spines["bottom"].set_color("#D1D5DB")

for bar in bars:
    height = bar.get_height()

    ax.text(
        bar.get_x() + bar.get_width() / 2,
        height,
        f"{height:g}",
        ha="center",
        va="bottom",
        fontsize=10,
        fontweight="bold",
        color="#374151"
    )

ax.margins(y=0.12)

plt.tight_layout()

plt.show()
