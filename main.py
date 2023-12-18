# Constants
CEMENT_PRICE = 3
GRAVEL_PRICE = 2
SAND_PRICE = 2
DISCOUNT_CEMENT = 1
DISCOUNT_GRAVEL = 2
DISCOUNT_SAND = 2
DISCOUNT_PRICE = 10

def display_menu():
    print("===== Building Material Sack Checker and Price Calculator =====")
    print("1. Check the contents and weight of a single sack")
    print("2. Check a customer's order for delivery")
    print("3. Calculate the price for a customer's order")
    print("4. Exit")
    print("===============================================================")

def check_single_sack():
    print("\nTASK 1: Check the contents and weight of a single sack")
    contents = input("Enter the contents (C for cement, G for gravel, S for sand): ")
    weight = float(input("Enter the weight of the sack (in kilograms): "))
    
    if contents == "C":
        if 24.9 <= weight <= 25.1:
            print("Accepted: Cement sack with correct weight")
        else:
            print("Rejected: Cement sack with incorrect weight")
    elif contents == "G" or contents == "S":
        if 49.9 <= weight <= 50.1:
            print("Accepted: Gravel/sand sack with correct weight")
        else:
            print("Rejected: Gravel/sand sack with incorrect weight")
    else:
        print("Rejected: Invalid contents")

def check_customer_order():
    print("\nTASK 2: Check a customer's order for delivery")
    total_weight = 0
    sacks_rejected = 0
    
    num_cement = int(input("Enter the number of cement sacks: "))
    num_gravel = int(input("Enter the number of gravel sacks: "))
    num_sand = int(input("Enter the number of sand sacks: "))
    
    for _ in range(num_cement):
        contents = "C"
        weight = float(input("Enter the weight of a cement sack (in kilograms): "))
        if 24.9 <= weight <= 25.1:
            total_weight += weight
        else:
            sacks_rejected += 1
    
    for _ in range(num_gravel):
        contents = "G"
        weight = float(input("Enter the weight of a gravel sack (in kilograms): "))
        if 49.9 <= weight <= 50.1:
            total_weight += weight
        else:
            sacks_rejected += 1
    
    for _ in range(num_sand):
        contents = "S"
        weight = float(input("Enter the weight of a sand sack (in kilograms): "))
        if 49.9 <= weight <= 50.1:
            total_weight += weight
        else:
            sacks_rejected += 1
    
    print(f"Total weight of the order: {total_weight} kilograms")
    print(f"Number of sacks rejected: {sacks_rejected}")

def calculate_order_price():
    print("\nTASK 3: Calculate the price for a customer's order")
    total_price = 0
    total_special_packs = 0
    
    num_cement = int(input("Enter the number of cement sacks: "))
    num_gravel = int(input("Enter the number of gravel sacks: "))
    num_sand = int(input("Enter the number of sand sacks: "))
    
    # Calculate regular price
    total_price += num_cement * CEMENT_PRICE
    total_price += num_gravel * GRAVEL_PRICE
    total_price += num_sand * SAND_PRICE
    
    # Check for special packs
    while num_cement >= DISCOUNT_CEMENT and num_sand >= DISCOUNT_SAND and num_gravel >= DISCOUNT_GRAVEL:
        total_price -= DISCOUNT_PRICE
        num_cement -= DISCOUNT_CEMENT
        num_sand -= DISCOUNT_SAND
        num_gravel -= DISCOUNT_GRAVEL
        total_special_packs += 1
    
    print(f"Regular price for the order: ${total_price}")
    
    if total_special_packs > 0:
        print(f"Special pack discount applied ({total_special_packs} pack(s)): -${DISCOUNT_PRICE * total_special_packs}")
        print(f"New price for the order: ${total_price}")
        print(f"Amount saved: ${DISCOUNT_PRICE * total_special_packs}")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1/2/3/4): ")
        
        if choice == "1":
            check_single_sack()
        elif choice == "2":
            check_customer_order()
        elif choice == "3":
            calculate_order_price()
        elif choice == "4":
            print("Thank you for using Building Material Sack Checker and Price Calculator. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
