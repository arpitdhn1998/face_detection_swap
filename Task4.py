#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import numpy 


# In[2]:


photo=numpy.zeros((500,500,3))
photo.shape


# In[3]:


#face
circle=cv2.circle(photo,(250,100),(50),(200,0,0),cv2.FILLED)
#stomach
rectangle=cv2.rectangle(photo,(200,150),(300,300),(0,200,0),cv2.FILLED)
#leg1
rectangle=cv2.rectangle(photo,(210,300),(230,400),(0,120,200),cv2.FILLED)
#legs2
rectangle=cv2.rectangle(photo,(260,300),(280,400),(0,120,200),cv2.FILLED)


# In[4]:


cv2.imshow("Task 4",photo)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:





# In[5]:


#cropping an image
crop=photo[50:150,200:305]
cv2.imshow("Task 4",crop)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:





# In[6]:


"""
#hstack resize
image = cv2.resize(crop, (500, 500), None, .25, .25)
cv2.imshow("Task 4",image)
cv2.waitKey(0)
cv2.destroyAllWindows()

new_img=numpy.hstack((photo,image))
"""


# In[ ]:





# In[7]:


photo2=numpy.zeros((500,500,3))
photo2.shape
#face2
circle2=cv2.circle(photo2,(250,100),(50),(0,0,255),cv2.FILLED)
#stomach
rectangle2=cv2.rectangle(photo2,(200,150),(300,300),(0,200,0),cv2.FILLED)
#leg1
rectangle2=cv2.rectangle(photo2,(210,300),(230,400),(100,100,200),cv2.FILLED)
#legs2
rectangle2=cv2.rectangle(photo2,(260,300),(280,400),(100,100,200),cv2.FILLED)


# In[8]:


cv2.imshow("Task 4",photo2)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:





# In[9]:


new_img=numpy.hstack((photo,photo2))
cv2.imshow("task",new_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:





# In[10]:


photo[50:150,200:305]=photo2[50:150,200:305]


# In[11]:


cv2.imshow("Task 4",photo)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:




