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

        start_index = 0  # Index corresponding to the year 1800
        end_index = 251  # Index corresponding to the year 2050

        # return the column names of malaysia_data as panda index
        years = malaysia_data.columns.astype(int).to_numpy()
        years = years[start_index:end_index]

        # Select the row corresponding Malaysia
        life = malaysia_data.loc['Malaysia'].to_numpy()
        life = life[start_index:end_index]


        # Initialize a plot
        fig, axs = plt.subplots()

        # Supertitle
        fig.suptitle("Malaysia Life Expectancy Projections")

        # Plot Years as x-axis and Life as y-axis
        axs.plot(years, life)
        axs.set_xlabel("Years")
        axs.set_xticks([1800, 1840, 1880, 1920, 1960, 2000, 2040])
        axs.set_xticklabels(['1800', '1840', '1880', '1920', '1960', '2000', '2040'])
        axs.set_ylabel("Life Expectancy")

        plt.show()
    except Exception as e:
        print(f"Error: {e}")
    except KeyboardInterrupt:
        print("Keyboard interuption, bye~")


if __name__ == "__main__":
    main()
