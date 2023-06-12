# Project: Country Statistic Analysis 2 - CITS1401
# Author: Aaron Tan
# UWA Student ID: 22884212
"""
This program reads a CSV file containing country data and performs various calculations and analyses based on the data.

Inputs:
- csvfile: A string containing the path to the CSV file.

Outputs:
- dict1: A dictionary containing calculated statistics for regions, including standard error and cosine similarity.
- dict2: A nested dictionary containing country information grouped by region. Country infomration includes: population, net change, 
percentage of population with respect to a region, density of population, and the rank of population in the region.

Notes:
The tested CSV file has the format: Country,Population,Yearly Change,Net Change,Urban,Land Area,Med Age,Regions
This program takes into account that rows and columns could be in different order, excluding the headings row.
If missing or invalid data is present, entire row(s) will be ignored.
Region names are converted to lower case for case sensitivity - must be kept in mind when calling specific regions in either dict1 or dict2.
Country names are also converted to lower case in dict2 - will not affect calling.
"""

def main(csvfile):
    dict1 = {}
    dict2 = {}

    # Define function to calculate standard error of a list of values
    def calculate_standard_error(values):
        n = len(values)
        mean = sum(values) / n
        variance = sum([(value - mean) ** 2 for value in values]) / (n - 1)
        standard_deviation = round((variance ** 0.5), 4)
        standard_error = round(standard_deviation / (n ** 0.5), 4)
        return standard_error

    # Define function to calculate cosine similarity between two lists of values
    def calculate_cosine_similarity(list1, list2):
        dot_product = sum([value1 * value2 for value1, value2 in zip(list1, list2)]) # Zip to ensure element-wise multiplication
        magnitude1 = (sum([value ** 2 for value in list1])) ** 0.5
        magnitude2 = (sum([value ** 2 for value in list2])) ** 0.5
        cosine_similarity = round(dot_product / (magnitude1 * magnitude2), 4)
        return cosine_similarity

    # Read CSV file
    with open(csvfile, 'r') as data:
        # Read all lines from the file
        lines = data.read().splitlines()
        # Convert lines to a list of rows
        csvfile = [line.split(',') for line in lines]
        # Define header row and remove title header row to allow easier manipulation of data
        header = csvfile[0]
        csvfile = csvfile[1:]

        # Column indices based on header
        country_index = header.index('Country')
        population_index = header.index('Population')
        net_change_index = header.index('Net Change')
        urban_index = header.index('Urban')
        land_area_index = header.index('Land Area')
        med_age_index = header.index('Med Age')
        regions_index = header.index('Regions')

        # Convert names to lower case for case sensitivity
        for row in csvfile:
            region = row[regions_index]
            row[regions_index] = region.lower()

        # Task 1 Part 1: Standard Error of a region
        region_population = {}

        for row in csvfile:
            try:
                population = int(row[population_index])
                region = row[regions_index]

                # Skip invalid or missing data
                if population <= 0 or region == '':
                    continue

                if region not in region_population:
                    region_population[region] = []
                region_population[region].append(population)
            except ValueError:
                continue
        
        # Calculate standard error using defined function
        for region, population_list in region_population.items():
            standard_error = calculate_standard_error(population_list)
            dict1[region] = [standard_error]

        # Task 1 Part 2: Cosine similarity between population and land area for a region
        region_population = {}
        region_land_area = {}

        for row in csvfile:
            try:
                region = row[regions_index]
                population = int(row[population_index])
                land_area = int(row[land_area_index])

                # Skip invalid or missing data
                if population <= 0 or land_area <= 0 or region == '':
                    continue

                if region not in region_population:
                    region_population[region] = []
                    region_land_area[region] = []

                region_population[region].append(population)
                region_land_area[region].append(land_area)
            except ValueError:
                continue
        
        # Calculate cosine similarity using defined function
        for region, population_list in region_population.items():
            cosine_similarity = calculate_cosine_similarity(population_list, region_land_area[region])
            dict1[region].append(cosine_similarity)

        # Task 2: Create nested dictionary with region and country information
        region_info = {}

        for row in csvfile:
            try:
                region = row[regions_index]
                country = row[country_index].lower() # Changed to lower case
                population = int(row[population_index])
                net_change = int(row[net_change_index])
                land_area = int(row[land_area_index])

                # Skip rows with invalid or missing data
                if any(value <= 0 for value in (population, land_area)) or any(value == '' for value in (region, country)):
                    continue

                # Filter rows that match the current region
                region_rows = [r for r in csvfile if r[regions_index] == region]
                total_population = sum(int(r[population_index]) for r in region_rows)

                # Check if total_population is not zero before division
                if total_population != 0:
                    density = round(population / land_area, 4)
                    rank = 1 + sum(1 for r in region_rows if int(r[population_index]) > population)
                    region_percentage = round((population / total_population) * 100, 4)

                    if region not in region_info:
                        region_info[region] = {}

                    country_info = [population, net_change, region_percentage, density, rank]
                    region_info[region][country] = country_info # Assign country_info as a value to the nested dictionary
            except (ValueError, IndexError):
                continue

        # Sort countries in each region based on specified criteria
        for region, countries in region_info.items():
            sorted_countries = sorted(
                countries.items(), key=lambda x: (-x[1][0], -x[1][3], x[0]) # Sorted by population, density, and name respectively
            )
            dict2[region] = {country: info for country, info in sorted_countries}

    # Return the dictionaries
    return dict1, dict2