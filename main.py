##################################################
'''
Q1: 
'''

def cube_a_number(x):
    result = x * x * x
    return result

cubed_res = cube_a_number(10)
print(f'The result is {cubed_res}.')

##################################################
'''
Q2:
'''

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
 
result = is_even(13)    # result => True or False
print(f'13 is even: {result}')

##################################################
'''
Q3:
'''

def is_even(n):
    return n % 2 == 0
 
result = is_even(13)    # result => True or False
print(f'13 is even: {result}')

##################################################
'''
Q4:
'''

def score_to_gpa(score):
    return round(score / 25, 1)

alice_score = score_to_gpa(50)  # 2.0
bob_score = score_to_gpa(90)    # 3.6

##################################################
'''
Challenge
'''

def middle_of_3(n1, n2, n3):
   if n1 < n2:
        if n2 < n3:
           return n2
        elif n1 < n3:
           return n3
        else:
            return n1
   else:
        if n3 < n2:
            return n2
        elif n1 < n3:
            return n1
        else:
            return n3

##################################################
