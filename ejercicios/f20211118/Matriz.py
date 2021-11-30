class Matrix3D():

    def __init__(self, a00 = 1, a01 = 1, a02 = 1, a10 = 1, a11 = 1, a12 = 1, a20 = 1, a21 = 1, a22 = 1):
        
        self.a00 = a00
        self.a01 = a01
        self.a02 = a02
        self.a10 = a10
        self.a11 = a11
        self.a12 = a12
        self.a20 = a20
        self.a21 = a21
        self.a22 = a22
        
        self.matrix = [[self.a00, self.a01, self.a02],[self.a10, self.a11, self.a12],[self.a20, self.a21, self.a22]]
        
        

    def __add__(self, other):
        
        suma = [[self.a00 + other.a00, self.a01 + other.a01, self.a02 + other.a02],[self.a10 + other.a10, self.a11 + other.a11, self.a12 + other.a12],[self.a20 + other.a20, self.a21 + other.a21, self.a22 + other.a22]]
        
        return suma

    def __sub__(self, other):
        
        resta = [[self.a00 - other.a00, self.a01 - other.a01, self.a02 - other.a02],[self.a10 - other.a10, self.a11 - other.a11, self.a12 - other.a12],[self.a20 - other.a20, self.a21 - other.a21, self.a22 - other.a22]]
        
        return resta

    def __mul__(self, other):
        
        mult = [[self.a00*other.a00 + self.a01*other.a10 + self.a02*other.a20, self.a00*other.a01 + self.a01*other.a11 + self.a02*other.a21, self.a00*other.a02 + self.a01*other.a12 + self.a02*other.a22],[self.a10*other.a00 + self.a11*other.a10 + self.a12*other.a20, self.a10*other.a01 + self.a11*other.a11 + self.a12*other.a21, self.a10*other.a02 + self.a11*other.a12 + self.a12*other.a22],[self.a20*other.a00 + self.a21*other.a10 + self.a22*other.a20, self.a20*other.a01 + self.a21*other.a11 + self.a22*other.a21, self.a20*other.a02 + self.a21*other.a12 + self.a22*other.a22]]
        
        return mult
    
    