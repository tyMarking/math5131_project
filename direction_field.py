import numpy as np
import matplotlib.pyplot as plt

# A = 100
A = 140
ALPHA = 10000
# BETA = 70
BETA = 50
C = 3e-10
D = 0.01

SpeciesX = "Satelites"
SpeciesY = "Debris Fragments"

def plot_direction_filed(dx_func, dy_func, x_range, y_range, x_ticks=40, y_ticks=40, ):
    x = np.linspace(x_range[0], x_range[1], x_ticks)
    y = np.linspace(y_range[0], y_range[1], y_ticks)
    # print(type(x))
    # print(y)
    X, Y = np.meshgrid(x,y)
    
    # print(type(X))
    # print(X.shape)
    # print(Y)
    dx = dx_func(X,Y)/x_range[1]
    dy = dy_func(X,Y)/y_range[1]
    dxu = dx/np.sqrt(dx**2+dy**2)
    dyu = dy/np.sqrt(dx**2+dy**2)
    print(dxu)
    print(dyu)
    plt.quiver(X,Y, dxu, dyu, color='purple')
    plt.scatter(x=3e3,y=700000, s=200, c="r", marker='x')
    plt.title("Direction Field")
    plt.xlabel(SpeciesX)
    plt.ylabel(SpeciesY)
    plt.show()


def dx1(X,Y):
    return A-(C*X*Y)
def dy1(X,Y):    
    return (BETA*A) -(D*Y) + (ALPHA*C*X*Y)

# def dx1(X,Y):
#     return np.ones(X.shape)
# def dy1(X,Y):    
#     return X**2-Y

def main():
    # plot_direction_filed(dx1, dy1, (-4,5), (-4,5), )
    plot_direction_filed(dx1, dy1, (0,7000), (0,1000000000), )

if __name__ == "__main__":
    main()