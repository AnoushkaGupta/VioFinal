from hack_violet.get_data import check_db_zip
import matplotlib.pyplot as plt


#national average crime rate per 100k according to FBI 2020
nat_violent = 366.7
nat_total = float(2489)
#national average crime rate per 100k according to FBI 2019
rochester_violent = float(748)
rochester_total = float(4239)


#Percent difference between national average and selected area, not currently shown
#def crime_percent_increase(current_zip):
    # current_data = check_db_zip(current_zip)
    #change_nat = float(current_data['Violent Crime']) - nat_violent
    #change_roch = float(current_data['Violent Crime']) - rochester_violent
    #return change_nat/nat_violent * 100, change_roch/rochester_violent * 100
    
    
    
def plot_graph_crime(current_zip):
    #plot_graph_crime plots a graph that compares total and violent crime rates againts
    #the national average and the national high on a nested bar chart.
    
    #checks database for zipcode data
    current_data = check_db_zip(current_zip)
    #creates data sets
    total = [current_data['Total Crime'], nat_total,  rochester_total]
    violent= [current_data['Violent Crime'], nat_violent, rochester_violent]
    value = [current_data['City'],'National Average', 'Rochester, New York']

    #creates a figure of custom size and plots the two bars for each category
    plt.figure(figsize = (8, 6)) 
    plt.bar( value, total, color ='#D2A1A1',  
            width = 0.4) 
    plt.bar( value, violent, color ='#B65555',  
            width = 0.4) 

    #Labels and formatting
    plt.title("Crime rate comparison") 
    plt.ylabel("Number of violent crimes per 100k people") 
    txt = 'Comparison of violent crimes in ' + current_data['City'] + ' to the National Average and city with highest crime rate: Rochester, New York based on most recent crime data from the FBI.'
    plt.figtext(0.5, 0.01, txt, wrap=True, horizontalalignment='center', fontsize=8)
    plt.legend(labels=['Total crime', 'Violent crime'])
    plt.show() 
    
    
#---------------------------------------------------------------------------------------------



#property prices as of June 2020 excluding Hawaii

nat_price = 295300
low_WV = 107000
high_cali = 579332

def plot_graph_housing(current_zip):
    #plot_graph_housing plots a graph that compares median house prices of the current zipcode
    # to the national average and the high/low on a bar graph
    
    #searches database and creates a dataset
    current_data = check_db_zip(current_zip)
    total = [current_data['Avg Property Value'], nat_price, low_WV, high_cali]
    value = [current_data['City'],'National Average', 'Lowest state-\n West Virginia', 'Highest state-\n California']
    
    
    price_sqft = current_data['Price Sqr Ft']
    
    #creates a new figure and plots datasets
    plt.figure(figsize = (8, 6)) 
    plt.bar( value, total, color ='#B65555',  width = 0.4) 
    
    #formatting and labels
    plt.text(current_data['City'], current_data['Avg Property Value'] +6000, "$"+str(price_sqft)+"/sqft",  horizontalalignment='center')
    plt.title("Median Housing Price Comparison") 
    plt.ylabel("Median Price ($)") 
    txt = 'Median house price in ' + current_data['City'] + ' compared to the national median and states with the highest and lowest median as of June 2020'
    plt.figtext(.5, 0.01, txt, wrap=True, horizontalalignment='center', fontsize=8)
    plt.show() 
    
 
