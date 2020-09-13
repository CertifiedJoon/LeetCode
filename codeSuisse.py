#This is a python programme.
#Assumption 1: There is at least one set of numbers that adds up to target.
#Assumption 2: All inputs are between INT_MIN and INT_MAX.
#Assumption 3: There can be duplicate numbers.
#Methodologies: Recursive Function with Backtracking.
class Solution(object):
    def __init__(self, num, target):
        #If all numbers > 0, sorting num, thus using breaks, would considerably shorten the runtime.
        #However, since i assume there can be negative integer inputs, sorting will not help.
        #An integer array to store the indexes of the shortest combination sum.
        #Since there is at least one set of numbers, it is convenient for calculation to declare this variable as the original input.
        shortest_combination = [i for i in range(len(num))]
        #Calls a Recursive function to calculate the shortest_combination
        self.find_combination(0, num, shortest_combination, [], target)
        print(shortest_combination)

    #A recursive, backtracking, function to find all combination sum, and by doing so, the shortest combination sum
    def find_combination(self, starting_index, num, shortest_combination, current_combination, target):
         #If current_combination adds up to the target
        if target == 0:
            #If current_combination is shorter than the shortest combination
            if (len(current_combination) < len(shortest_combination)):
                #Simple assignment using "=" is reset while backtracking, thus used s.extend()
                shortest_combination.clear()
                shortest_combination.extend(current_combination)
            return

        #recursivity starts here
        for i in range(starting_index, len(num)):
            #i+1 since one element can only be used once, target-num[i] to see if combination of numbers adds up to target
            #extend current_combination with the interating index
            self.find_combination(i + 1, num, shortest_combination, current_combination + [i], target-num[i])

print(Solution([1,6,8,16,17], 24))
