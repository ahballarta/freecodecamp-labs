def number_pattern(n):
    result=[]
    if not isinstance(n, int):
        return f'Argument must be an integer value.'
    if n<1:
        return f'Argument must be an integer greater than 0.'
    for number in range(1,n+1):
        result.append(str(number))
    return " ".join(result)

print(number_pattern(5))
