import numpy as np
import cv2

#sample points
p1=[[155,120],[480,120],[20,475],[620,475]]
p2=[[0,0],[400,0],[0,600],[400,600]]

k=np.array([[1406.08415449821,0,0],
    [2.20679787308599, 1417.99930662800,0],
    [1014.13643417416, 566.347754321696,1]]).T
print('The K Matrix is:', k)

def homography(p1, p2):
  A= []
  for val in range(0,len(p1)):
    x_1, y_1 = p1[val][0], p1[val][1]
    x_2, y_2 =p2[val][0], p2[val][1]
    A.append([x_1, y_1, 1 ,0 ,0 ,0, -x_2 * x_1, -x_2 * y_1, -x_2 ])
    A.append([0, 0 ,0 ,x_1, y_1, 1, -y_2*x_1, -y_2 * y_1, -y_2 ])

  A=np.array(A)
  u,S,Vh = np.linalg.svd(A)
  #print(Vh)
  l= Vh[-1,:]/Vh[-1,-1]
  h= np.reshape(l,(3,3))
  return h

def img_perspective(h,k):
  h1= h[:,0]
  h2= h[:,1]
  h3= h[:,2]
  k1= np.linalg.inv(k)
  l= 2/(np.linalg.norm(np.matmul(k1,h1))+ np.linalg.norm(np.matmul(k1,h2)))
  #l1= np.linalg.inv(l)
  bt= l* np.matmul(k1,h)
  det= np.linalg.det(bt)
  if det>0:
    b= bt
  else:
    b= -1*bt

  ro1= b[:,0]
  ro2= b[:,1]
  ro3= np.cross(ro1,ro2)
  t= b[:,2]
  R= np.column_stack((ro1,ro2,ro3,t))
  proj_mat= np.matmul(k,R)
  return proj_mat


h= homography(p1,p2)
h1, s1=cv2.Findhomography(p1,p2)
print('The Function Homography is:', h1)
print('')
print('The calculated homography matrix is:', h)
img_perspective(h,k)


