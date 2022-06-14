def find_x(arry):
    """This function finds the missing number from the array.
    Given that the array consists of 1 to n """
    
    for x in range (1, len(arry)):
        if x not in arry:
            return x



if __name__ == "__main__":
    arry = [3,7,1,2,8,4,5]
    print(find_x(arry))