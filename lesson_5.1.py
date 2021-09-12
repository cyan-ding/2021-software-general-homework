"""Make a class for a robot! This robot can only drive in a straight line on a field 7 meters long. The robot has a drive base and an arm that can move up and down. Imagine that the arm can pick up and score cubes for 5 points each. Your robot should have these variables:
   Position
Arm position
Whether or not it has a cube
Score from scoring cubes
The robot class should also have methods to:
Move
Raise/lower arm
Pick up a cube
Score a cube
Rules/information:
The robot starts at position 0 with no cubes and the arm 0 inches off the ground.
A cube can only be picked up when:
The robot is at space 3 (aka 3 meters from starting position)
The arm is 0 inches off the ground
The robot does not already have a cube
The robot must be holding a cube 10 inches in the air at space 7 to score it.

Once you have this class created, make a way for the user to control the robot! Use loops and input. Every time the robot does something, make sure to print out information on its position, etc. so the user doesn’t get confused. """













class robot:
    def __init__(self, pos, arm_pos, cube, points):
      self.pos = pos

      self.arm_pos = arm_pos
      self.cube = cube
      self.points = points
    
    
    def move(self,distance ):
        self.distance = distance
        self.pos += distance
        print("The robot moves", distance, "meters and is now", self.pos, "meters from starting position.")
    
    def arm_up(self, up):
        self.up = up
        self.arm_pos += up
        print("The arm position is now", self.arm_pos, "inches from the ground")
    
    def cubecheck(self):
        
        if self.pos == 3 and self.arm_pos == 0 and self.cube == False:
            self.cube = True
            print("A cube has been picked up. ")
        else:
            print("A cube has not been picked up. ")
    def cubescore(self):
        if self.cube == True and self.arm_pos == 10 and self.pos == 7:
            self.points += 5
            print("noice you scored some points. your point total is now", self.points)
        else:
            print("no cube has been scored. ")
            
robo = robot(0,0,False, 0)    

while True:
    input1 = int(input("Input how many meters you want the robot to move: "))
    input2 = int(input("Input how many inches you want the robot arm to move upwards: "))
    input3 = bool(input("Input whether you want to pick up a cube: "))
    input4 = bool(input("Input whether you want to score a cube:  "))

    if input1 ==0:
        print("The location has not been changed")
    elif input1 < 0 and robo.pos < 0:
        print("The robot has moved backwards", input1, "meters and is now", robo.pos, "meters behind the starting position")
    else:
      robo.move(input1)
      print("The robot's location is now", robo.pos, "meters from the start")
    
    if input2 == 0:
        print("The location of the arm has not changed")
    
    elif input2 !=0:
        robo.arm_up(input2)
        print("The robot's arm is now", robo.arm_pos, "inches from the ground")
 
    
    if input3 == True: 
      robo.cubecheck()

    if input4 == True:
      robo.cubescore()
    
