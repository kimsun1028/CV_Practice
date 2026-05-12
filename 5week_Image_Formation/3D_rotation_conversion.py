import numpy as np
from scipy.spatial.transform import Rotation

euler = (45,30,60) #xyz 축 방향 기준 각도

robj = Rotation.from_euler('zyx', euler[::-1], degrees = True)

print('\n## Euler Angle(ZYX)')
print(np.rad2deg (robj.as_euler('zyx'))) 
print('\n## Rotation Matrix')
print(robj.as_matrix())
print('\n## Rotation Vector')
print(robj.as_rotvec())
print('\n## Quaternion (XYZW)')
print(robj.as_quat())