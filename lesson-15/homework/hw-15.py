################################# Task -1 ########################################
## 1. Basic Plotting
# import matplotlib.pyplot as plt
# import numpy as np
# def f(x):
#     return x**2 - 4*x + 4
# x = np.linspace(-10, 10, 400)
# y = f(x)
# plt.figure(figsize=(8, 6))
# plt.plot(x, y, label='$f(x) = x^2 - 4x + 4$', color='blue')
# plt.xlabel('x')
# plt.ylabel('f(x)')
# plt.title('Plot of the function $f(x) = x^2 - 4x + 4$')
# plt.grid(True)
# plt.axhline(0, color='black', linewidth=0.5)
# plt.axvline(0, color='black', linewidth=0.5)
# plt.legend()
# plt.show()
################################# Task -2 ########################################
## 2. Sine and Cosine Plot
# import numpy as np
# import matplotlib.pyplot as plt
# x = np.linspace(0, 2 * np.pi, 400)
# y_sin = np.sin(x)
# y_cos = np.cos(x)
# plt.figure(figsize=(8, 6))
# plt.plot(x, y_sin, label='sin(x)', color='blue', linestyle='--', marker='o', markersize=4)
# plt.plot(x, y_cos, label='cos(x)', color='red', linestyle='-', marker='s', markersize=4)
# plt.title('Plot of sin(x) and cos(x)')
# plt.xlabel('x (radians)')
# plt.ylabel('Function value')
# plt.legend()
# plt.grid(True)
# plt.axhline(0, color='black', linewidth=0.5)
# plt.show()
################################# Task -3 ########################################
## 3. Subplots
# import numpy as np
# import matplotlib.pyplot as plt
# x1 = np.linspace(-10, 10, 400)       # For x^3
# x2 = np.linspace(-2 * np.pi, 2 * np.pi, 400)  # For sin(x)
# x3 = np.linspace(-2, 2, 400)         # For exp(x)
# x4 = np.linspace(0, 10, 400)         # For log(x + 1)
# fig, axs = plt.subplots(2, 2, figsize=(12, 10))
# axs[0, 0].plot(x1, x1**3, color='purple')
# axs[0, 0].set_title('f(x) = x³')
# axs[0, 0].set_xlabel('x')
# axs[0, 0].set_ylabel('f(x)')
# axs[0, 0].grid(True)
# axs[0, 1].plot(x2, np.sin(x2), color='blue')
# axs[0, 1].set_title('f(x) = sin(x)')
# axs[0, 1].set_xlabel('x')
# axs[0, 1].set_ylabel('f(x)')
# axs[0, 1].grid(True)
# axs[1, 0].plot(x3, np.exp(x3), color='green')
# axs[1, 0].set_title('f(x) = eˣ')
# axs[1, 0].set_xlabel('x')
# axs[1, 0].set_ylabel('f(x)')
# axs[1, 0].grid(True)
# axs[1, 1].plot(x4, np.log(x4 + 1), color='orange')
# axs[1, 1].set_title('f(x) = log(x + 1)')
# axs[1, 1].set_xlabel('x')
# axs[1, 1].set_ylabel('f(x)')
# axs[1, 1].grid(True)
# plt.tight_layout()
# plt.show()
################################# Task -4 ########################################
## 4. Scatter Plot
# import numpy as np
# import matplotlib.pyplot as plt
# x = np.random.uniform(0, 10, 100)
# y = np.random.uniform(0, 10, 100)
# colors = np.random.rand(100)
# markers = ['o', 's', '^', 'D', 'v']
# marker_types = [markers[i % len(markers)] for i in range(100)]
# plt.figure(figsize=(8, 6))
# for i in range(100):
#     plt.scatter(x[i], y[i], color=plt.cm.viridis(colors[i]), marker=marker_types[i], edgecolors='black')
# plt.title('Scatter Plot of 100 Random Points')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.grid(True)
# plt.show()
################################# Task -5 ########################################
## 5. Histogram
# import numpy as np
# import matplotlib.pyplot as plt
# data = np.random.normal(loc=0, scale=1, size=1000)
# plt.figure(figsize=(8, 6))
# plt.hist(data, bins=30, color='skyblue', edgecolor='black', alpha=0.7)
# plt.title('Histogram of Normally Distributed Data (μ=0, σ=1)')
# plt.xlabel('Value')
# plt.ylabel('Frequency')
# plt.grid(True)
# plt.show()
################################# Task -6 ########################################
## 6. 3D Plotting
# import numpy as np
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
# x = np.linspace(-5, 5, 100)
# y = np.linspace(-5, 5, 100)
# X, Y = np.meshgrid(x, y)
# Z = np.cos(X**2 + Y**2)
# fig = plt.figure(figsize=(10, 8))
# ax = fig.add_subplot(111, projection='3d')
# surf = ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none')
# fig.colorbar(surf, shrink=0.5, aspect=10)
# ax.set_title('3D Surface Plot of $f(x, y) = \cos(x^2 + y^2)$')
# ax.set_xlabel('x')
# ax.set_ylabel('y')
# ax.set_zlabel('f(x, y)')
# plt.show()
################################# Task -7 ########################################    
## 7. Bar Chart
# import matplotlib.pyplot as plt
# products = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
# sales = [200, 150, 250, 175, 225]
# colors = ['dodgerblue', 'crimson', 'mediumseagreen', 'goldenrod', 'orchid']
# plt.figure(figsize=(8, 6))
# bars = plt.bar(products, sales, color=colors)
# plt.title('Sales Data for Different Products')
# plt.xlabel('Product')
# plt.ylabel('Sales')
# plt.grid(axis='y', linestyle='--', alpha=0.6)
# for bar in bars:
#     yval = bar.get_height()
#     plt.text(bar.get_x() + bar.get_width()/2.0, yval + 5, f'{yval}', ha='center', va='bottom')
# plt.tight_layout()
# plt.show()
################################# Task -8 ########################################
## 8. Stacked Bar Chart
# import matplotlib.pyplot as plt
# import numpy as np
# time_periods = ['T1', 'T2', 'T3', 'T4']
# category_a = [20, 35, 30, 35]
# category_b = [25, 32, 34, 20]
# category_c = [15, 18, 20, 25]
# x = np.arange(len(time_periods))  
# width = 0.6  
# plt.figure(figsize=(8, 6))
# bar1 = plt.bar(x, category_a, width, label='Category A', color='skyblue')
# bar2 = plt.bar(x, category_b, width, bottom=category_a, label='Category B', color='lightgreen')
# bottom_c = np.array(category_a) + np.array(category_b)
# bar3 = plt.bar(x, category_c, width, bottom=bottom_c, label='Category C', color='salmon')
# plt.title('Stacked Bar Chart of Category Contributions Over Time')
# plt.xlabel('Time Period')
# plt.ylabel('Value')
# plt.xticks(x, time_periods)
# plt.legend()
# plt.grid(axis='y', linestyle='--', alpha=0.6)
# plt.tight_layout()
# plt.show()

