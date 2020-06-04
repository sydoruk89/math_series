def fibonacci(n):
    """
    The function return the nth value in the fibonacci series.

    Args:
        n (int): integer
    """
    if n >= 0:
        if n < 2:
            return n
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)
    else:
        return 'Please provide a positive number'

  
def lucas(n):
    """
    The function return the nth value in the lucas series.

    Args:
        n (int): integer
    """
    if n >= 0:
        if n == 0:
            return 2
        elif n == 1:
            return n
        else:
            return lucas(n - 1) + lucas(n - 2)
    else:
        return 'Please provide a positive number'

    
def sum_series(n, prev = 0, next = 1):
    """
    Calling this function with no optional parameters will produce numbers from the fibonacci series.

    Args:
        n (int): integer
        prev (int, optional): [description]. Defaults to 0.
        next (int, optional): [description]. Defaults to 1.
    """
    if n >= 0 and prev >= 0 and next >= 0:
        for i in range(n):
            prev, next = next, prev + next
        return prev
    else:
        return 'Please provide a positive number'


