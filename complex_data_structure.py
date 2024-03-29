complex_data = [
{
"name": "Alice",
"age": 30,
"details": {
"address": ("123 Main St", "City", "Country"),
"contacts": ["email@example.com", "123-456-7890"]
}
},
{
"name": "Bob",
"age": 35,
"details": {
"address": ("456 Oak St", "Town", "Country"),
"contacts": ["bob@example.com", "987-654-3210"]
}
}
]


#1.Printing first name from data

print(complex_data[0]["name"])

#2.Displaying the age of the second person

print(complex_data[1]["age"])

#3.Show the complete address of the first person.

address = complex_data[0]["details"]["address"]
street, city, country = address
print("Address:", street, city, country)

#4.Print the second contact of the second person.

contact = complex_data[1]["details"]["contacts"][1]
print("Second contact of the second person:", contact)

#5.Display the city of the first person's address.

city = complex_data[0]["details"]["address"][1]
print("City of the first person's address:", city)

#6.Print the email address of the second person

email = complex_data[1]["details"]["contacts"][0]
print("Email address of the second person:", email)

#7.Show the country of the second person's address.

country = complex_data[1]["details"]["address"][2]
print("Country of the second person's address:", country)

#8.Print the number of contacts the first person has.

num_contacts = len(complex_data[0]["details"]["contacts"])
print("Number of contacts for the first person:", num_contacts)

#9.Display the street name of the second person's address.

street = complex_data[1]["details"]["address"][0]
print("Street name of the second person's address:", street)

#10. Print the number of characters in the first person's name.

name_length = len(complex_data[0]["name"])
print("Number of characters in the first person's name:", name_length)
