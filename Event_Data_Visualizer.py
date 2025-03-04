import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import pandas as pd
import json
import sys

# DESC: Display the retrieved stats in a simple to understand format
# Preconditions: string for title, list of fighter stats for both fighers
# Postconditions: Graphically visualized fight stats for selected matchup
def DisplayFighterMatchup(eventTitle ,fighter1info, fighter2info):
    fighters = [fighter1info[0], fighter2info[0]]
    fighterData = {
        "Record": [fighter1info[1], fighter2info[1]],
        "Avg fight time": [fighter1info[2], fighter2info[2]],
        "Height (ft)" : [fighter1info[3], fighter2info[3]],
        "Weight (lbs)" : [fighter1info[4], fighter2info[4]],
        "Reach (in)" : [fighter1info[5], fighter2info[5]],
        "Stance" : [fighter1info[6], fighter2info[6]],
        "DOB" : [fighter1info[7], fighter2info[7]],
        "SLpM" : [float(fighter1info[8]), float(fighter2info[8])],
        "Strk Acc" : [int(fighter1info[9][:-1]), int(fighter2info[9][:-1])],
        "SApM" : [float(fighter1info[10]), float(fighter2info[10])],
        "Strk Def" : [int(fighter1info[11][:-1]), int(fighter2info[11][:-1])],
        "TD avg 15min" : [float(fighter1info[12]), float(fighter2info[12])],
        "TD Acc" : [int(fighter1info[13][:-1]), int(fighter2info[13][:-1])],
        "TD Def" : [int(fighter1info[14][:-1]), int(fighter2info[14][:-1])],
        "Sub avg 15min" : [float(fighter1info[15]), float(fighter2info[15])],
    }

    df = pd.DataFrame(fighterData, index=fighters)

    fig = plt.figure(figsize=(12, 8))
    gs = gridspec.GridSpec(3, 4, height_ratios=[1, 2, 2])  # First row for text, next two for graphs

    axText = fig.add_subplot(gs[0, :])  # Use all 4 columns for fighter info
    axText.axis("off")  # Hide axes
    fighterInfo = f"""
    {eventTitle}
    ---------------------------------
    {fighters[0]} vs {fighters[1]}
    ---------------------------------
    Weight: {df.loc[fighters[0], "Weight (lbs)"]} 
    Record: {df.loc[fighters[0], "Record"]} vs {df.loc[fighters[1], "Record"]}
    Height: {df.loc[fighters[0], "Height (ft)"]} vs {df.loc[fighters[1], "Height (ft)"]} 
    Reach: {df.loc[fighters[0], "Reach (in)"]} vs {df.loc[fighters[1], "Reach (in)"]} 
    Stance: {df.loc[fighters[0], "Stance"]} vs {df.loc[fighters[1], "Stance"]}
    DOB: {df.loc[fighters[0], "DOB"]} vs {df.loc[fighters[1], "DOB"]}
    """

    axText.text(0.5, 0.5, fighterInfo, fontsize=12, ha="center", va="center", fontfamily="monospace")

    stats_to_compare = [
    "SLpM", "Strk Acc", "SApM", "Strk Def", 
    "TD avg 15min", "TD Acc", "TD Def", "Sub avg 15min"
    ]

    for i, stat in enumerate(stats_to_compare):
        row = 1 if i < 4 else 2  # First 4 go to row 1, next 4 go to row 2
        col = i % 4  # Distribute across 4 columns
        ax = fig.add_subplot(gs[row, col])  # Assign subplot position
        ax.bar(fighters, df[stat], color=["red", "blue"])
        ax.set_title(stat)
        ax.set_ylabel("Value")
        ax.set_xticklabels(fighters, rotation=20, ha="right")  # Rotate and align text

    plt.tight_layout()
    plt.show()

    return

# DESC: Calls the fucntion to display fighter stats, argument index can specify what fight to see the stats of
def main():
    with open("eventInfo.json", "r") as file:
        info = json.load(file)
    if len(sys.argv) > 1:
        DisplayFighterMatchup(info[0], info[int(sys.argv[1])][0], info[int(sys.argv[1])][1])
    else:
        DisplayFighterMatchup(info[0], info[1][0], info[1][1])

if __name__ == "__main__":
    main()