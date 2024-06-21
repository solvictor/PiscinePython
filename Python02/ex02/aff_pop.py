from load_csv import load
import matplotlib.pyplot as plt


def main():
    """Plot data from population_total.csv"""

    df = load("population_total.csv")
    if df is None:
        return

    df = df[df["country"].isin(("France", "Belgium"))]
    print(df)
    df = df.map(lambda v: (print(v), v))
    df = df.loc[:, "1800":"2050"]
    df = df.set_index("country")
    df = df.transpose()
    df.plot(figsize=(6, 5), legend=False)
    plt.title("Population Projections")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.show()


if __name__ == "__main__":
    main()
