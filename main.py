#REMOVE PASS AND FIX THE FUNCTION
#change to test push and forks
def sum_of_products(list1, list2):
    math_sum = 0 
    for i in range(len(list1)):
        math_sum +=(int(list1[i]) * int(list2[i]))
        return math_sum

if __name__ == '__main__':
    in1 = (input()).split()
    in2= (input()).split()

    result= sum_of_products(in1, in2)
    print (result)
    ('Error.')
    #fi