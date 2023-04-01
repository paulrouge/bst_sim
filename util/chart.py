import matplotlib.pyplot as plt
import pandas as pd
import os

# This function creates a chart from a CSV file and displays it,
# deletes the CSV file when you close the chart window

def create_chart_from_csv(csv_path, chuck_size, initial_mint):
    # Load the CSV file into a pandas DataFrame
    df = pd.read_csv(csv_path)

    # Extract the x column (if there is one)
    x_col = df.columns[0] if len(df.columns) > 1 else None

    # Extract the y columns from the DataFrame
    y1_col = 'bst_supply'
    y2_col = 'bst_price'
    y1 = df[y1_col]
    y2 = df[y2_col]

    # Create the figure and axis objects
    fig, ax1 = plt.subplots()

    # Plot the supply data on the left axis
    ax1.set_xlabel(x_col)
    ax1.set_ylabel(y1_col, color='b')
    ax1.plot(y1, color='b')
    ax1.tick_params(axis='y', labelcolor='b')

    # Create a second axis on the right for the price data
    ax2 = ax1.twinx()

    # Plot the price data on the right axis
    ax2.set_ylabel(y2_col, color='r')
    ax2.plot(y2, color='r')
    ax2.tick_params(axis='y', labelcolor='r')

    # Add a title to the chart
    # plt.title(f"{y1_col} vs. {y2_col}")
    plt.title(f'Initial Mint: {initial_mint} | Chunk Size: {chuck_size}', fontsize=10)
    
    # Display the chart
    plt.show()

    # onclose delete file
    os.remove(csv_path)

