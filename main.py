import pandas as pd

df = pd.read_csv("movies.csv")

print("===== AI RECOMMENDATION SYSTEM =====")

genre = input(
    "\nChoose Genre (Action/Romance/Sci-Fi/Horror): "
)

recommendations = df[
    df["Genre"].str.lower() == genre.lower()
]

if len(recommendations) > 0:

    recommendations = recommendations.sort_values(
        by="Rating",
        ascending=False
    )

    print("\nRecommended Movies:\n")

    for index, row in recommendations.iterrows():
        print(
            f"{row['Movie']}  | Rating: {row['Rating']}"
        )

else:
    print("\nNo recommendations found.")
