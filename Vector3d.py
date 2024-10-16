
def reLU(x):
  if x <0 :
    return 0
  else:
    return x

def e(i):
  ei =i
  ei = ei + i

class Matrix:
  def __init__(self,v1,v2):
    self.ihat = v1
    self.jhat = v2
  def __mul__(self,other):
    if isinstance(other,Matrix):
      return Matrix(other * self.ihat,other * self.jhat)
    elif isinstance(other,Vector):
      return other * self
  def __str__(self):
    return f"ihat: \n{str(self.ihat)}\njhat: \n{str(self.jhat)}"
    
class Vector:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def __add__(self, other):
    if isinstance(other, Vector):
      return Vector(self.x + other.x, self.y + other.y)
    else:
      return Vector('error','error')

  def __mul__(self, other):
    if isinstance(other, Matrix):
      s1 = Vector(self.x * other.ihat.x, self.x * other.ihat.y)
      s2 = Vector(self.y * other.jhat.x, self.y * other.jhat.y)
      s3 = s1 + s2
      return s3
    elif isinstance(other, (int,float)):
      return Vector(self.x * other, self.y * other)
    else:
      return Vector('error','error')

  def __str__(self):
    strn = '[ '
    space1 = reLU((len(str(self.y))- len(str(self.x)))/2)
    space2 = reLU((len(str(self.x)) - len(str(self.y)))/2)
    x = self.x
    y = self.y
    if space1 > 0 and space1 < 1:
      x = str(self.x) + '0'
      if self.x > 0 :
        x = str(self.x) + ' '
    if space2 > 0 and space2 < 1:
      y = str(self.y) + '0'
      if self.y > 0 :
        y = str(self.y) + ' '

    space1 = int(space1)
    space2 = int(space2)

    for i in range(space1):
      strn = strn + " "
      e(i)
    strn = strn + str(x)
    for i in range(space1):
      strn = strn + " "
      e(i)
    strn = strn + " ]\n[ "
    for i in range(space2):
      strn = strn + " "
      e(i)
    strn = strn + str(y)
    for i in range(space2):
      e(i)
      strn = strn + " "
    strn = strn + " ]"
    return strn

class Matrix3d:
  def __init__(self,v1,v2,v3):
    self.ihat = v1
    self.jhat = v2
    self.khat = v3
  def __mul__(self,other):
    if isinstance(other,Matrix3d):
      return Matrix3d(other * self.ihat,other * self.jhat, other * self.khat)
    elif isinstance(other,Vector3d):
      return other * self
  def __str__(self):
    return f"ihat: \n{str(self.ihat)}\njhat: \n{str(self.jhat)}\nkhat: \n{str(self.khat)}"

class Vector3d:
  def __init__(self, x, y, z):
    self.x = x
    self.y = y
    self.z = z

  def __add__(self, other):
    if isinstance(other, Vector3d):
      return Vector3d(self.x + other.x, self.y + other.y, self.z + other.z)
    else:
      return Vector3d('error','error','error')

  def __mul__(self, other):
    if isinstance(other, Matrix3d):
      s1 = Vector3d(self.x * other.ihat.x, self.x * other.ihat.y, self.x * other.ihat.z)
      s2 = Vector3d(self.y * other.jhat.x, self.y * other.jhat.y, self.y * other.jhat.z)
      s3 = Vector3d(self.z * other.khat.x, self.z * other.khat.y, self.z * other.khat.z)
      s4 = s1 + s2 + s3
      return s4
    elif isinstance(other, (int,float)):
      return Vector3d(self.x * other, self.y * other, self.z * other)
    else:
      return Vector3d('error','error', 'error')

  def __str__(self):
    strn = '[ '
    refrance = max([len(str(self.y)),len(str(self.x)),len(str(self.z))])
    
    space1 = reLU((refrance- len(str(self.x)))/2)
    space2 = reLU((refrance - len(str(self.y)))/2)
    space3 = reLU((refrance - len(str(self.z)))/2)
    x = self.x
    y = self.y
    z = self.z
    if space1 > 0 and space1 < 1:
      x = str(self.x) + '0'
      if self.x > 0 :
        x = str(self.x) + ' '
    if space2 > 0 and space2 < 1:
      y = str(self.y) + '0'
      if self.y > 0 :
        y = str(self.y) + ' '
    if space3 > 0 and space3 < 1:
      z = str(self.z) + '0'
      if self.z > 0 :
        z = str(self.z) + ' '
  
    space1 = int(space1)
    space2 = int(space2)
    space3 = int(space3)

    for i in range(space1):
      strn = strn + " "
      e(i)
    strn = strn + str(x)
    for i in range(space1):
      strn = strn + " "
      e(i)
    strn = strn + " ]\n[ "
    for i in range(space2):
      strn = strn + " "
      e(i)
    strn = strn + str(y)
    for i in range(space2):
      e(i)
      strn = strn + " "
    strn = strn + " ]\n[ "
    for i in range(space3):
      strn = strn + " "
      e(i)
    strn = strn + str(z)
    for i in range(space3):
      e(i)
      strn = strn + " "
    strn = strn + " ]"
    
    return strn
    