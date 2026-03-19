from time import sleep, time  
from functools import wraps

def measure (func):
    @wraps(func)
    def wrapper (*args, **kwargs):
        t = time()
        r = func(*args, **kwargs)
        t2 = time()
        print(func.__name__, "took {} seconds".format(t2 - t))
        return r 
    
    return wrapper

def max_allowed_result(threshold):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            r = func(*args, **kwargs)
            if r > threshold: 
                print("result ({}) is bigger than allowed. Allowed is {}"
                    .format(r, threshold))
                return None 
            else:
                return r
        return wrapper
    return decorator

@measure
@max_allowed_result(120)
def slowly_multiply(x, y):
    r = x * y 
    sleep(0.3)
    return r

print(slowly_multiply(2, 11))

class Vehicle():
    def __init__(self, n_wheels, n_weight, n_current_speed):
        self.n_wheels = n_wheels
        self.n_weight = n_weight
        self.n_current_speed = n_current_speed

    def accelerate(self, by_Speed): 
        raise NotImplementedError 

    def deccelerate(self, by_Speed): 
        raise NotImplementedError

class Car(Vehicle):
    def __init__ (self, n_weight, n_doors, n_current_speed, n_wheels=4):
        super().__init__(n_wheels, n_weight, n_current_speed)
        self.n_doors = n_doors

    def accelerate(self, by_Speed):
        self.n_current_speed += by_Speed
        

myCar = Car(2500, 4, 25.5)


        

    

        

