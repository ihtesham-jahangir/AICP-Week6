# Building Material Sack Checker and Price Calculator

This Python program allows users to check the contents and weight of building material sacks and calculate the price of customer orders. The program is designed to ensure that correct orders are prepared for delivery while providing pricing information.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Overview

The manager of a building materials delivery service requires a tool to validate sacks of different building materials, such as cement, gravel, and sand. The program checks the contents and weight of each sack, ensuring they meet specific criteria, and calculates the price for customer orders based on the number and type of sacks.

## Features

### 1. Check the Contents and Weight of a Single Sack

- Users can enter the contents and weight of a single sack.
- The program verifies that the contents are valid (C for cement, G for gravel, S for sand).
- The weight is validated, ensuring it falls within acceptable ranges.
- Accepted sacks are confirmed, and rejected sacks display the reason(s) for rejection.

### 2. Check a Customer's Order for Delivery

- Users can input the number of sacks of each type required for a customer's order.
- The program uses Task 1 to check the contents and weight of each sack.
- It calculates the total weight of the order and counts the number of rejected sacks.

### 3. Calculate the Price for a Customer's Order

- Users input the number of sacks of each type required for a customer's order.
- The program calculates the regular price for the order based on the quantity and type of sacks.
- It checks for special packs (e.g., 1 sack of cement, 2 sacks of sand, and 2 sacks of gravel) and applies discounts when applicable.
- The program displays the regular price, any applied discounts, and the final price, along with the amount saved.

## Usage

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/ihtesham-jahangir/AICP-Week6
Navigate to the project directory:

bash
Copy code
cd building-material-sack-checker
Run the program by executing the following command:

#BASH
python sack_checker.py

Follow the on-screen instructions to perform the tasks as described in the Features section.

Contributing
Contributions to this project are welcome! If you find any issues, want to enhance the program, or have suggestions, please feel free to submit a pull request.

License
This project is licensed under the MIT License - see the LICENSE file for details.




