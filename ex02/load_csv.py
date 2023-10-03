import pandas as pd


def load(path: str) -> pd.DataFrame | None:
    '''
    Load CSV from a path and return the dataset.

    Parameters:
    param1 (path: str): Path to the file to be read.

    Returns:
    pd.DataFrame: DataSet that has been read
    '''
    try:
        data = pd.read_csv(path)
        print(f"Loading dataset of dimensions {data.shape}")
        return data
    except Exception as e:
        print(f"{type(e).__name__}: {e}")
    except KeyboardInterrupt:
        print("Keyboard interuption, bye~")
