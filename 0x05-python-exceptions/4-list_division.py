#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """
        Divides element by element 2 lists

        Args:
            my_list_1: Dividend list
            my_list_2: Divisor list
            list_length: Length of new list

        Return:
            Quotient list
    """
    list = []
    for i in range(list_length):
        try:
            q = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            q = 0
            print("division by 0")
        except TypeError:
            q = 0
            print("wrong type")
        except IndexError:
            q = 0
            print("out of range")
        except BaseException:
            q = 0
        finally:
            list.append(q)
    return list
