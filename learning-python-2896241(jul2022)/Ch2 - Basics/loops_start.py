#
# Example file for working with loops
# LinkedIn Learning Python course by Joe Marini
#


def main():
    x = 3

    # TODO: define a while loop
    # while(x<5):
    #     print(x)
    #     x = x + 1



    # TODO: define a for loop
    # for x in range(5,10):
    #     print(x)

    # TODO: use a for loop over a collection
    days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]

    for d in days:
        print(d)


    # TODO: use the break and continue statements
    
    for x in range(5,10):
        # if x == 7:
        #     break
        if x % 2 == 0:
            continue
        print(x)

    # TODO: using the enumerate() function to get index 
    for i,d in enumerate(days):
        print (i, d)
  
  # Since the index starts with 0, Monday will be marked with 0
  # If we wanted to see counting start at 1, print(i+1, d)

if __name__ == "__main__":
    main()
