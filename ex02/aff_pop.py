import numpy as np
import matplotlib.pyplot as plt
from load_csv import load


# Reference: https://tinyurl.com/bddt7c95

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
        dataset = load("population_total.csv")

        # Extract the rows where the 'country' column is equal to
        # 'Malaysia' and 'France'
        malaysia_data = dataset[dataset['country'] == 'Malaysia']
        france_data = dataset[dataset['country'] == 'France']

        # Sets the country column as the index
        malaysia_data.set_index('country', inplace=True)
        france_data.set_index('country', inplace=True)

        start_index = 0  # Index corresponding to the year 1800
        end_index = 251  # Index corresponding to the year 2050

        # return the column names of malaysia_data as panda index
        years = malaysia_data.columns.astype(int).to_numpy()
        years = years[start_index:end_index + 1]

        # Select the row corresponding Malaysia and France
        population_malaysia = malaysia_data.loc['Malaysia'].to_numpy()
        population_malaysia = population_malaysia[start_index:end_index + 1]
        population_malaysia = convert_str_numbers(population_malaysia)
        population_france = france_data.loc['France'].to_numpy()
        population_france = population_france[start_index:end_index + 1]
        population_france = convert_str_numbers(population_france)

        # Initialize a plot
        fig, axs = plt.subplots()

        # Supertitle
        fig.suptitle("Population Projection")

        # Plot Years as x-axis and Life as y-axis
        axs.plot(years, population_malaysia, label="Malaysia")
        axs.plot(years, population_france, label="France")
        axs.set_xlabel("Years")
        axs.set_ylabel("Population")
        axs.set_yticks([20_000_000, 40_000_000, 60_000_000, 80_000_000])
        axs.set_yticklabels(['20m', '40m', '60m', '80m'])
        axs.legend(loc="lower right")

        plt.show()
    except Exception as e:
        print(f"Error: {e}")
    except KeyboardInterrupt:
        print("Keyboard interuption, bye~")


if __name__ == "__main__":
    main()
