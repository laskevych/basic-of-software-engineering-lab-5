import unittest
import src.task as task


class MyTestCase(unittest.TestCase):
    def test_calculate_function(self):
        values = [
            {
                "x": -5,
                "loopIterations": 5,
                "result": -100
            },
            {
                "x": 0,
                "loopIterations": 0,
                "result": 0
            },
            {
                "x": 0,
                "loopIterations": 2,
                "result": 0
            },
            {
                "x": 5,
                "loopIterations": 10,
                "result": 14.144841269841269
            },
        ]

        for value in values:
            self.assertEqual(
                task.calculate(value.get("x"), value.get("loopIterations")),
                value.get("result")
            )

    def test_validation_function_loop_iterations_equal_zero(self):
        with self.assertRaises(task.InvalidValueOfLoopIterationsError):
            task.validate_values(1, 2, 3, 0)

    def test_validation_function_start_greater_than_end(self):
        with self.assertRaises(task.InvalidValueOfStartEndError):
            task.validate_values(5, 1, 3, 5)

    def test_validation_function_step_equal_zero(self):
        with self.assertRaises(task.InvalidValueOfStepError):
            task.validate_values(-5, 5, 0, 5)


if __name__ == '__main__':
    unittest.main()
