from pymongo import MongoClient

# Replace the URI with your MongoDB connection string
client = MongoClient('mongodb+srv://satyakarthikvelivela:firescrim123@firescrim.wxzexrz.mongodb.net/')

# Replace 'your_database' with the name of your database
db = client['registration']

# Replace 'your_collection' with the name of your collection
collection = db['squadpayments']

# Query to find all documents in the collection and store phone numbers in an array
phone_numbers = [doc['phoneno'] for doc in collection.find({}, {'phoneno': 1, '_id': 0}).skip(2) if 'phoneno' in doc]

# Print the phone numbers
print(phone_numbers)

# Close the MongoDB connection
client.close()