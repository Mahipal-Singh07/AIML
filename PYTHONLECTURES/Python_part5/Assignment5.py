import os 

#Q1
# with open("names.txt","w") as f:
#     f.write("Mahipal\n")
#     f.write("Rahul\n")
#     f.write("Amit\n")
#     f.write("Rohit\n")
#     f.write("Vikas\n")

# with open("names.txt","r") as f:
#     print(f.read())

#Q2
# with open("log.txt","a") as f:
#     f.write("Program run successfully")

# with open("log.txt","r") as f:
#     print(f.read())    

#Q3

# nums=[5,10,15,20,25]

# nums=[val for val in nums if val>15]
# print(nums)

#Q4
import json

# 1. Create dictionary of 3 cities
cities = {
    "Delhi": 30000000,
    "Mumbai": 20000000,
    "Pune": 15000000
}

# 2. Save dictionary into JSON file
with open("cities.json", "w") as f:
    json.dump(cities, f, indent=4)

print("Data saved successfully!")

# 3. Read JSON file
with open("cities.json", "r") as f:
    data = json.load(f)

# Print each city and population
print("\nCity Populations:")

for city, population in data.items():
    print(city, ":", population)

# 4. Take new city and population from user
new_city = input("\nEnter new city: ")
new_population = int(input("Enter population: "))

# 5. Update dictionary
data[new_city] = new_population

# 6. Save updated data into JSON file
with open("cities.json", "w") as f:
    json.dump(data, f, indent=4)

print("\nUpdated city data successfully!")

# 7. Display updated JSON data
print("\nUpdated City Populations:")

for city, population in data.items():
    print(city, ":", population)

#Q5
import json

try:
    with open("cities.json","r") as f:
        data=json.load(f)

    for cities,population in data.items():
       print(city,":",population)

except FileNotFoundError:
    print("cities.json file not found!")  

except json.JSONDecodeError:
    print("Invalid JSON data!")

finally :
    print("Work done successfully !")    
        