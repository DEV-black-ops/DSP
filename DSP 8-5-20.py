#!/usr/bin/env python
# coding: utf-8

# ## Solution 1
# 
# 
# 

# In[ ]:


import jupyterthemes 


# In[1]:


import numpy as n
import numpy.fft as FFT
import matplotlib.pyplot as plt


# In[8]:


day = [n.sin(2*10*n.pi*t) for t in n.linspace(0,1,50)]


# In[9]:


month = [n.sin(2*2*n.pi*t) for t in n.linspace(0,1,50)]


# In[10]:


year = [n.sin(2*2*n.pi*t) for t in n.linspace(0,1,50)]


# In[11]:


mixsin = [i+J+K for i,J,K in zip(day,month,year)]


# In[12]:


fft_wave = FFT.fft(mixsin)


# In[13]:


plt.plot(mixsin)


# In[14]:


plt.plot(fft_wave)


# ## Solution 2
# 

# In[70]:


xp = [0,1,2,3,4,5,6,7] 
fp = [4,5,22,5,14,4,18,1] #DEVENDRA
n.interp(2.5, xp, fp)


# In[72]:


plt.plot(xp,fp ,)


# ## or Solution 2
# 

# In[23]:


import thinkdsp as t
import thinkplot as p
import matplotlib as plt


# In[18]:


data = t.read_wave('Downloads/12345.wav')

data.plot()


# In[21]:


wave1 =   data.segment(start = 0, duration = 2)
spec = wave1.make_spectrum()
spec.plot()


# In[29]:


lowPass = spec.low_pass(700)


# ## solution 3

# In[30]:


import thinkdsp as d
from IPython.display import Audio
import thinkplot as t
from IPython.display import Audio


# In[31]:



m=d.SinSignal(freq=523,amp=3,offset= 0)
n=d.SinSignal(freq=554,amp=3,offset=0)
o=d.SinSignal(freq=587,amp=4,offset=0)
p=d.SinSignal(freq=622,amp=5,offset=0)
q=d.SinSignal(freq=659,amp=5,offset=0)
r=d.SinSignal(freq=698,amp=5,offset=0)
s=d.SinSignal(freq=740,amp=5,offset=0)
t=d.SinSignal(freq=780,amp=5,offset=0)
u=d.SinSignal(freq=831,amp=5,offset=0)
v=d.SinSignal(freq=880,amp=5,offset=0)
w=d.SinSignal(freq=932,amp=5,offset=0)
x=d.SinSignal(freq=988,amp=5,offset=0)
y=d.SinSignal(freq=1047,amp=5,offset=0)


# In[34]:


m1=m.make_wave(duration=1,start=0,framerate=48000)
n1=n.make_wave(duration=1,start=1,framerate=48000)
o1=o.make_wave(duration=1,start=2,framerate=48000)
p1=p.make_wave(duration=1,start=3,framerate=48000)
q1=q.make_wave(duration=1,start=4,framerate=48000)
r1=r.make_wave(duration=1,start=5,framerate=48000)
s1=s.make_wave(duration=1,start=6,framerate=48000)
t1=t.make_wave(duration=1,start=7,framerate=48000)
u1=u.make_wave(duration=1,start=8,framerate=48000)
v1=v.make_wave(duration=1,start=9,framerate=48000)
w1=w.make_wave(duration=1,start=10,framerate=48000)
x1=x.make_wave(duration=1,start=11,framerate=48000)
y1=y.make_wave(duration=1,start=12,framerate=48000)
a= m1+n1+o1+p1+q1+r1+s1+t1+u1+v1+w1+x1+y1
b=Audio(data=a.ys,rate=a.framerate)


# In[35]:


b


# In[ ]:




