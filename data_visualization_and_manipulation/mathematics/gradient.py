import numpy as np

def gradient_descent(x, y, learning_rate=0.01, epochs=1000):
    # 1. Initialize parameters (slope 'm' and intercept 'b')
    m = 0
    b = 0
    n = len(x)
    
    for i in range(epochs):
        # 2. Calculate the prediction (y = mx + b)
        y_predicted = m * x + b
        
        # 3. Calculate the cost (Mean Squared Error) - optional for tracking
        MSE = (1/n) * sum([val**2 for val in (y - y_predicted)])
        
        # 4. Calculate gradients (derivatives)
        # loss_slope_m = derivative of MSE with respect to m
        # loss_slope_b = derivative of MSE with respect to b
        loss_slope_m = -(2/n) * sum(x * (y - y_predicted))
        loss_slope_b = -(2/n) * sum(y - y_predicted)
        
        # 5. Update parameters
        m = m - learning_rate * loss_slope_m
        b = b - learning_rate * loss_slope_b
        
        if i % 100 == 0:
            print(f"Iteration {i}: loss_function {MSE:.4f}, m {m:.4f}, b {b:.4f}")
            
    return m, b

# Sample Data
x = np.array([1, 2, 3, 4, 5])
y = np.array([5, 7, 9, 11, 13]) # y = 2x + 3

m, b = gradient_descent(x, y)
print(f"\nFinal Result: y = {m:.2f}x + {b:.2f}")