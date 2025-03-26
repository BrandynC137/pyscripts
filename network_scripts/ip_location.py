import argparse
import requests
import os
from dotenv import load_dotenv
from prettytable import PrettyTable
load_dotenv()

def get_ip_location(ip_address):
    try:
        # Get API key from environment variable
        access_token = os.getenv("NETWORK_SCRIPTS_API_KEY")
        
        # Check if the API key is missing
        if not access_token:
            raise ValueError("API key is missing. Please set the 'NETWORK_SCRIPTS_API_KEY' environment variable.")

        # Construct the API URL
        url = f"https://ipinfo.io/{ip_address}/json?token={access_token}"
        
        # Make the request to the API
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code != 200:
            raise Exception(f"Error: Received status code {response.status_code} from API.")

        # Try to parse the JSON response
        try:
            data = response.json()
        except json.JSONDecodeError:
            raise ValueError("Error parsing the JSON response from the API.")
        
        return data

    except requests.exceptions.RequestException as e:
        # Handle network errors (e.g., no internet, timeouts)
        print(f"Network error occurred: {e}")
        return None
    
    except ValueError as e:
        # Handle specific value errors (e.g., missing API key)
        print(f"Value error: {e}")
        return None
    
    except Exception as e:
        # Handle other general errors
        print(f"An error occurred: {e}")
        return None

def main():
    
    parser = argparse.ArgumentParser(description="Process command line arguments.")
    parser.add_argument("-ip", "--ip_address", type=str, help="IP address used for processing location.", required=True)
    args = parser.parse_args()

    location_data = get_ip_location(args.ip_address)

    table = PrettyTable()
    table.field_names = location_data.keys()
    table.add_row(location_data.values())

    print(table)

# This ensures that the main function only runs when the script is executed directly
if __name__ == "__main__":
    main()