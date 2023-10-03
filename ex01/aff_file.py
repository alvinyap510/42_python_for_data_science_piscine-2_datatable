import matplotlib.pyplot as plt
from load_csv import load


# Reference: https://tinyurl.com/bddt7c95


def main():
    '''
    Load life expectancy CSV file, and plot it using matplotlib.
    '''
    try:
        dataset = load("life_expectancy_years.csv")

        # Extract the rows where the 'country' column is equal to 'Malaysia'
        malaysia_data = dataset[dataset['country'] == 'Malaysia']

        # Sets the country column as the index of malaysia_data
        malaysia_data.set_index('country', inplace=True)

        # retuan the column names of malaysia_data as panda index
        years = malaysia_data.columns.astype(int).to_numpy()

        # Select the row corresponding Malaysia
        life = malaysia_data.loc['Malaysia'].to_numpy()

        # Initialize a plot
        fig, axs = plt.subplots()

        # Supertitle
        fig.suptitle("Malaysia Life Expectancy Projections")

        # Plit Years as x-axis and Life as y-axis
        axs.plot(years, life)
        axs.set_xlabel("Years")
        axs.set_ylabel("Life Expectancy")

        plt.show()
    except Exception as e:
        print(f"Error: {e}")
    except KeyboardInterrupt:
        print("Keyboard interuption, bye~")


if __name__ == "__main__":
    main()
