class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates)==2:
            return True
        elif len(coordinates)>2:
            if coordinates[1][0]-coordinates[0][0]==0:
                slope = 90
            else:
                slope = (coordinates[1][1]-coordinates[0][1])/(coordinates[1][0]-coordinates[0][0])
            x,y = coordinates[0][0],coordinates[0][1]
            coordinates = coordinates[2:]
            for i in coordinates:
                if (i[0]-x)==0:
                    slp = 90
                else:
                    slp = ((i[1]-y)/(i[0]-x))
                
                if slp == slope:
                    pass
                else:
                    return False
            return True
