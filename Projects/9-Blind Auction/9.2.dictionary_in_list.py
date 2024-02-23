travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

#Function to add to travel_log
def add_new_country(country, times_of_visit, cities_visited):
    travel_log.append(
        {"country": country,
         "visits": times_of_visit,
         "cities": cities_visited
         }
    )

#User input
country_visited = input("Which country did you visit? ")
times = int(input("How many times have you visited that country? "))
cities = input("Which cities did you visit? ").split()

#Function call and argument passing
add_new_country(country= country_visited, times_of_visit= times, cities_visited= cities)

print(travel_log)