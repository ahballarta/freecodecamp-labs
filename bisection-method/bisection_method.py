def square_root_bisection(square_target,tolerance=1e-5,max_iterations=50):
    if square_target < 0:
        raise ValueError('Square root of negative number is not defined in real numbers')
    if square_target == 1 or square_target == 0:
        print(f'The square root of {square_target} is {square_target}')
        return square_target
    
    if square_target>1:
        low=0
        high=square_target
    else:
        low=square_target
        high=1
    iteration_index=0
    mid = (low+high)/2
    error = (mid**2)-square_target

    if error == 0:
        print(f'The square root of {square_target} is approximately {mid}')
        return mid

    while abs(high - low) > tolerance and iteration_index<max_iterations:
        if error > 0:
            high = mid
        else:
            low = mid  
        iteration_index += 1
        mid = (low+high)/2
        error = (mid**2)-square_target
    
    if iteration_index == max_iterations and abs(high - low) > tolerance:
        print(f'Failed to converge within {max_iterations} iterations')
        return None
    else:
        print(f'The square root of {square_target} is approximately {mid}' with an error of {error} and a number of iterations of {iteration_index}')
    return mid

print(square_root_bisection(0.001, 1e-7, 50))
print(square_root_bisection(225, 1e-7, 10))
print(square_root_bisection(81, 1e-3, 50))
