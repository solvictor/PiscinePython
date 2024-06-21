from load_csv import load
import matplotlib.pyplot as plt


def convert(x):
    """Converts x to float value

    Args:
        x (str): data value as in the csv

    Returns:
        float: corresponding float value
    """

    mag = {"K": 1e3, "M": 1e6, "B": 1e9}.get(x[-1].upper(), None)

    return float(x[:-1]) * mag if mag else float(x)


def main():
    """Plot data from population_total.csv"""

    df = load("population_total.csv")
    if df is None:
        return

    countries = ("Belgium", "France")
    colors = ("steelblue", "forestgreen")
    start = 1800
    end = 2050

    df = df.set_index("country")
    df = df.transpose()
    df = df.loc[str(start):str(end)]

    max_pop = 0
    for country, col in zip(countries, colors):
        cdf = df[country]
        cdf = cdf.map(convert)
        max_pop = max(max_pop, max(cdf))
        plt.plot(range(start, end + 1), cdf, color=col)

    y_ticks = [i * 1e7 for i in range(2, int(max_pop / 1e7) + 1, 2)]
    plt.xticks(range(start, end + 1, 40))
    plt.yticks(y_ticks, [f"{pop / 1e6:.0f}M" for pop in y_ticks])
    plt.legend(countries, loc="lower right")
    plt.title("Population Projections")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.show()


if __name__ == "__main__":
    main()
