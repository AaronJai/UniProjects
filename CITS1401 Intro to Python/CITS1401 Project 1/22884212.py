# Project: Country Statistic Analysis - CITS1401
# Author: Aaron Tan
# UWA Student ID: 22884212
"""
This program reads a CSV file of countries and calculates various statistics based on the countries in a given region.

Inputs:
- csvfile: A string containing the path to the CSV file
- region: A string containing the name of the region to calculate statistics for

Outputs:
- maxmin_result: A list containing the name of the country with the maximum population and the name of the country with the minimum population
- stdvaverage_result: A list containing the average population and standard deviation of population for all countries in the specified region
- density: A list containing the name and density (population/land area) of all countries in the specified region, sorted by density in descending order
- corr: A float containing the correlation coefficient between population and land area for all countries in the specified region
"""

def main(csvfile, region):
    # Read CSV file
    with open(csvfile, 'r') as data:
        # Convert file to a list of rows
        csvfile = [line.strip().split(',') for line in data.readlines()]
        # Remove title header row to allow easier manipulation of data
        csvfile = csvfile[1:]

    # Question 1
    # Initialise values for min/max population and their names
    min_pop, max_pop = float('inf'), float('-inf')
    min_country, max_country = '', ''
    for row in csvfile:
        if row[5] == region and float(row[3]) > 0:
            # Set population as an integer
            population = int(row[1])
            # Check if current population is smaller than the current minimum (inf)
            if population < min_pop:
                min_pop = population
                min_country = row[0]
            # Check if current population is larger than the current maximum (-inf)
            if population > max_pop:
                max_pop = population
                max_country = row[0]
    maxmin_result = [max_country, min_country]

    # Question 2
    total_pop = 0
    num_countries = 0
    for row in csvfile:
        if row[5] == region:
            # Add the population of the current country to the total population and increase the number of countries by 1
            total_pop += int(row[1])
            num_countries += 1
    # Make sure there's at least 1 country before calculating average
    if num_countries > 0:
        # calculate average population
        avg_pop = round(total_pop / num_countries, 4)
        # calculate standard deviation through variance
        variance = 0
        for row in csvfile:
            if row[5] == region:
                variance += (int(row[1]) - avg_pop) ** 2
        variance /= (num_countries - 1)
        std_dev = round(variance ** 0.5, 4)
    stdvaverage_result = [avg_pop, std_dev]
    
    # Question 3
    all_countries = []
    for row in csvfile:
        if row[5] == region:
            # density = P/L (population/land area)
            density = round(int(row[1]) / int(row[4]), 4)
            # Create list containing country name and density
            country_data = [row[0], density]
            # append that list to initialised list
            all_countries.append(country_data)
            # Sort countries based on second element in descending order
            all_countries.sort(reverse = True, key = lambda x: x[1])
    countries = all_countries

    # Question 4
    population = []
    land_area = []
    for row in csvfile:
        if row[5] == region:
            # Append population and land area of the current country to its respective list
            population.append(int(row[1]))
            land_area.append(int(row[4]))

    # Ensure there is data vailable for population and land area
    if len(population) > 0 and len(land_area) > 0:
        n = len(population)

        # Calculate sum of population and land area for all countries in specified region
        sum_pop = sum(population)
        sum_area = sum(land_area)

        # Calculate sum of product and land area for all countries in specified region
        sum_pop_area = sum([population[i] * land_area[i] for i in range(n)])

        # Calculate sum of squares of population and land area for all countries in specified region
        sum_pop_sq = sum([population[i] ** 2 for i in range(n)])
        sum_area_sq = sum([land_area[i] ** 2 for i in range(n)])

        # Calculate correlation coefficient
        numerator = n * sum_pop_area - sum_pop * sum_area
        denominator = ((n * sum_pop_sq - sum_pop ** 2) * (n * sum_area_sq - sum_area ** 2)) ** 0.5
        correlation_coefficient = round(numerator / denominator, 4)
    corr = correlation_coefficient

    # Return all results
    return (maxmin_result, stdvaverage_result, countries, corr)

# Defining variables shown in project instruction sheet example
MaxMin, stdvAverage, density, corr = main('countries.csv', 'Africa')

print(MaxMin)
print(stdvAverage)
