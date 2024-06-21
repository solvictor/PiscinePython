import pandas


def load(path: str) -> pandas.DataFrame | None:
    """Get a DataFrame from a csv file

    Args:
        path (str): path of the csv file

    Returns:
        pandas.DataFrame | None: DataFrame or None if a problem occurs
    """

    try:
        data = pandas.read_csv(path)
        print("Loading dataset of dimensions", data.shape)
        return data
    except Exception:
        pass
    return None


def main():
    """Test this file's functions"""

    print(load("life_expectancy_years.csv"))


if __name__ == "__main__":
    main()
