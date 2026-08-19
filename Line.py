# ------------Matplotlib Line-----------

'''
Linestyle
You can use the keyword argument linestyle, or shorter ls, to change the style of the plotted line:
'''
# Use a dotted line:
# import numpy as np 
# import matplotlib.pyplot as plt 
# ypoints = np.array([3,8,1,10])
# plt.plot(ypoints, ls='dotted')
# plt.show()
# Use a dashed line:
# plt.plot(ypoints , ls="dashed")
# plt.show()
# dotted can be written as :.
# dashed can be written as --.
# plt.plot(ypoints , ls=':')
# plt.plot(ypoints, linestyle='--')
# plt.show()

'''
Line Styles
You can choose any of these styles:
Style	Or
'solid' (default)	'-'	
'dotted'	':'	
'dashed'	'--'	
'dashdot'	'-.'	
'None'	'' or ' '
'''

'''
Line Color
You can use the keyword argument color or the shorter c to set the color of the line:
'''
# Set the line color to red:
# import numpy as np 
# import matplotlib.pyplot as plt
# ypoints = np.array([3,6,2,10])
# plt.plot(ypoints , color='r')
# You can also use Hexadecimal color values:
# plt.plot(ypoints, c = '#4CAF50')
# Or any of the 140 supported color names.
# plt.plot(ypoints, c = 'hotpink')
# plt.show()

'''
Line Width
You can use the keyword argument linewidth or the shorter lw to change the width of the line.
The value is a floating number, in points:
'''
# Plot with a 20.5pt wide line:
# import numpy as np 
# import matplotlib.pyplot as plt 
# ypoints = np.array([3,4,8,1,10,4,8,9])
# plt.plot(ypoints , lw = 20.5)
# plt.show()

'''
Multiple Lines
You can plot as many lines as you like by simply adding more plt.plot() functions:
'''
# import numpy as np
# import matplotlib.pyplot as plt 
# y1 = np.array([3,8,1,10])
# y2 = np.array([6, 2, 7, 11])

# plt.plot(y1)
# plt.plot(y2)

# plt.show()

'''
You can also plot many lines by adding the points for the x- and y-axis for each line in the same plt.plot() function.

(In the examples above we only specified the points on the y-axis, meaning that the points on the x-axis got the the default values (0, 1, 2, 3).)

The x- and y- values come in pairs:
'''
# Draw two lines by specifiyng the x- and y-point values for both lines:
# import numpy as np
# import matplotlib.pyplot as plt 
# x1 = np.array([0, 1, 2, 3])
# y1 = np.array([3, 8, 1, 10])
# x2 = np.array([0, 1, 2, 3])
# y2 = np.array([6, 2, 7, 11])
# plt.plot(x1,y1,x2,y2)
# plt.show()

# --------matplotlib line lesson completed----------
