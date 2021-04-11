# Time Complexity: O(n)
# Space Complexity: O(1) because I used two variables

# Find the maximum profit with only one trasaction (buying and selling a stock)
def buy_sell_stock(prices):
    min_profit = math.inf
    max_profit = 0
            
    for i in range(len(prices)):
        if prices[i] < min_profit:
            min_profit = prices[i]
        else:
            # if we can find bigger profit than max_profit
            candidate_max_profit = prices[i] - min_profit 
            if pcandidate_max_profit > max_profit:
                max_profit = candidate_max_profit
    
    return max_profit

##################################
########### Approach 1 ###########
##################################
# Time Complexity: O(nlogn)
# Space Complexity: O(n)
def find_k_most_frequent_num(k, nums):
    counter = {}
    
    # O(n)
    for num in nums:
        if num in counter.keys():
            counter[num] += 1
        else:
            counter[num] = 1
    #O(nlogn)
    sorted_counter = sorted(counter.items(), key=lambda item:-item[1]) #this will output tuple, sorted in ascending order

    #O(k)
    return [k for k, v in sorted_counter[:k]]

##################################
########### Approach 2 ###########
##################################
# I will solve the above problem again using QuickSelect algorithm to improve time complexity
# Time Compexity: average O(n), worst case O(n^2) using QuickSelect
# Space Complexity: O(n)

def find_k_most_frequent_num(k, nums):
    def partition(left_idx, right_idx):
        #randomly select pivot
        pivot_idx = random.randint(left_idx, right_idx)
        pivot_freq = counter[unique_elem[pivot_idx]] 

        # move pivot to the right end
        unique_elem[pivot_idx], unique_elem[right_idx] = unique_elem[right_idx], unique_elem[pivot_idx]  

        # push less freq elems to the left
        future_pivot = left_idx
        for i in range(left_idx, right_idx):
            if counter[unique_elem[i]] < pivot_freq:
                unique_elem[future_pivot], unique_elem[i] = unique_elem[i], unique_elem[future_pivot]
                future_pivot += 1

        # move pivot back to the middle place
        unique_elem[right_idx], unique_elem[future_pivot] = unique_elem[future_pivot], unique_elem[right_idx]  

        return future_pivot

    def quickselect(left_idx, right_idx, k):
        # base case: when it has only one elem
        if left_idx == right_idx: 
            return

        pivot_idx = partition(left_idx, right_idx)

        # if pivot position is same as k
        # then (n - k)th less freq element in (n - k) sorted list.
        if k == pivot_idx:
            return 
        # recur for the left part
        elif k < pivot_idx:
            quickselect(left_idx, pivot_idx - 1, k)
        # recur for the right part
        else:
            quickselect(pivot_idx + 1, right_idx, k)
    
    #####run quickselect algorithm####
    counter = {}

    # O(n)
    # Count the number of each unique element
    for num in nums:
        if num in counter.keys():
            counter[num] += 1
        else:
            counter[num] = 1

    unique_elem = list(counter.keys())
    n = len(unique_elem)
    
    quickselect(0, n - 1, n - k)

    # Return k most frequent elements
    return unique_elem[n - k:]

