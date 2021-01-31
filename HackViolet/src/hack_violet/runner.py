#Runner: This module holds the dictionary and runs the program tools
#from compare_crime_data import plot_graph_crime, plot_graph_housing
#from builtins import int
from hack_violet.data_visuals import plot_graph_crime, plot_graph_housing
from hack_violet.tracker import compile_map

zipcode = input("Type zipcode: ")    
zipcode = str(zipcode)
if len(zipcode) == 5:    
    plot_graph_crime(zipcode)
    plot_graph_housing(zipcode)
    compile_map(zipcode)
else:
    print("Input Invalid")
    quit




