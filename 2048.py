import random
import os
import keyboard  # 需要安装：pip install keyboard

# 初始化游戏板
block=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
# 生成两个初始数字块
empty_indices = [i for i in range(16) if block[i] == 0]
if empty_indices:
    block[random.choice(empty_indices)] = 2 if random.random() < 0.9 else 4  # 90%概率生成2，10%概率生成4
    empty_indices = [i for i in range(16) if block[i] == 0]
    if empty_indices:
        block[random.choice(empty_indices)] = 2 if random.random() < 0.9 else 4

b1 = []  # 上一个状态
b2 = [1]  # 历史状态列表，b2[0]是当前状态索引
cz = 0  # 操作标志

def clear_screen():
    """清空屏幕"""
    os.system('cls' if os.name == 'nt' else 'clear')

def display_board():
    """显示游戏板"""
    # 计算总分
    zongfen = sum(block)
    print(f"总分：{zongfen}")
    print("Ctrl+R:重新开始 Ctrl+Q:退出 Ctrl+Z:撤销 Ctrl+Y:取消撤销 wasd:移动")
    
    # 显示游戏板
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

def check_game_status():
    """检查游戏状态（胜利或失败）"""
    # 判断是否胜利
    if 2048 in block:
        print("你赢了！")
        return False
    
    # 判断是否失败
    b4 = 0
    b3 = block.copy()
    for i in range(15):
        if not((i+1)%4==0):
            if b3[i] == b3[i+1]:
                b4 += 1
    for i in range(12):
        if b3[i] == b3[i+4]:
            b4 += 1
    if b4 == 0 and not(0 in b3):
        print("你输了,没有地方可以移动了")
        return False
    
    return True

def move_up():
    moved = False
    for col in range(4):
        # 移动所有非零元素向上
        for row in range(1, 4):
            if block[row*4+col] != 0:
                current_row = row
                while current_row > 0 and block[(current_row-1)*4+col] == 0:
                    block[(current_row-1)*4+col] = block[current_row*4+col]
                    block[current_row*4+col] = 0
                    current_row -= 1
                    moved = True
        # 合并相同数字
        for row in range(1, 4):
            if block[row*4+col] != 0 and block[row*4+col] == block[(row-1)*4+col]:
                block[(row-1)*4+col] *= 2
                block[row*4+col] = 0
                moved = True
        # 再次移动所有非零元素向上
        for row in range(1, 4):
            if block[row*4+col] != 0:
                current_row = row
                while current_row > 0 and block[(current_row-1)*4+col] == 0:
                    block[(current_row-1)*4+col] = block[current_row*4+col]
                    block[current_row*4+col] = 0
                    current_row -= 1
    return moved

def move_down():
    moved = False
    for col in range(4):
        # 移动所有非零元素向下
        for row in range(2, -1, -1):
            if block[row*4+col] != 0:
                current_row = row
                while current_row < 3 and block[(current_row+1)*4+col] == 0:
                    block[(current_row+1)*4+col] = block[current_row*4+col]
                    block[current_row*4+col] = 0
                    current_row += 1
                    moved = True
        # 合并相同数字
        for row in range(2, -1, -1):
            if block[row*4+col] != 0 and block[row*4+col] == block[(row+1)*4+col]:
                block[(row+1)*4+col] *= 2
                block[row*4+col] = 0
                moved = True
        # 再次移动所有非零元素向下
        for row in range(2, -1, -1):
            if block[row*4+col] != 0:
                current_row = row
                while current_row < 3 and block[(current_row+1)*4+col] == 0:
                    block[(current_row+1)*4+col] = block[current_row*4+col]
                    block[current_row*4+col] = 0
                    current_row += 1
    return moved

def move_left():
    moved = False
    for row in range(4):
        # 移动所有非零元素向左
        for col in range(1, 4):
            if block[row*4+col] != 0:
                current_col = col
                while current_col > 0 and block[row*4+current_col-1] == 0:
                    block[row*4+current_col-1] = block[row*4+current_col]
                    block[row*4+current_col] = 0
                    current_col -= 1
                    moved = True
        # 合并相同数字
        for col in range(1, 4):
            if block[row*4+col] != 0 and block[row*4+col] == block[row*4+col-1]:
                block[row*4+col-1] *= 2
                block[row*4+col] = 0
                moved = True
        # 再次移动所有非零元素向左
        for col in range(1, 4):
            if block[row*4+col] != 0:
                current_col = col
                while current_col > 0 and block[row*4+current_col-1] == 0:
                    block[row*4+current_col-1] = block[row*4+current_col]
                    block[row*4+current_col] = 0
                    current_col -= 1
    return moved

