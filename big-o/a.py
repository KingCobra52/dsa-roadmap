a_list = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#linear solution
def linear_solution(the_list: list):
    min = the_list[0]
    for num in the_list[1:]:
        if num < min:
            min = num
    return min

#n^2 solution
def quadratic_solution(the_list: list):
    for i in range(len(the_list)):
        is_min = True
        for j in range(len(the_list)):
            if the_list[j] < the_list[i]:
                #the_list[i] is NOT the min
                is_min = False
                break

        if is_min:
            return the_list[i]

def main():
   print(linear_solution(a_list))
   print(quadratic_solution(a_list))

if __name__ == "__main__":
    main()
