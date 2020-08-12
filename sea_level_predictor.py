import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot

    x=df['Year']
    y=df['CSIRO Adjusted Sea Level']    
    plt.scatter(x,y, color="red", marker="o")

    # Create first line of best fit
    (slope, intercept, rvalue, pvalue, stderr) = linregress(x,y)
    
    x_pred = list(range(1880, 2050))
    y_pred = [slope * x + intercept for x in x_pred]
    plt.plot(x_pred,y_pred, color="green")

    # Create second line of best fit
    recent = df[df['Year'] >= 2000]
    x_recent = recent['Year']
    y_recent = recent['CSIRO Adjusted Sea Level']

    (slope, intercept, rvalue, pvalue, stderr) = linregress(x_recent,y_recent)
    
    x_rec = list(range(2000, 2050))
    y_rec = [slope * x_recent + intercept for x_recent in x_rec]
    plt.plot(x_rec,y_rec, color="black")  
    

    # Add labels and title
    plt.xlabel('Year') 
    plt.ylabel('Sea Level (inches)') 
    plt.title('Rise in Sea Level')

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()