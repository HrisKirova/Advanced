def check_gift(sum_won):
    if 100 <= sum_won <= 199:
        return "Football"
    elif 200 <= sum_won <= 299:
        return "Teddy Bear"
    elif sum_won >= 300:
        return "Lego Construction Set"

matrix = [input().split() for _ in range(6)]
sum_col = 0


for throw in range(3):
    current_row, current_col = map(int, input().strip("()").split(", "))
    if current_row < 0 or current_row > 5 or current_col < 0 or current_col > 5:
        continue
    if matrix[current_row][current_col] == "B":
        for row in range(6):
            if matrix[row][current_col].isdigit():
                sum_col += int(matrix[row][current_col])
                matrix[row][current_col] = "0"

if sum_col >= 100:
    prize = check_gift(sum_col)
    print(f"Good job! You scored {sum_col} points, and you've won {prize}.")
else:
    print(f"Sorry! You need {100 - sum_col} points more to win a prize.")

