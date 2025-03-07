#Andrew Chambers Assignment 3a

#Euler Function(equation)
def EulerFunc(t,y) :
    res = t - y**2
    return res

#Euler method
def EulerMethod():
    t_max = 2
    Iterations = 10
    t = 0
    y = 1
    h = t_max / Iterations

   
    while t < t_max - .005: #Note the -.005 is here due to a python rounding error
        y = y + h*EulerFunc(t,y)
        t += h
       
    return y

# Runge-Kutta Function(a Euler but incase the equation was different for the given problems)
def RungeFunc(t,y):
    res = t - y**2
    return res

# RungeKutta method
def RungeKutta():
    t_max = 2
    Iterations = 10
    h = t_max / Iterations
    t = 0
    y = 1

    while t < t_max - .005: #Note the -.005 is here due to a python rounding error
       
        kOne = h * RungeFunc(t,y)
        kTwo = h * RungeFunc(t+(h/2),y+(1/2)*kOne)
        kThree = h* RungeFunc(t+(h/2),y+(1/2)*kTwo)
        kFour = h*RungeFunc(t+h,y+kThree)
        y = y + (1/6)*(kOne + 2*kTwo+ 2*kThree + kFour)
        t+= h
     
    return y

def main():
    #Run our Euler method
    EulerAnswer = EulerMethod()
    print(EulerAnswer)
   
    #Space out the answers
    print("")
   
    #Run our Runge Kutta Method
    RungeAnswer = RungeKutta()
    print(RungeAnswer)

#Run our program.
if __name__ == "__main__":
    main()
