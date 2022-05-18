from functools import wraps

def greeter(func):
    def aloha():
        name = func()
        welcome_text = f"Aloha {name.title()}"
        return welcome_text
    return aloha

def sums_of_str_elements_are_equal(func):
    def numbers_sum():
        def digits_sum(number):
            if number[0] == "-":
                negative = True
                number = number[1:]
            else:
                negative = False

            calculated_sum = sum(int(digit) for digit in number)

            return -1 * calculated_sum if negative else calculated_sum

        numbers = func().split()

        first_sum = digits_sum(numbers[0])
        second_sum = digits_sum(numbers[1])

        sign = "==" if first_sum ==  second_sum else "!="

        return f"{first_sum} {sign} {second_sum}"

    return numbers_sum


def format_output(*required_keys):
    def make_dict(func):
        def wrapper(*args, **kwargs):
            dictionary_to_convert = func(*args, **kwargs)
            dictionary_keys = {}

            for key in required_keys:
                new_keys = key.split("__")

                for x in new_keys:
                    if x not in dictionary_to_convert.keys():
                        raise ValueError
                    dictionary_value = dictionary_to_convert[x]
                    dictionary_keys[x] = dictionary_value if len(dictionary_value)>0 else "Empty value"

            return dictionary_to_convert
        return wrapper
    return make_dict


def add_method_to_instance(klass):
    def outer_wrapper(callable):
        def wrapper():
            return callable()

        setattr(klass, callable.__name__, wrapper)

        return wrapper
    return outer_wrapper


