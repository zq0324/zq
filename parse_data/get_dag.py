# coding = utf-8
import time



def get_one_device(deviceID,start, end):
    with open("0123.txt", "r") as f:
        lines = f.readlines()
    num = 0
    status = False
    with open(deviceID + ".log", "a+") as f:
        for l in lines:
            if l.strip().find(deviceID) > 0 :
                if l.strip().find(start) >= 0:
                    print("start......")
                    status = True
                    num = 1
                    print("find %s .." % num)
                    f.write(l)
                elif status :

                    num += 1
                    print("find %s .." % num)
                    f.write(l)
                elif l.strip().find(end) >= 0:
                    num +=1
                    f.write(l)
                    status = False
                    print("find %s .." % num)
                    print("end.......")
                    break




id = "330302028-2094-4937"
get_one_device(id,"1555911170109","000000000000")

