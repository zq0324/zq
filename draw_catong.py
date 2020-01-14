from tkinter import *

window = Tk()
window.title("tkinter")  # 窗口的标题
window.geometry("800x600")  # 窗口的大小
canvas = Canvas(window, width=700, height=500, bg="lightblue")
canvas.pack()
# 右手
canvas.create_oval(275, 335, 335, 395, fill="white")
canvas.create_polygon(215, 260, 315, 335, 285, 365, 230, 305, fill="blue", outline="black")
# 脚
canvas.create_oval(205, 425, 290, 475, fill="white")
canvas.create_oval(205, 425, 115, 475, fill="white")
# 左手
canvas.create_oval(73, 335, 133, 395, fill="white")
canvas.create_polygon(190, 260, 90, 335, 120, 365, 205, 305, fill="blue", outline="black")
# 肚子
canvas.create_oval(115, 285, 285, 450, fill="blue")
canvas.create_oval(130, 300, 268, 428, fill="white")
canvas.create_arc(143, 285, 256, 418, extent=-180, fill="white")
# 脸
canvas.create_oval(100, 110, 300, 300, fill="blue")
canvas.create_oval(110, 140, 290, 300, fill="white")
# 鼻子
canvas.create_oval(184, 160, 210, 185, fill="red")
canvas.create_oval(193, 165, 202, 174, fill="white")
# 眼睛
canvas.create_oval(196, 122, 230, 167, fill="white")
canvas.create_oval(162, 122, 196, 167, fill="white")
# 左眼瞳孔
canvas.create_oval(170, 130, 188, 155, fill="black")
canvas.create_oval(174, 134, 184, 144, fill="white")
# 右眼瞳孔
canvas.create_oval(204, 130, 222, 155, fill="black")
canvas.create_oval(208, 134, 218, 144, fill="white")
# 嘴
canvas.create_arc(125, 150, 275, 286, extent=-180, fill="red")
# canvas.create_arc(275,275,200,200,extent = -180,style = ARC)
# 中间胡须
canvas.create_line(198, 185, 198, 220, fill="black")
# 左边胡须
canvas.create_line(123, 165, 178, 190, fill="black")
canvas.create_line(113, 195, 178, 196, fill="black")
canvas.create_line(113, 220, 178, 202, fill="black")

# 右边胡须
canvas.create_line(280, 165, 218, 190, fill="black")
canvas.create_line(285, 195, 218, 196, fill="black")
canvas.create_line(285, 220, 218, 202, fill="black")
# 板牙
# canvas.create_rectangle(155,220,170,240,fill = "white")
# canvas.create_rectangle(170,220,185,240,fill = "white")
canvas.create_rectangle(185, 219, 200, 240, fill="white")
canvas.create_rectangle(200, 219, 215, 240, fill="white")
# canvas.create_rectangle(215,220,230,240,fill = "white")
# canvas.create_rectangle(230,220,245,240,fill = "white")
# 领结和铃铛
canvas.create_rectangle(143, 303, 258, 288, fill="red")
canvas.create_oval(184, 295, 215, 325, fill="gold")
canvas.create_rectangle(184, 311, 215, 304, fill="gold")
canvas.create_oval(195, 313, 203, 320, fill="black")
canvas.create_line(199, 320, 199, 325, fill="black")

# 第二个

# 右手
canvas.create_oval(575, 335, 635, 395, fill="white")

canvas.create_polygon(515, 260, 615, 335, 585, 365, 530, 305, fill="pink", outline="black")
# 脚
canvas.create_oval(505, 425, 590, 475, fill="white")
canvas.create_oval(505, 425, 415, 475, fill="white")
# 左手
canvas.create_oval(373, 335, 433, 395, fill="white")
canvas.create_polygon(490, 260, 390, 335, 420, 365, 505, 305, fill="pink", outline="black")
# 肚子
canvas.create_oval(415, 285, 585, 450, fill="pink")
canvas.create_oval(430, 300, 568, 428, fill="white")
canvas.create_arc(443, 285, 556, 418, extent=-180, fill="white")
# 脸
canvas.create_oval(400, 110, 600, 300, fill="pink")
canvas.create_oval(410, 140, 590, 300, fill="white")
# 鼻子
canvas.create_oval(484, 160, 510, 185, fill="red")
canvas.create_oval(493, 165, 502, 174, fill="white")
# 眼睛
canvas.create_oval(496, 122, 530, 167, fill="white")
canvas.create_oval(462, 122, 496, 167, fill="white")
# 左眼瞳孔
canvas.create_oval(470, 130, 488, 155, fill="black")
canvas.create_oval(474, 134, 484, 144, fill="white")
# 右眼瞳孔
canvas.create_oval(504, 130, 522, 155, fill="black")
canvas.create_oval(508, 134, 518, 144, fill="white")
# 嘴
canvas.create_arc(425, 150, 575, 286, extent=-180, fill="red")
# canvas.create_arc(275,275,200,200,extent = -180,style = ARC)
# 中间胡须
canvas.create_line(498, 185, 498, 220, fill="black")
# 左边胡须
canvas.create_line(423, 165, 478, 190, fill="black")
canvas.create_line(413, 195, 478, 196, fill="black")
canvas.create_line(413, 220, 478, 202, fill="black")

# 右边胡须
canvas.create_line(580, 165, 518, 190, fill="black")
canvas.create_line(585, 195, 518, 196, fill="black")
canvas.create_line(585, 220, 518, 202, fill="black")
# 板牙
# canvas.create_rectangle(155,220,170,240,fill = "white")
# canvas.create_rectangle(170,220,185,240,fill = "white")
canvas.create_rectangle(485, 219, 500, 240, fill="white")
canvas.create_rectangle(500, 219, 515, 240, fill="white")
# canvas.create_rectangle(215,220,230,240,fill = "white")
# canvas.create_rectangle(230,220,245,240,fill = "white")
# 领结和铃铛
canvas.create_rectangle(443, 303, 558, 288, fill="red")
canvas.create_oval(484, 295, 515, 325, fill="gold")
canvas.create_rectangle(484, 311, 515, 304, fill="gold")
canvas.create_oval(495, 313, 503, 320, fill="black")
canvas.create_line(499, 320, 499, 325, fill="black")

window.mainloop()  # 让窗口一直存在

