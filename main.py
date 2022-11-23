import src.task as task

try:
    start, end, step, loop_iterations = task.ask_values()
    task.validate_values(start, end, step, loop_iterations)

    task.print_to_console(start, end, step, loop_iterations)

    if task.ask_save_result_to_file():
        task.save_to_file(start, end, step, loop_iterations)
except ValueError as error:
    print(error)

