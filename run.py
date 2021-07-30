# Check 3x plus 1 for a list of numbers.


def run(max_number):
    output = (0, 0)
    print(f"Running 3x plus 1 from 1 to {max_number}")
    tenth = int(max_number / 10)
    for num in range(1, max_number):
        if num % tenth == 0:
            print(f"{num / tenth}/10")
        passes = 1
        returned_number = three_x(num)

        while returned_number != 1:
            passes += 1
            returned_number = three_x(returned_number)
        if passes > output[0]:
            output = passes, num
    print(f"{output[1]} Had the most passes with {output[0]}")


def three_x(operant):
    return make_odd(3 * operant + 1)


def make_odd(operant):
    if operant % 2 == 0:
        operant = int(operant / 2)
        operant = make_odd(operant)
    return int(operant)


run(10000000)
