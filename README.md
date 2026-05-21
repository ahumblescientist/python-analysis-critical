# python-analysis-critical
the following provides a summary on what each script does:

1. arabic_to_english.py convert the data given in csv to another csv file in english (cleaner)
2. generate_figures: to generate general distributions figures
3. hypothesisn.py : to test hypothesis n given in order

# libraries used
- numpy
- pandas
- seaborn
- scipy
- matplotlib

# how to run
1. the script arabic_to_english expects a file named "responses.csv" (of course with the expected format of columns)
2. the output of the previous script is a file called "responses_english.csv" which all the other scripts expect before they do anything

# the hypothesis files
1. they output a figure to visualize the variables of the hypothesis
2. in the terminal used to run the script (python3 name.py) they output the relevant variables (p-value, ...etc)
