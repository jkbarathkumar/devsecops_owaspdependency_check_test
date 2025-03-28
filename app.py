import requests
import numpy as np

# Function to fetch data from a URL
def fetch_data(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        
        # Raise an exception if the response is not successful
        response.raise_for_status()
        
        # Return the JSON content of the response
        return response.json()
    
    except requests.exceptions.RequestException as e:
        # If there's an error, print it and return None
        print(f"Error fetching data from {url}: {e}")
        return None

# Function to calculate the mean of a list of numbers
def calculate_mean(numbers):
    if not numbers:
        print("The list is empty. Cannot calculate mean.")
        return None
    
    # Calculate the mean using numpy
    return np.mean(numbers)

# Example usage
if __name__ == "__main__":
    # Example URL for fetching data (replace with a real API or URL)
    url = "https://jsonplaceholder.typicode.com/todos/1"
    
    # Fetch data from the URL
    data = fetch_data(url)
    
    if data:
        print("Fetched Data:", data)
    
    # Example numbers for calculating the mean
    numbers = [1, 2, 3, 4, 5]
    
    # Calculate the mean of the numbers
    mean = calculate_mean(numbers)
    
    if mean is not None:
        print(f"The mean of the numbers {numbers} is {mean}")
