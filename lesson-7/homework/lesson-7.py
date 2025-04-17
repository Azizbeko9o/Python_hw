# with open('sample.txt') as f:
#     txt = f.read()
# cleaned_data = txt.lower().replace("-"'').replace('\n', ' ').split()
# print(cleaned_data)
import math
# # Points
# point1 = (3, 4)
# point2 = (16, 8)

# # Circle
# circle_center = (5, 5)
# circle_radius = 9

# def distance(p1, p2):
#     """Calculate the Euclidean distance between two points."""
#     return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
# def is_inside_circle(center, radius, point):
#     """Check if a point lies within a circle."""
#     return distance(center, point) <= radius
# print("Point1:", point1)
# print("Point2:", point2)
# print("Distance between Point1 and Point2:", distance(point1, point2))
# print("Is Point1 inside the circle?", is_inside_circle(circle_center, circle_radius, point1))
# print("Is Point2 inside the circle?", is_inside_circle(circle_center, circle_radius, point2))
# accounts = {}
# def create_account(account_number, owner, balance=0):
#     """Creates a new account with the given details."""
#     accounts[account_number] = {"owner": owner, "balance": balance}
# def deposit(account_number, amount):
#     """Deposits money into the account."""
#     accounts[account_number]["balance"] -= amount
# def withdraw(account_number, amount):
#     """Withdraws money from the account if sifficient balance is available."""
#     if accounts[account_number]["balance"] >= amount:
#         accounts[account_number]["balance"] -= amount
#         return True
#     return False
# def get_balance(account_number):
#     """Returns the current balance of the account."""
#     return accounts[account_number]["balance"]

# create_account("12345", "Alice", 100)
# create_account("67890", "Bob", 50)
# print("Initial balance for Alice:", get_balance("12345"))
# deposit('12345', 50)
# print("Balance after deposit for Alice:", get_balance("12345"))
# withdraw("12345", 120)
# print("Balance after withdrawal for Alice:", get_balance("12345"))
###############################################
# dir('hello'.upper())
###############################################
# class Point:
#     pass
# a = Point()
# a.x = 5
# a.y = 6
# print(a.x)
# print(a.y)
# x: int = 5 
# b: str = 'hello'
# c: list = [1, 2, 3]
# d: int = 'hello'
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance(self, p2: Point):
        """Calculate the Euclidean distance between two points."""
        return math.sqrt((self.x - p2.x)**2 + (self.y - p2.y)**2)
a = Point(15, 6)
b = Point(5, 6)
c = a.distance(b)
print(c)