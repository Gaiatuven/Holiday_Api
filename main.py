import requests
import json
import os

Xpi_Key = os.environ.get('NINJA_API')

# Allow users to specify country and year interactively
country = input("Enter the country code (e.g., za): ")
year = input("Enter the year (e.g., 2024): ")

api_url = f'https://api.api-ninjas.com/v1/holidays?country={country}&year={year}'
headers = {'X-Api-Key': Xpi_Key}

response = requests.get(api_url, headers=headers)

if response.status_code == requests.codes.ok:
    info = response.json()

    # Save the JSON data to a file
    with open(f"{country}_{year}_holidays.json", 'w') as file:
        json.dump(info, file, indent=4)  # Save with indentation

    print(f"Holiday information for {country} in {year}:\n")
    for holiday in info:
        # Format the date
        formatted_date = f"{holiday['day']}, {holiday['date']}"

        # Print the details of each holiday
        print(f"Country: {holiday['country']}")
        print(f"Year: {holiday['year']}")
        print(f"Date: {formatted_date}")
        print(f"Name: {holiday['name']}")
        print(f"Type: {holiday['type']}")
        print()  # Add an empty line to separate holidays

else:
    print(f"Error: {response.status_code}\n{response.text}")
