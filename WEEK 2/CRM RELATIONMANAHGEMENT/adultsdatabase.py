import pymongo
import pandas as pd

if __name__ == "__main__":
    print("SERVER RUNNING")

    # Connect to MongoDB
    client = pymongo.MongoClient("mongodb://localhost:27017")
    print(client)

    # Database name
    database = client["Adults_Data_DATABASE"]

    # Creating collection
    collection = database['ADULTS_DATA']

    # Read CSV file into DataFrame
    csv_data = pd.read_csv('adult.csv')

    # Convert DataFrame to list of dictionaries
    adults_records = csv_data.to_dict(orient='records')

    # Remove the '_id' field from each dictionary
    for record in adults_records:
        record.pop('_id', None)

    # Insert records into MongoDB
    result = collection.insert_many(adults_records)

    # Print the inserted documents' IDs
    print("Successfully Inserted :) :", result.inserted_ids)

    # Close the connection
    client.close()
