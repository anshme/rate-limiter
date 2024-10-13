from server import server
import requests

user_name = "Anshuman"
password = "****"

if __name__ == '__main__':
    # URL of the Flask server
    name = "Anjuman"
    url = f'http://127.0.0.1:2002/ping/{name}'

    # Make a GET request to the server
    try:
        response = requests.get(url)
        # Print the response from the server
        if response.status_code == 200:
            print("Server Response:", response.text)
        else:
            print(f"Failed to reach server. Status code: {response.status_code}")
    except Exception as err:
        print(f"{err.__class__}")