import pytest
from lib.todo import *

"""
Given an instance of the class with a task
#__init__ Sets the task property and the complete property to False  (no return)
"""
def test_if_sets_init_variables():
    todo = Todo('Complete upper body day 1 weightlifting program today')
    result = f"The task property is: '{todo.task}'. The complete property is: '{todo.complete}'."
    assert result == "The task property is: 'Complete upper body day 1 weightlifting program today'. The complete property is: 'False'."


"""
Given an instance of the class with a task
#mark_complete Sets the task property and the complete property to False  (no return)
"""
def test_if_marks_complete():
    todo = Todo('Complete upper body day 1 weightlifting program today')
    todo.mark_complete()
    result = todo.complete
    assert result == True