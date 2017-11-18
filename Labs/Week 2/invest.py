# import modules
import math

# function to calculate the investment over 3 years
def invest():
    '''
    Invest amount1 euro at rate interest
    write the numbers for each year
    '''

    # Input amount1, rate
    amount = float(input("initial amount = "))
    rate = float(input("invest rate = "))

    # calculate and print amount1, interst1, finalAmount1
    amount1 = amount
    interest1 = amount1 * rate
    finalAmount1 = amount1 + interest1

    print("Year 1 (amount, interest, final amount): ", amount1, interest1, finalAmount1)

    # calculate and print amount2, interst2, finalAmount2 
    amount2 = finalAmount1
    interest2 = amount2 * rate
    finalAmount2 = amount2 + interest2

    print("Year 1 (amount, interest, final amount): ", amount2, interest2, finalAmount2)


    # calculate and print amount3, interst3, finalAmount3

    amount3 = finalAmount2
    interest3 = amount3 * rate
    finalAmount3 = amount3 + interest1

    print("Year 1 (amount, interest, final amount): ", amount3, interest3, finalAmount3)



# end def

invest()
