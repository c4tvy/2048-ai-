import random
block=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
if random.randint(1,10) == 10:
    block[random.randint(1,16)-1]=4
else:
    block[random.randint(1,16)-1]=2
b1=[]
b2=[1]
b3=[]
cz=0
def up(up2):
    for up1 in "012010":
        if block[int(up1)*4+up2] == 0:
            block[int(up1)*4+up2]=block[int(up1)*4+up2+4]
            block[int(up1)*4+up2+4]=0
def down(down2):
    for down1 in "321323":
        if block[int(down1)*4+down2] == 0:
            block[int(down1)*4+down2]=block[int(down1)*4+down2-4]
            block[int(down1)*4+down2-4]=0
def left(left1):
    for left2 in "012010":
        if block[int(left2)+left1*4] == 0:
            block[int(left2)+left1*4]=block[int(left2)+left1*4+1]
            block[int(left2)+left1*4+1]=0
def right(right1):
    for right2 in "321323":
        if block[int(right2)+right1*4] == 0:
            block[int(right2)+right1*4]=block[int(right2)+right1*4-1]
            block[int(right2)+right1*4-1]=0
while True:
    can=[]
    for i in range(16):
        if block[i] ==0:
            can.append(i)
    if block != b1 and cz==0 :
        if random.randint(1,10) == 10:
            block[can[random.randint(1,(len(can)))-1]]=4
        else:
            block[can[random.randint(1,(len(can)))-1]]=2
        b2.append(block.copy())
        b2[0]=b2[0]+1
    elif cz==1 and b2[0]>1:
        cz=0
        block=b2[b2[0]-1]
        b2[0]=b2[0]-1
    elif cz==1 and b2[0]==1:
        block=b2[1]
    elif cz==1:
        cz=0
    elif cz==2 and len(b2)-1>b2[0]:
        b2[0]+=1
        block=b2[b2[0]]
        cz=0
    zongfen=0
    for i in block:
        zongfen+=i
    print(f"总分：{zongfen}")
    for a in range(16):
        if (a+1)%4 ==0:
            print("_"*(4-len(str(block[a]))),end="")
            if block[a] ==0:
                print("_")
            else:
                print(block[a])
        else:    
            print("_"*(4-len(str(block[a]))),end="")
            if block[a] ==0:
                print("_",end="  ")
            else:
                print(block[a],end="  ")
    b1=block.copy()
    key=input("wasd移动，r键重新开始，q键退出，z键撤销，y键取消撤销")
    if key == "q":
        break
    elif key == "r":
        block=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        block[random.randint(1,16)-1]=(random.randint(1,2))*2
        b2=[1]
    elif key == "z":
        cz=1
    elif key == "y":
        cz=2
    elif key=="w":
        for up2 in range(4):
            up(up2)
            for up1 in "012":
                if block[int(up1)*4+up2] == block[int(up1)*4+up2+4]:
                    block[int(up1)*4+up2]=block[int(up1)*4+up2+4]*2
                    block[int(up1)*4+up2+4]=0
            up(up2)
        for i in range(len(b2)-1-b2[0]):
            b2.pop(len(b2)-1)
    elif key=="s":
        for down2 in range(4):
            down(down2)
            for down1 in "321":
                if block[int(down1)*4+down2] == block[int(down1)*4+down2-4]:
                    block[int(down1)*4+down2]=block[int(down1)*4+down2]*2
                    block[int(down1)*4+down2-4]=0
            down(down2)
        for i in range(len(b2)-1-b2[0]):
            b2.pop(len(b2)-1)
    elif key=="a":
        for left1 in range(4):
            left(left1)
            for left2 in "012":
                if block[int(left2)+left1*4] == block[int(left2)+left1*4+1]:
                    block[int(left2)+left1*4]=block[int(left2)+left1*4]*2
                    block[int(left2)+left1*4+1]=0
            left(left1)
        for i in range(len(b2)-1-b2[0]):
            b2.pop(len(b2)-1)
    elif key=="d":
        for right1 in range(4):
            right(right1)
            for right2 in "321":
                if block[int(right2)+right1*4] == block[int(right2)+right1*4-1]:
                    block[int(right2)+right1*4]=block[int(right2)+right1*4]*2
                    block[int(right2)+right1*4-1]=0
            right(right1)
        for i in range(len(b2)-1-b2[0]):
            b2.pop(len(b2)-1)
    if 2048 in block:
        print("你过关！")
        break
    b4=0
    b3=block.copy()
    for i in range(15):
        if not((i+1)%4==0):
            if b3[i] == b3[i+1]:
                b4+=1
    for i in range(12):
        if b3[i] == b3[i+4]:
            b4+=1
    if b4 == 0 and not(0 in b3):
        print("你输了,没有地方可以移动了")