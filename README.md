# function-plotter
A GUI programme that plots arbitrary user-entered functions (Polynomials in One Variable).
made as one of the summer training Qualification tasks of [Master Micro](https://www.master-micro.com/).
Requirements 
1. Write a GUI programme that plots arbitrary user-entered functions. 
2. Take a function of x from the user, e.g., 5*x^3 + 2*x.
3. Take min and max values of x from the user.
4. The following operators must be supported: + - / * ^.
5. The GUI should be simple and beautiful (well organized).
6. Apply appropriate input validation to the user's input.
7. Display messages to the user to explain any wrong input.
8. You may use programming language and platform of your choice.
9. Your code should be well organised and well documented.
The application has three main inputs: function, min, and max.

![image](https://user-images.githubusercontent.com/58492759/168443368-34649980-066d-415e-8453-4ed082fb670c.png)

the input must be at the form (number * x ^ powre) e.g, 5*x^3+8 not 5x^3+8

![image](https://user-images.githubusercontent.com/58492759/168443444-8576059c-3ec4-4c0b-8643-a10305002be3.png)

In the case of negative power and range from negative to positive, the point at x=0 is undefined, so it's replaced with a very small value that approaches zero.

![image](https://user-images.githubusercontent.com/58492759/168443486-eb969f88-39d8-4bbc-a655-69d329fa24ce.png)
