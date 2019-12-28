# https://www.codewars.com/kata/54d496788776e49e6b00052f

from collections import defaultdict
from math import sqrt


def is_prime(number):
    for i in range(2, int(sqrt(number))+1):
        if number % i == 0:
            return False
    return True

def get_prime(number):
    abs_number = abs(number)
    return [i for i in range(2, abs_number+1) if is_prime(i) and abs_number % i == 0]

def sum_for_list(lst):
    prime_numbers = defaultdict(int)
    for number in lst:
        for prime in get_prime(number):
            prime_numbers[prime] += number
    return sorted([[prime, sum] for prime, sum in prime_numbers.items()])