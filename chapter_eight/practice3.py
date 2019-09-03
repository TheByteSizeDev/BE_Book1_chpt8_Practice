''' 
Create a function called calc_dollars. In the function body, define a dictionary and store it in a variable named piggyBank. The dictionary should have the following keys defined.

quarters
nickels
dimes
pennies
For each coin type, give yourself as many as you like.

piggyBank = {
    "pennies": 342,
    "nickels": 9,
    "dimes": 32
}

Once you have given yourself a large stash of coins in your piggybank, look at each key and perform the appropriate math on the integer value to determine how much money you have in dollars. Store that value in a variable named dollarAmount and print it.

Given the coins shown above, the output would be 7.07 when you call calc_dollars()
'''

def calc_dollars():

    piggyBank = {
        "quarters": 250,
        "nickels": 34,
        "dimes": 122,
        "pennies": 324
    }

    total_quarters = piggyBank['quarters'] * .25
    total_nickels = piggyBank['nickels'] * .05
    total_dimes = piggyBank['dimes'] * .10
    total_pennies = piggyBank['pennies'] * .01
    total_dollars = total_quarters + total_dimes + total_nickels + total_pennies
    
    print(f"You have $ {total_dollars}")

calc_dollars()

