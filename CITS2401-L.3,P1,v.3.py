import numpy as np
import matplotlib.pyplot as plt


def microcar(x,y):
    
    ex_hor_disp = np.array([])
    ex_vert_disp = np.array([])
    
    act_hor_disp = np.array([])
    act_vert_disp = np.array([])
    
    ex_dist = np.array([])
    act_dist = np.array([])
    
    
    for i in range(len(x)):
        with open(x[i],'r') as ex_inputfile:
            #This is us declaring and initalising variables in a local scope to reset for each car
            vert_displacement = 0
            hor_displacement = 0
            #This is us defining our measurements of displacement and distance
            ex_distance = 0
            act_distance = 0
            
            
            
            for line in ex_inputfile:
                instruction = line.split(',')
                instruction[2] = instruction[2].strip()
                
                
                
            
                #This is just looking at the instructed/expected displacement over time
                if instruction[0] == 'N':
                    vert_displacement += (int(instruction[1])*int(instruction[2]))
                    
                elif instruction[0] == 'S':
                    vert_displacement -= (int(instruction[1])*int(instruction[2]))
                    
                elif instruction[0] == 'E':
                    hor_displacement += (int(instruction[1])*int(instruction[2]))
                    
                else:
                    hor_displacement -= (int(instruction[1])*int(instruction[2]))
                
                ex_distance += (int(instruction[1])*int(instruction[2]))
            
            #This is used to add the final expected displacements to the array
            ex_hor_disp = np.append(ex_hor_disp,hor_displacement)
            ex_vert_disp = np.append(ex_vert_disp,vert_displacement)
            
            #Likewise, this is used to add the final expected distance travelled to the array
            ex_dist = np.append(ex_dist,ex_distance)
            


        with open (y[i],'r') as act_inputfile:
            #This is again just us declaring and initalising variables on a local scale for each car
            vert_displacement = 0
            hor_displacement = 0
            
            for line in act_inputfile:
                action = line.split(',')
                action[2] = action[2].strip()
                print(action)
                
                
                
                #This is just looking at the actual displacement over time
                if action[0] == 'N':
                    vert_displacement += (int(action[1])*int(action[2]))
                    
                elif action[0] == 'S':
                    vert_displacement -= (int(action[1])*int(action[2]))
                    
                elif action[0] == 'E':
                    hor_displacement += (int(action[1])*int(action[2]))
                    
                else:
                    hor_displacement -= (int(action[1])*int(action[2]))
                
                act_distance += (int(action[1])*int(action[2]))
                
            #This is used to add the final expected displacements to the array
            act_hor_disp = np.append(act_hor_disp,hor_displacement)
            act_vert_disp = np.append(act_vert_disp,vert_displacement)
            
            #Likewise, this is used to add the final expected distance travelled to the array
            act_dist = np.append(act_dist,act_distance)
            
    return ex_hor_disp, ex_vert_disp, act_hor_disp, act_vert_disp, ex_dist, act_dist


def plotmicrocar(x,y):
    
    
    #setting each array equal to the returned arrays from the microcar function
    ex_hor_disp, ex_vert_disp, act_hor_disp, act_vert_disp, ex_dist, act_dist =  microcar(x,y)
    
    #And now, we start to plot
    
    #This is the top graph, showing expected vs actual distances covered by each car
    
    #This is just declaring that it's a subplot, but the problem is, how do we adjust the size of the top plot so it takes up the whole top row?
    
    #This problem is fixed by the fact that you don't have to have consistent row and column numbers for each subplot, just that the ordering makes sense.
    plt.subplot(2,1,1)
    
    
    '''Really, this whole part is just taken from an online source, at least the width adjustment part is'''
    #This is getting the x position of each bar, for the expected distances
    x1 = np.arange(len(ex_dist))
    
    #This is getting the x positions of each bar, for the actual distances
    x2 = [x + 0.2 for x in x1]
    
    #This is actually plotting each one now
    
    #Plot the expected distances for each car
    plt.bar(x1, ex_dist, width = 0.2, color = 'blue', label = 'Exp')
    
    #Plot the actual distances for each car
    plt.bar(x2, act_dist, width = 0.2, color = 'black',  label = 'Act')
    
    #general layout
    plt.xlabel('mvcar')
    plt.ylabel('Dist')
    
    #So usually the tick would appear in the middle of the left bar if we just had x1, but we want it in the middle, so we use x1+0.1, which is half the width of the bar.
    plt.xticks(x1 + 0.1, x1)
    plt.legend()
    plt.title("Distance")
    
    plt.tight_layout()
  
    
    
    
    #This is the bottom left subplot
    miv_legend_array = []
    for i in range(len(ex_hor_disp)):
        miv_legend_array.append("mivcar "+str(i))
        
    print(miv_legend_array)
    
    #Currently, we can see that this whole 'ax' shebang works, but we're not sure why
    ax = plt.subplot(2,2,3)
    ax.set_xmargin(1)
    ax.set_ymargin(1)
    for i in range(len(ex_hor_disp)):
        plt.scatter([ex_hor_disp[i]],[ex_vert_disp[i]], marker = 'o', c = np.random.rand(3,) )
        plt.xlabel = "Horizontal Displacement"
        plt.ylabel = "Vertical Displacement"
    plt.title('E')
    plt.legend([x for x in miv_legend_array])
    
    #This is the bottom right subplot
        
    #This just generates the suff for the legend
    car_legend_array = []
    for i in range(len(ex_hor_disp)):
        car_legend_array.append("Car "+str(i))
        
    print(car_legend_array)
        
    ax = plt.subplot(2,2,4)
    ax.set_xmargin(1)
    ax.set_ymargin(1)
    for i in range(len(ex_hor_disp)):
        ax.scatter([act_hor_disp[i]],[act_vert_disp[i]], marker = 'x', c = np.random.rand(3,))
        ax.xlabel = "Horizontal Displacement"
        ax.ylabel = "Vertical Displacement"
        
    plt.title('Actual')
    ax.legend([x for x in car_legend_array])
    plt.show()
    

            
        
        

    
 
    
    
