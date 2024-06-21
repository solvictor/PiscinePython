from load_csv import load
import matplotlib.pyplot as plt


def main():
    """Plot the projection of life expectancy in relation
    to the gross national product of the year 1900 """

    income_data = load(
        "income_per_person_gdppercapita_ppp_inflation_adjusted.csv",
    )
    if income_data is None:
        return

    life_expectancy_data = load("life_expectancy_years.csv")
    if life_expectancy_data is None:
        return

    year = "1900"
    gnp = income_data[year]
    life_expectancy = life_expectancy_data[year]
    plt.figure(figsize=(7, 5))
    plt.scatter(gnp, life_expectancy)
    plt.title(year)
    plt.xlabel("Gross domestic product")
    plt.ylabel("Life Expectancy")
    plt.xscale("log")
    plt.xticks(ticks=[300, 1000, 10000], labels=["300", "1k", "10k"])
    plt.show()


if __name__ == "__main__":
    main()
