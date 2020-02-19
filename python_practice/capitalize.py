

# Complete the solve function below.
def solve(s):
    
    for letter in s.split():
        s = s.replace(letter, letter.capitalize())
    return s
