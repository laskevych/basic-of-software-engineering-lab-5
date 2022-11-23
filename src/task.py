
def calculate(x: float, n: int) -> float:
    y: float = 0

    if x >= 0:
        for i in range(0, n):
            if i <= 0:
                continue

            y += x / i
    else:
        for i in range(0, n):

            sub_loop_sum: float = 0
            for j in range(1, n + 1):
                sub_loop_sum += x - i + j

            y += sub_loop_sum

    return y


def print_to_console(start: float, end: float, step: float, loop_iterations: int) -> None:
    while start <= end:
        print("X = {0}; Y = {1}".format(start, calculate(start, loop_iterations)))
        start += step


def save_to_file(start: float, end: float, step: float, loop_iterations: int) -> None:
    with open('tmp/calculation_result.txt', 'w') as file:
        while start <= end:
            file.write("X = {0}; Y = {1}\n".format(start, calculate(start, loop_iterations)))
            start += step


def ask_values() -> tuple:
    print("Please, enter number values for variables:")

    start = float(input("start: float = "))
    end = float(input("end: float = "))
    step = float(input("step: float = "))
    loop_iterations = int(input("loop_iterations: int = "))

    return start, end, step, loop_iterations


def validate_values(start: float, end: float, step: float, loop_iterations: int) -> None:
    if loop_iterations <= 0:
        raise InvalidValueOfLoopIterationsError("Error! Number of loop iterations must be greater than 0.")

    if start > end:
        raise InvalidValueOfStartEndError("Error! Variable `from` must be less than `to`.")

    if step <= 0:
        raise InvalidValueOfStepError("Error! Variable `step` must be greater than 0.")


def ask_save_result_to_file() -> bool:
    answer = int(input("Do you want to save result to file? Type: `0` - No; `1` - Yes: "))

    if answer == 0:
        return False
    elif answer == 1:
        return True
    else:
        raise ValueError("Error! Type `0` or `1` for save result to file.")


class InvalidValueOfLoopIterationsError(Exception):
    pass


class InvalidValueOfStartEndError(Exception):
    pass


class InvalidValueOfStepError(Exception):
    pass

