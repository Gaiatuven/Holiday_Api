##Holiday Information Retrieval Script

####This script allows you to retrieve holiday information for a specific country and year using the API Ninjas holiday API. The retrieved data is saved to a JSON file for further analysis.
Prerequisites

Before using this script, make sure you have the following:

    Python 3.x installed on your system.
    An API key from API Ninjas. You can obtain your API key by signing up on their website.

Getting Started

    Clone this repository or download the script.

    Set your API key as an environment variable. You can do this by running the following command in your terminal, replacing YOUR_API_KEY with your actual API key:

Bash

    export NINJA_API=YOUR_API_KEY

Install the required Python libraries using pip:

bash

    pip install requests

Run the script using the following command:

bash

    python holiday_info.py

Usage

When you run the script, it will prompt you to provide the following information:

    Country Code: Enter the country code (e.g., "za" for South Africa).

    Year: Enter the year for which you want to retrieve holiday information (e.g., "2024").

The script will then make a request to the API Ninjas holiday API, retrieve the holiday data, and save it to a JSON file in the current directory. It will also display the details of each holiday, including country, year, date, name, and type.
Sample Output

Here's a sample of what the script's output may look like:

Holiday information for za in 2024:

Country: za
Year: 2024
Date: Friday, 2024-01-01
Name: New Year's Day
Type: Public Holiday

Country: za
Year: 2024
Date: Thursday, 2024-04-25
Name: Freedom Day
Type: Public Holiday

...

Notes

    The retrieved holiday data is saved to a JSON file named <country>_<year>_holidays.json.

    If an error occurs during the API request, the script will display the error code and message.

Author

This script was created by [https://github.com/Gaiatuven].

License

This project is licensed under the MIT License.