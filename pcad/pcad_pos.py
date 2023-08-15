class pos:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
        pass
    
    def mov(self, x, y, z):
        self.x = self.x + x
        self.y = self.y + y
        self.z = self.z + z
        pass
        
    
class rot:
    def __init__(self, ax=0, ay=0, az=0) -> None:
        self.ax = ax
        self.ay = ay
        self.az = az
        pass
    
    def rot(self, ax, ay, az) -> None:
        self.ax = (self.ax + ax) % 360
        self.ay = (self.ay + ay) % 360
        self.az = (self.az + az) % 360
        

