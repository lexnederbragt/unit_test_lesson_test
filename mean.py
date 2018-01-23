def mean(num_list):
    """Returns the mean for a list of numbers"""
    try:
        mean = sum(num_list)/float(len(num_list))
        if isinstance(mean, complex):
            return NotImplemented
        return mean
    except ZeroDivisionError as detail :
        msg = "The algebraic mean of an empty list is undefined."
        msg += "Please provide a list of numbers."
        raise ZeroDivisionError(detail.__str__() + "\n" +  msg)
    except TypeError as detail :
        msg = "The algebraic mean of an non-numerical list is undefined."
        msg += "Please provide a list of numbers."
        raise TypeError(detail.__str__() + "\n" +  msg)
