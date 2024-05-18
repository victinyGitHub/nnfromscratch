import numpy as np
import functions as f

class Module():
    def __init__(self) -> None:
        pass

    def __call__():
        pass
    
    def backward():
        pass
    
class Linear(Module):

    def __init__(self, d1, d2) -> None:
        self.d1 = d1
        self.d2 = d2
        self.map = np.random.rand(d1, d2) - 0.5
        self.bias = np.random.rand(d1, 1)
        self.input = None

    def __call__(self, input):
        self.input = input
        self.out = np.matmul(self.map, input)
        self.out += self.bias
        return self.out
    
    def backward(self, grad):
        backu = np.matmul(np.transpose(self.map), grad)
        
        self.d_weights = np.matmul(grad, np.transpose(self.input) )
        self.d_bias = grad

        # self.map -= lr * d_weights
        # self.bias -= lr * d_bias these should be handled in the step function
        return backu
    
class Sigmoid(Module):
    
    def __init__(self) -> None:
        super().__init__()
        self.derivative = lambda x : f.sigmoid(x) * (1 - f.sigmoid(x))

        self.elementwise_d = np.vectorize(self.derivative)

    def __call__(self, x):
        self.input = x
        return np.vectorize(f.sigmoid(x))

    def backward(self, grad):
        return np.multiply(self.elementwise_d(self.input), grad)
    
class Logistics(Module):
# how are you going to pass in the y's
    def __call__(self, t, y): 
        self.input = (t, y)
        self.t, self.y = t, y
        return y * np.log(1 + np.exp(-t)) + (1 - y) * np.log(1 + np.exp(t))

    def backward(self, grad):
        v = self.input
        return (f.sigmoid(self.t) - self.y) * grad
    
class Model(Module):

    def __init__(self, layers = []):
        self.layers = layers
        
    def __call__(self, x_in):
        x = x_in
        for layer in self.layers:
            x = layer(x)
    
    def append(self, layer):
        self.layers.append(layer)

    def backward(self):
        

