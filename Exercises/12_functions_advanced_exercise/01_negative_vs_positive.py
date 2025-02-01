def sum_negative(*args):
    sum_neg = 0
    for num in args:
        if num < 0:
            sum_neg += num
    return sum_neg
def sum_positive(*args):
    sum_pos = 0
    for num in args:
        if num > 0:
            sum_pos += num
    return sum_pos

numbers = [int(n) for n in input().split()]
negative_sum = sum_negative(*numbers)
positive_sum = sum_positive(*numbers)

print(negative_sum)
print(positive_sum)

def absolute_comparison(pos_sum, neg_sum):
    if pos_sum < abs(neg_sum):
        print("The negatives are stronger than the positives")
    else:
        print("The positives are stronger than the negatives")

absolute_comparison(positive_sum, negative_sum)
