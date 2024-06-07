import requests
from bs4 import BeautifulSoup
import json

# Send a GET request to the website
url = "https://guidestarindia.org/Search.aspx?q=+reliance"
response = requests.get(url)

if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.content, "html.parser")

    # Find all elements with the class name "CPBData"
    cpb_data_elements = soup.find_all(class_="CPBData")

    # Initialize the output dictionary
    output = {}

    # Loop through each CPBData element
    for element in cpb_data_elements:
        # Find all span tags within the current element
        span_tags = element.find_all("span")

        # Extract key from the first span tag
        key = span_tags[0].get_text(strip=True).lower().replace(" ", "_")

        # Extract values from subsequent span tags
        values = [span.get_text(strip=True) for span in span_tags[1:]]

        # Join values into a single string
        value = ", ".join(values)

        # Store key-value pair in output dictionary
        output[key] = value

    # Serialize the dictionary into a JSON string
    json_data = json.dumps(output, ensure_ascii=False)

    # Write the JSON string to a file
    with open("output.json", "w", encoding="utf-8") as json_file:
        json_file.write(json_data)

    print("Data saved to output.json file.")

else:
    print("Failed to retrieve data from the website.")
