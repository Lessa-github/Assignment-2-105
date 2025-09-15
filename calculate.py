#!/usr/bin/env python3
import cgi
import cgitb
import math
import os
from datetime import datetime

cgitb.enable()

# To read URL parameters, we use the QUERY_STRING environment variable
query_string = os.environ.get('QUERY_STRING', '')
params = {}
if query_string:
    params = dict(qc.split("=") for qc in query_string.split("&"))

# Get the values for a, b, and c, converting them to float
# Set a default value of 0.0 if not provided
try:
    a = float(params.get('a', '1.0')) # Avoid division by zero
    b = float(params.get('b', '0.0'))
    c = float(params.get('c', '0.0'))
except (ValueError, TypeError):
    a, b, c = 1.0, 0.0, 0.0

# Ensure 'a' is not zero
if a == 0:
    a = 1.0

# Step 1: Calculate c^3
c_cubed = c ** 3

# Step 2: Calculate the square root of c^3
# Use a try-except block to handle roots of negative numbers
try:
    sqrt_c_cubed = math.sqrt(c_cubed)
except ValueError:
    sqrt_c_cubed = 0.0 # Undefined result, treated as 0

# Step 3: Divide by a
division_result = sqrt_c_cubed / a

# Step 4: Multiply by 10
multiplication_result = division_result * 10

# Step 5: Add b
final_result = multiplication_result + b

current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Print the HTTP header and the HTML response body
print("Content-Type: text/html\r\n")
print("===========================================<br>")
print("Assignment #2<br>")
print("Lessa<br>") # Replace with your last name
print(f"Final Result: {final_result:.1f}<br>")
print(f"Step 1: c = {c:.1f} , c³ = {c_cubed:.1f}<br>")
print(f"Step 2: √(c³) = {sqrt_c_cubed:.1f}<br>")
print(f"Step 3: {sqrt_c_cubed:.1f} / {a:.1f} = {division_result:.1f}<br>")
print(f"Step 4: {division_result:.1f} * 10 = {multiplication_result:.1f}<br>")
print(f"Step 5: {multiplication_result:.1f} + {b:.1f} = {final_result:.1f}<br>")
print(f"<br>Calculation completed at {current_time}<br>")
print("===========================================<br>")