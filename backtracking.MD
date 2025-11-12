# Backtracking algorithm
- constraint satisfaction problems
- incrementally build a solution
- explores possible solutions by extending a partial solution
- if partial solution cannot be extendeed to a valid **complete** solution (violates a constraint)
- Then backup (backtrack) to previous point.
- exhausted search

```python
def solve_problem_backtracking(initial_state):
    current_solution = []
    
    all_solutions = [] 

    backtrack(current_solution, all_solutions)
    
    return all_solutions[0] if all_solutions else "No solution found"

def backtrack(current_solution, all_solutions):
    
    if is_solution(current_solution):
        all_solutions.append(current_solution.copy()) 
        return

    for candidate in get_candidates(current_solution):
        
        if is_valid(current_solution, candidate):
            
            current_solution.append(candidate) 
            backtrack(current_solution, all_solutions)
            
            current_solution.pop() 


def is_solution(current_solution):
    return False

def get_candidates(current_solution):
    return range(1) 

def is_valid(current_solution, candidate):
    return True
```

```python
# all permuatations
def find_permutations(nums):
    """
    Finds all unique permutations of the given array of numbers using backtracking.

    :param nums: A list of integers (or any hashable type) to permute.
    :return: A list of lists, where each inner list is a unique permutation.
    """
    all_permutations = []
    n = len(nums)

    def backtrack(current_permutation):
        # 1. Base Case (Goal Check): A permutation is complete when its length
        # matches the length of the original array.
        if len(current_permutation) == n:
            # We found a complete permutation. Store a copy of it.
            all_permutations.append(list(current_permutation))
            return

        # 2. Recursive Step (Explore Candidates):
        # The candidates are the numbers from the original 'nums' array
        # that have NOT yet been used in the 'current_permutation'.
        for num in nums:
            
            # 3. Constraint Check (Safety):
            # Check if the current number (candidate) is already in the
            # current partial permutation. If it is, skip it.
            if num not in current_permutation:
                
                # 4. Make a Choice (Action):
                # Add the candidate to the current partial permutation.
                current_permutation.append(num)
                
                # 5. Recurse:
                # Move to the next depth level to find the next element.
                backtrack(current_permutation)
                
                # 6. Backtrack (Undo):
                # Remove the element we just added before trying the next candidate.
                # This clears the choice and allows the search to branch to a new path.
                current_permutation.pop()

    # Start the backtracking process with an empty initial permutation.
    backtrack([])
    
    return all_permutations
```