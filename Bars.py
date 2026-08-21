# -----------Matplotlib Bars----------

'''
Creating Bars
With Pyplot, you can use the bar() function to draw bar graphs:
'''
# Draw 4 bars:
# import numpy as np 
# import matplotlib.pyplot as plt 
# x = np.array(['A','B','C','D'])
# y = np.array([3,8,1,10])

# plt.bar(x,y)
# plt.show()
'''
The bar() function takes arguments that describes the layout of the bars.
The categories and their values represented by the first and second argument as arrays.
'''
# import numpy as np 
# import matplotlib.pyplot as plt 
# x = np.array(['Apples','Bananas'])
# y = np.array([450,380])
# plt.bar(x,y)
# plt.show()

'''
Horizontal Bars
If you want the bars to be displayed horizontally instead of vertically, use the barh() function:
'''
# Draw 4 horizontal bars:
# import numpy as np 
# import matplotlib.pyplot as plt 
# x = np.array(['A','B','C','D'])
# y = np.array([12,56,76,98])

# plt.barh(x,y)
# plt.show()

'''
Bar Color
The bar() and barh() take the keyword argument color to set the color of the bars:
'''
# Draw 4 red bars:
# import numpy as np 
# import matplotlib.pyplot as plt 
# x = np.array(['A','B','C','D'])
# y = np.array([12,56,76,98])

# plt.barh(x,y, color = "red")
# plt.bar(x,y, color = "red")
# plt.show()

'''
Color Names
You can use any of the 140 supported color names.
'''
# Draw 4 "hot pink" bars:
# import matplotlib.pyplot as plt
# import numpy as np

# x = np.array(["A", "B", "C", "D"])
# y = np.array([3, 8, 1, 10])

# plt.bar(x, y, color = "hotpink")
# plt.show()

'''
Draw 4 bars with a beautiful green color:
'''
# import matplotlib.pyplot as plt
# import numpy as np

# x = np.array(["A", "B", "C", "D"])
# y = np.array([3, 8, 1, 10])

# plt.bar(x, y, color = "#00F99E")
# plt.show()

'''
Bar Width
The bar() takes the keyword argument width to set the width of the bars:
'''
# Draw 4 very thin bars:
# import matplotlib.pyplot as plt
# import numpy as np

# x = np.array(["A", "B", "C", "D"])
# y = np.array([3, 8, 1, 10])

# plt.bar(x,y , width = 0.1  )
# plt.show()

'''
The default width value is 0.8
Note: For horizontal bars, use height instead of width.
'''
# The barh() takes the keyword argument height to set the height of the bars:
# Draw a 4 very thin bar 
# import matplotlib.pyplot as plt
# import numpy as np

# x = np.array(["A", "B", "C", "D"])
# y = np.array([3, 8, 1, 10])

# plt.barh(x, y, height = 0.1)
# plt.show()

# --------Matplotlib Bars lesson Completed-------