def move_right():
    moved = False
    for row in range(4):
        # 移动所有非零元素向右
        for col in range(2, -1, -1):
            if block[row*4+col] != 0:
                current_col = col
                while current_col < 3 and block[row*4+current_col+1] == 0:
                    block[row*4+current_col+1] = block[row*4+current_col]
                    block[row*4+current_col] = 0
                    current_col += 1
                    moved = True
        # 合并相同数字
        for col in range(2, -1, -1):
            if block[row*4+col] != 0 and block[row*4+col] == block[row*4+col+1]:
                block[row*4+col+1] *= 2
                block[row*4+col] = 0
                moved = True
        # 再次移动所有非零元素向右
        for col in range(2, -1, -1):
            if block[row*4+col] != 0:
                current_col = col
                while current_col < 3 and block[row*4+current_col+1] == 0:
                    block[row*4+current_col+1] = block[row*4+current_col]
                    block[row*4+current_col] = 0
                    current_col += 1
    return moved

# 初始状态保存到历史
b2.append(block.copy())

# 显示初始界面
clear_screen()
display_board()

# 注册热键
keyboard.add_hotkey('ctrl+z', lambda: undo())
keyboard.add_hotkey('ctrl+y', lambda: redo())
keyboard.add_hotkey('ctrl+r', lambda: restart())
keyboard.add_hotkey('ctrl+q', lambda: exit_game())

def undo():
    """撤销操作"""
    global block, b2
    if b2[0] > 1:
        b2[0] -= 1
        block = b2[b2[0]].copy()
        update_display()

def redo():
    """取消撤销"""
    global block, b2
    if b2[0] < len(b2) - 1:
        b2[0] += 1
        block = b2[b2[0]].copy()
        update_display()

def restart():
    """重新开始游戏"""
    global block, b2, cz
    block = [0] * 16
    empty_indices = [i for i in range(16) if block[i] == 0]
    if empty_indices:
        block[random.choice(empty_indices)] = 2 if random.random() < 0.9 else 4
        empty_indices = [i for i in range(16) if block[i] == 0]
        if empty_indices:
            block[random.choice(empty_indices)] = 2 if random.random() < 0.9 else 4
    # 重置历史
    b2 = [1, block.copy()]
    cz = 0
    update_display()

def exit_game():
    """退出游戏"""
    global game_running
    game_running = False
    keyboard.unhook_all()
    print("游戏结束！")
    exit()

def update_display():
    """更新显示"""
    clear_screen()
    display_board()
    if not check_game_status():
        # 游戏结束，等待用户按下任意键退出或重新开始
        print("按任意键继续...")
        keyboard.read_event()
        exit_game()

# 游戏主循环
game_running = True
while game_running:
    # 保存当前状态
    b1 = block.copy()
    
    # 等待键盘输入
    event = keyboard.read_event()
    if event.event_type != keyboard.KEY_DOWN:
        continue
        
    key = event.name.lower()
    
    # 处理移动
    moved = False
    if key in ["w", "up"]:
        moved = move_up()
    elif key in ["s", "down"]:
        moved = move_down()
    elif key in ["a", "left"]:
        moved = move_left()
    elif key in ["d", "right"]:
        moved = move_right()
    
    # 如果有移动，添加新数字并更新历史
    if moved:
        # 查找空位置
        empty_indices = [i for i in range(16) if block[i] == 0]
        if empty_indices:
            # 随机选择一个空位置添加新数字
            block[random.choice(empty_indices)] = 2 if random.random() < 0.9 else 4
            
            # 更新历史
            # 如果当前不是最新状态，删除后面的历史
            while len(b2) > b2[0] + 1:
                b2.pop()
            # 添加新状态
            b2.append(block.copy())
            b2[0] = len(b2) - 1
        
        # 更新显示
        update_display()