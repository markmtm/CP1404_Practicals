def main():
    score = float(input("Enter score: "))
    result = get_result(score)
    print(result)


def get_result(score):
    if score < 0:
        result = "Invalid score"
    elif score > 100:
        result = "Invalid score"
    elif score >= 90:
        result = "Excellent"
    elif score >= 50:
        result = "Passable"
    else:
        result = "Bad"
    return result

main()