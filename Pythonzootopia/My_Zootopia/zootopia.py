import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve the API key from environment variables
API_KEY = "WrUCy90a0IavXJjWhX/l+w==yUxP0mygfyNo2Rkm"
BASE_URL = "https://api.api-ninjas.com/v1/animals"


def get_animal_info(animal_name):
    """
    Fetches information about an animal from the API Ninja Animals API.

    Parameters:
        animal_name (str): The name of the animal to search for.

    Returns:
        dict: The API response in JSON format if successful, or an error message.
    """
    url = f"{BASE_URL}?name={animal_name}"
    headers = {"X-Api-Key": API_KEY}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()  # Successful response
    else:
        return {"error": f"Error {response.status_code}: {response.text}"}


if __name__ == "__main__":
    animal = input("Enter the name of an animal: ").strip().lower()
    result = get_animal_info(animal)

    print(result)
