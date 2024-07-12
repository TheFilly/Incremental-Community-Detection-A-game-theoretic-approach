
"""
Checks for convergence of a value
Input: The value, past_values, threshold, the tolerance parameter and minimal iterations
Output: Boolean of convergence
"""


def checkConvergence(value, past_values, threshhold, tolerance, min_iterations):
    if len(past_values) <= min_iterations:
        past_values.append(value)
        return False
    else:
        past_values.append(value)
        if len(past_values) > min_iterations:
            past_values.pop(0)
        avg = sum(past_values) / len(past_values)
        if abs(value) > threshhold and abs(value - avg) < tolerance:
            return True
        else:
            return False
