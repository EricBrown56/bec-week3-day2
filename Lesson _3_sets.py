'''
Task 1: Flight Route Comparison Imagine you work for an airline and need to compare the flight routes of your airline with a competitor. You have two sets of flight destinations, one for each airline. Write a Python program to find out:

Destinations that both airlines fly to.
Destinations unique to your airline.
Whether there are any destinations that neither airline shares.
Example Code:'''

our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

# Destinations that both airlines fly to.
# The intersection() method returns a set that contains the similarity between two or more sets.

def destinations_both_airlines(our_routes, competitor_routes):
    both = our_routes.intersection(competitor_routes)
    print(f'The destinations that both airlines fly to are: {both}')

destinations_both_airlines(our_routes, competitor_routes)

print('=' * 100)
# Destinations unique to your airline.
# The difference() method returns a set that contains the difference between two sets.

def destinations_unique_airline(our_routes, competitor_routes):
    unique = our_routes.difference(competitor_routes)
    print(f'The destinations that are unique to our airline are: {unique}')

destinations_unique_airline(our_routes, competitor_routes)

print('=' * 100)

# Whether there are any destinations that neither airline shares.
# The symmetric_difference() method returns a set that contains all items from both sets, except items that are present in both sets.

def destinations_neither_airline(our_routes, competitor_routes):
    neither = our_routes.symmetric_difference(competitor_routes)
    print(f'The destinations that neither airline shares are: {neither}')

destinations_neither_airline(our_routes, competitor_routes)

print('=' * 100)
print('=' * 100)

'''
Task 1: Duplicate Entries Cleanup You are given a list of customer IDs, some of which are duplicated. Write a Python function to remove duplicates and display the unique customer IDs.
'''
customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]

def remove_duplicates(customer_ids):
    unique_customer_ids = set(customer_ids)
    print(f'The unique customer IDs are: {unique_customer_ids}')

remove_duplicates(customer_ids)



