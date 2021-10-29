#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Top universities
from PIL import Image

#read the image
harvard = ("Harvard.jpg")
massachusest = Image.open("Massachusest.jpg")
Stanford = Image.open("Stanford.jpg")
berkeley = Image.open("Berkeley.jpg")
oxford = Image.open("Oxford.jpg")
columbia = Image.open("Columbia.jpg")
colifornia = Image.open("Colifornia.jpg")
washington = Image.open("Washington.jpg")
a = " Harvard University is a private Ivy League research university in Cambridge, Massachusetts. Founded in 1636 as Harvard College and named for its first benefactor, the Puritan clergyman John Harvard, it is the oldest institution of higher learning in the United States and among the most prestigious in the world"
b = "Massachusetts Institute of Technology is a private land-grant research university in Cambridge, Massachusetts. Established in 1861, MIT has since played a key role in the development of modern technology and science and has been ranked among the top academic institutions in the world"
c = "Stanford University, officially Leland Stanford Junior University, is a private research university in Stanford, California. The campus occupies 8,180 acres, among the largest in the United States, and enrolls over 17,000 students. Stanford is ranked among the best universities in the world."
d = "The University of California, Berkeley is a public land-grant research university in Berkeley, California. Established in 1868 as the University of California, it is the state's first land-grant university and the first campus of the University of California system."
e = "The University of Oxford is a collegiate research university in Oxford, England. There is evidence of teaching as early as 1096, making it the oldest university in the English-speaking world and the world's second-oldest university in continuous operation."
f = " Columbia University is a private Ivy League research university in New York City. Established in 1754 as King's College on the grounds of Trinity Church in Manhattan, Columbia is the oldest institution of higher education in New York and the fifth-oldest institution of higher learning in the United States"
g = "The University of California (UC) is a public land-grant research university system in the U.S. state of California. The system is composed of the campuses at Berkeley, Davis, Irvine, Los Angeles, Merced, Riverside, San Diego, San Francisco, Santa Barbara, and Santa Cruz, along with numerous research centers and academic abroad centers"
h = "Washington University in St. Louis is a private research university in Greater St. Louis with its main campus mostly in unincorporated St. Louis County, Missouri, and Clayton, Missouri"

university = input("Dunyoning Top 8 Universitetlari haqida ma`lumot beramiz, qaysi biriga o`qish qiziqishini bildirasiz?: ")

if university == "harvard":
    harvard.show()
    print(f"{a}")
elif university == "massachusest":
    massachusest.show()
    print(f"{b}")
elif university == "stanford":
    stanford.show()
    print(f"{c}")
elif university == "berkeley":
    berkeley.show()
    print(f"{d}")
elif university == "oxford":
    oxford.show()
    print(f" {e}")
elif university == "columbia":
    columbia.show()
    print(f" {f}")
elif university == "colifornia":
    colifornia.show()
    print(f" {g}")

    
else:
    washington.show()
    print(f" {h}")


# In[ ]:




