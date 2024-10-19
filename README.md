# midterm_project
# Midterm Project: Dosa Restaurant Order Analysis

## Overview
This project aims to help a new Dosa restaurant design a better order management system by analyzing the orders received over the past year. The primary goal is to extract meaningful insights from the order data, which will assist the restaurant owner in understanding customer behavior and popular menu items.

## Project Structure
The project includes the following files:

- `example_orders.json`: Sample order data provided for analysis.
- `customers.json`: A JSON file containing customer information with phone numbers as keys and customer names as values.
- `items.json`: A JSON file containing menu items with their prices and the number of times each item has been ordered.
- `main.py`: The main Python script that processes the JSON order data.

## Goals
1. **Read JSON Orders**: The script reads orders from a JSON file whose name is passed as the first argument.
2. **Create `customers.json`**: Generates a JSON file with phone numbers as keys and customer names as values.
3. **Create `items.json`**: Generates a JSON file with item names as keys and an object containing the price and order count for each item.

## Installation
To run this project, you need to have Python installed on your machine. You can install Python from [python.org](https://www.python.org/downloads/).

## Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/ragztigadi/midterm_project.git
   cd midterm_project
