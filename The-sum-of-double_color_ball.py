import re
import os
from datetime import datetime



fp = open('D://shuagnseqiu.txt', 'a', 1)

m = 0
num = 0

i1 = i2 = i3 = i4 = i5 = i6 =i7 = 1

time1 = datetime.now()
for i1 in range(1, 34):
    for i2 in range(2, 34):
        if (i1 < i2):
            for i3 in range(3,34):
                time2 = datetime.now() - time1
                print (time2)
                if(i2 < i3):
                    for i4 in range(4, 34):
                        if(i3 < i4):
                            for i5 in range(5, 34):
                                if(i4 < i5):
                                    for i6 in range(6, 34):
                                        if(i5 < i6):
                                            for i7 in range (1, 17):
                                                num += 1
                                                fp.write(str((i1,i2,i3,i4,i5,i6,i7))) 

print ("The last num is ", num)
