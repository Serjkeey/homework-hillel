def cache_decorator(func):
    cache = {}

    def wrapper(*args, **kwargs):
        key = (args, frozenset(kwargs.items()))

        if key in cache:
            print(f'Використовується кеш для аргументів {args} та {kwargs}')
            return cache[key]

        print(f'Викликається функція {func.__name__} з аргументами {args} та {kwargs}')
        result = func(*args, **kwargs)
        cache[key] = result
        return result

    return wrapper


@cache_decorator
def triangle_area(a: float, b: float) -> float:
    print(f'Викликається функція triangle_area з аргументами {a} та {b}')
    return a * b


@cache_decorator
def circle_area(r: float) -> float:
    print(f'Викликається функція circle_area з аргументом {r}')
    return 3.14 * (r * r)


print('Результат виклику triangle_area(5, 10):', triangle_area(5, 10))
print('Результат виклику triangle_area(5, 10):', triangle_area(5, 10))
print('Результат виклику circle_area(20):', circle_area(20))
print('Результат виклику triangle_area(10, 10):', triangle_area(10, 10))
print('Результат виклику circle_area(20):', circle_area(20))
