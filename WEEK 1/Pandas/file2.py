# scraopping data into excel using pandas and playwright library

 # playwright library is used to fetch any web data

from playwright.sync_api import sync_playwright
import pandas as pandu



# Importing necessary libraries
from playwright.sync_api import sync_playwright
import pandas as pd

# Define the main function
def main():
    # Start a Playwright session
    with sync_playwright() as p:

        # Set the check-in and check-out dates for the hotel search
        checkin_date = '2023-03-23'
        checkout_date = '2023-03-24'

        # Construct the URL for the hotel search using the provided dates and location (Paris)
        page_url = f'https://www.booking.com/searchresults.en-us.html?checkin={checkin_date}&checkout={checkout_date}&selected_currency=USD&ss=Paris&ssne=Paris&ssne_untouched=Paris&lang=en-us&sb=1&src_elem=sb&src=searchresults&dest_type=city&group_adults=1&no_rooms=1&group_children=0&sb_travel_purpose=leisure'

        # Launch a Chromium browser instance
        browser = p.chromium.launch(headless=False)
        # Create a new browser page
        page = browser.new_page()
        # Navigate to the constructed URL, allowing a timeout of 60000 milliseconds (60 seconds)
        page.goto(page_url, timeout=60000)

        # Find all hotel elements on the page using a specific locator
        hotels = page.locator('//div[@data-testid="property-card"]').all()
        # Print the number of hotels found
        print(f'There are: {len(hotels)} hotels.')

        # Initialize an empty list to store hotel information
        hotels_list = []

        # Iterate through each hotel element found
        for hotel in hotels:
            # Create a dictionary to store hotel details
            hotel_dict = {}
            # Extract the hotel name using a specific locator and add it to the dictionary
            hotel_dict['hotel'] = hotel.locator('//div[@data-testid="title"]').inner_text()
            # Extract the hotel price using a specific locator and add it to the dictionary
            hotel_dict['price'] = hotel.locator('//span[@data-testid="price-and-discounted-price"]').inner_text()
            # Extract the hotel score using a specific locator and add it to the dictionary
            hotel_dict['score'] = hotel.locator('//div[@data-testid="review-score"]/div[1]').inner_text()
            # Extract the average review rating using a specific locator and add it to the dictionary
            hotel_dict['avg review'] = hotel.locator('//div[@data-testid="review-score"]/div[2]/div[1]').inner_text()
            # Extract the number of reviews using a specific locator, split it, and add it to the dictionary
            hotel_dict['reviews count'] = hotel.locator('//div[@data-testid="review-score"]/div[2]/div[2]').inner_text().split()[0]

            # Append the hotel dictionary to the list of hotels
            hotels_list.append(hotel_dict)

        # Convert the list of hotel dictionaries into a pandas DataFrame
        df = pd.DataFrame(hotels_list)
        # Write the DataFrame to an Excel file
        df.to_excel('hotels_list.xlsx', index=False)
        # Write the DataFrame to a CSV file
        df.to_csv('hotels_list.csv', index=False)

        # Close the browser instance
        browser.close()

# Check if the script is being run directly
if __name__ == '__main__':
    # Call the main function
    main()
