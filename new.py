import time
import requests
from requests.auth import HTTPBasicAuth

# Setup your Assembla API credentials and repository details
API_KEY = "f94007cf8b03be5aada5"
API_SECRET = "f906f3df5b63e0fbff9e9b346d9aceba7060b8ae"
PROJECT_NAME = "Arman"
FILE_PATH = ".travis.yml"
UPDATE_MESSAGE = "Add space to the end of file"

def get_file_content():
    """Fetch the content of the file from Assembla."""
    url = f"https://api.assembla.com/v1/spaces/{PROJECT_NAME}/documents"
    response = requests.get(url, auth=HTTPBasicAuth(API_KEY, API_SECRET))
    response.raise_for_status()
    return response.json()  # Adjust according to the API's response structure

def update_file(new_content):
    """Update the content of the file in Assembla."""
    url = f"https://api.assembla.com/v1/spaces/{PROJECT_NAME}/documents"  # Update with the correct endpoint
    data = {
        "content": new_content,
        "message": UPDATE_MESSAGE
    }
    response = requests.put(url, json=data, auth=HTTPBasicAuth(API_KEY, API_SECRET))
    response.raise_for_status()

def main():
    while True:
        try:
            current_content = get_file_content()

            # Process the content (make adjustments as needed)
            updated_content = current_content.rstrip() + " "  # Avoid accidental multiple spaces
            
            # Update the file
            update_file(updated_content)
            print("Successfully added a space to the file.")

        except requests.RequestException as e:
            print(f"Request error occurred: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

        time.sleep(180000)  # Sleep for 3000 minutes

if name == "main":
    main()