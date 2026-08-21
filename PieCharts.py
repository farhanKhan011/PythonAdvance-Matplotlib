# ----------Matplotlib Pie Charts----------

'''
Creating Pie Charts
With Pyplot, you can use the pie() function to draw pie charts:
'''
# A simple pie chart:
# import numpy as np 
# import matplotlib.pyplot as plt
# y = np.array([35,25,25,15])
# plt.pie(y)
# plt.show()

'''
after running in the output 
As you can see the pie chart draws one piece (called a wedge) for each value in the array (in this case [35, 25, 25, 15]).
By default the plotting of the first wedge starts from the x-axis and moves counterclockwise:
'''
# Note: The size of each wedge is determined by comparing the value with all the other values, by using this formula:
# The value divided by the sum of all values: x/sum(x)

'''
Labels
Add labels to the pie chart with the labels parameter.
The labels parameter must be an array with one label for each wedge:
'''
# A simple pie chart:
# import numpy as np 
# import matplotlib.pyplot as plt 

# x = np.array([35,25,25,15])
# myLabel = ['Apples','Grapes','Bananas','Melon']
# plt.pie(x , labels = myLabel )
# plt.show()

'''
Start Angle
As mentioned the default start angle is at the x-axis, but you can change the start angle by specifying a startangle parameter.
The startangle parameter is defined with an angle in degrees, default angle is 0:
'''
# import numpy as np 
# import matplotlib.pyplot as plt 
# x = np.array([35,25,25,15])
# myLabels = ["Views",'Likes','Comments','shairs']
# plt.pie(x , labels = myLabels , startangle=90)
# plt.show()

'''
Explode
Maybe you want one of the wedges to stand out? The explode parameter allows you to do that.
The explode parameter, if specified, and not None, must be an array with one value for each wedge.
Each value represents how far from the center each wedge is displayed:
'''
# Pull the "Apples" wedge 0.2 from the center of the pie:
# import numpy as np 
# import matplotlib.pyplot as plt 
# x = np.array([35,25,25,15])
# myLabels = ["Keyboard","Mouse","Speaker","Mic"]
# myExplode = [0 , 0 ,  0 , 0.5 ]
 # Add a shadow to the pie chart by setting the shadows parameter to True:
# plt.pie(x , labels = myLabels , explode = myExplode , shadow = True)
# plt.show() 

'''
Colors
You can set the color of each wedge with the colors parameter.
The colors parameter, if specified, must be an array with one value for each wedge:
'''
# import numpy as np 
# import matplotlib.pyplot as plt 
# y = np.array([40,25,25,10])
# myLabels = ["Pencils" , "Erasers" , "Sharpner" , "Bags"]
# myExplods = [0,0.3,0,0]
# myColors = ['red','hotpink','brown','black']

# plt.pie(y ,startangle=90, labels=myLabels , explode=myExplods , shadow=True , colors=myColors)
# plt.show()

'''
You can use Hexadecimal color values, any of the 140 supported color names, or one of these shortcuts:

'r' - Red
'g' - Green
'b' - Blue
'c' - Cyan
'm' - Magenta
'y' - Yellow
'k' - Black
'w' - White
'''

'''
Legend
To add a list of explanation for each wedge, use the legend() function:
'''
# import numpy as np 
# import matplotlib.pyplot as plt 
# x = np.array([35,25,25,15])
# myLabels = ["Apples" , "Bananas" , "Cherries" , "Mango"]

# plt.pie(x , labels = myLabels )
# To add a header to the legend, add the title parameter to the legend function.
# plt.legend(title = "Fruits list")
# plt.show()

# ---------Matplotlib Pie Charts lesson completed------------