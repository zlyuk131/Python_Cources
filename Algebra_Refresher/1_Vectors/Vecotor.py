import math
class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimention = len(coordinates)
        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be iterable')
    
    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)
    
    #define copare function to compare two vector instances
    def __eq__(self, v):
        return self.coordinates == v.coordinates
    #define addition operation on verctors
    def checkLenght(self):
        return len(self.coordinates)
        
    def applyOperator(*arg):
        self = arg[0]
        v = arg[3]
        operator = arg[2]
        returnVector = [] 
        if operator == "+" or operator == "-":

            if self.dimention == v.dimention:
                for i in range(self.dimention):
                    returnVector.append((self.coordinates[i]) + (v.coordinates[i]))
                return returnVector
            else:
                print ('Can not add vectors of different length.')
        else:
            for i in range(self.dimention):
                returnVector.append(self.coordinates[i] * v)
            return returnVector

    def __add__(self, v):
        returnVector = []     
        if self.dimention == v.dimention:
            for i in range(self.dimention):
                returnVector.append((self.coordinates[i]) + (v.coordinates[i]))
            return Vector([returnVector[0], returnVector[1]])
        else:
            print ('Can not add vectors of different length.')

    def __sub__(self, v):
        returnVector = []     
        if self.dimention == v.dimention:
            for i in range(self.dimention):
                returnVector.append((self.coordinates[i]) - (v.coordinates[i]))
            return Vector([returnVector[0], returnVector[1]])
        else:
            print ('Can not add vectors of different length.')

    def __mul__(self, multiplier):
        returnVector = []     
        for i in range(self.dimention):
            if isinstance(multiplier, Vector):
                if self.dimention != multiplier.dimention:
                    print ('Can not add vectors of different length.')
                #print 'Multiplier is list: {}'.format(multiplier)
                returnVector.append(self.coordinates[i] * multiplier.coordinates[i])
            else:     
                #print 'Multiplier is number: {}'.format(multiplier)
                returnVector.append(self.coordinates[i] * multiplier)

        return Vector(returnVector)            
    
    def getMagnitude(self):
        vectorCoordinatesSumSqur = [x**2 for x in self.coordinates]
        self.magnitude = round(math.sqrt(sum(vectorCoordinatesSumSqur)), 4)
        print ('Calculte and set "magnitude" prop of the vector: {}').format(self.magnitude)
        return self.magnitude

    def normalize(self):
        vectorDirectionArr = []
        #if magnitude property does not exist
        if not hasattr(self, 'magnitude'):
            print ("Calculating vector magnitude: {}").format(self.getMagnitude())

        for i in range(self.dimention):
            print ("magnitude: {}").format(self.magnitude)
            vectorDirectionArr.append(round((self.coordinates[i])/self.magnitude, 3))

        return vectorDirectionArr
    
    def innerProd(self, v):
        prodVector = self * v
        return sum(prodVector.coordinates)


my_vector1 = Vector([1, 2])
my_vectorT1 = Vector([3, 4])

my_vector2 = Vector([5.581, -2.136])

my_vector3 = Vector([7.119,8.215])
my_vector4 = Vector([-8.223,0.878])

my_vector5 = Vector([8.813,-1.331,-6.247])
my_vector6 = Vector([1.996,3.108,-4.554])


#print my_vector1 + my_vector2 
#print my_vector3 - my_vector4 
#print my_vector5 * 7.41
print (my_vector1 * my_vectorT1)
print (my_vector1.innerProd(my_vectorT1))
print (math.acos(0.20))
#print my_vector1.getVectorMagnitude()

#print my_vector5.getVectorMagnitude()
#print "vector 1 magnitude is: "
#print my_vector1.getMagnitude()
#print my_vector6.getVectorMagnitude()
#my_vector2.getVectorMagnitude()
#print my_vector2.normalize()
#print my_vector6.normalize()
print (math.acos(5 / (math.sqrt(6) * math.sqrt(10))))