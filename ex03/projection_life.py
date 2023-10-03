import numpy as np
import matplotlib.pyplot as plt
from load_csv import load


def convert_str_numbers(arr):
    '''
    Convert string numbers that contains M or k to actual int
    '''
    result = []
    for num_str in arr:
        if num_str.endswith('M'):
            num = float(num_str.rstrip('M')) * 1e6
        elif num_str.endswith('k'):
            num = float(num_str.rstrip('k')) * 1e3
        else:
            num = float(num_str)
        result.append(int(num))
    return np.array(result)


def main():
    '''
    Load population CSV file, and plot it using matplotlib.
    '''
    try:
        # Load DataSets
        income_dataset = load(
            "income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
        life_dataset = load("life_expectancy_years.csv")

        # Extract Data of 1900
        income_1900 = income_dataset['1900'].to_numpy()
        life_1900 = life_dataset['1900'].to_numpy()

        # Initialize a plot
        fig, axs = plt.subplots()

        # Set Title
        # fig.suptitle("1900")
        axs.set_title("1990")

        # Plot / Scatter
        axs.scatter(income_1900, life_1900, marker="o")
        axs.set_xlabel("Gross Domestic Product")
        axs.set_ylabel("Life Expectancy")
        axs.set_xscale('log')
        axs.set_xticks([300, 1_000, 10_000])
        axs.set_xticklabels(['300', '1k', '10k'])

        plt.show()

    except Exception as e:
        print(f"Error: {e}")
    except KeyboardInterrupt:
        print("Keyboard interuption, bye~")


if __name__ == "__main__":
    main()
