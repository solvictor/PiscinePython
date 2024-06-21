from load_csv import load
import matplotlib.pyplot as plt


def main():
    """Plot data from life_expectancy_years.csv"""

    df = load("life_expectancy_years.csv")
    if df is None:
        return

    country = "France"
    start = 1800
    end = 2080

    df = df.set_index("country")
    df = df.transpose()
    df = df[country]

    plt.plot(range(start, end + 21), df)
    plt.title(country + " life expectancy projections")
    plt.xticks(range(start, end + 1, 40))
    plt.xlabel("Year")
    plt.ylabel("Life expectancy")
    plt.show()


if __name__ == "__main__":
    main()
