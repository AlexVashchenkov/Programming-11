from tkinter import *

l = [8, 7, 6, 5, 4, 3, 2, 1]
n = len(l)
eps = 3.125

sorting_list = []
buff = []
while l != sorted(l):
    for i in range(len(l)-1):
        if buff == [] or i != buff[-1][1]:
            if l[i] > l[i+1]:
                l[i], l[i+1] = l[i+1], l[i]
                buff.append([i, i+1])
    sorting_list.append(buff)
    buff = []
'''fill="#fff"'''
def draw_swap(index1, index2, x):
    canv.create_oval(x - eps, index1 - eps, x + eps, index1 + eps, fill="#000")
    canv.create_oval(x - eps, index2 - eps, x + eps, index2 + eps, fill="#000")
    canv.create_line(x, index1, x, index2)

root = Tk()
lengthxwidth = '810x810'
root.geometry(lengthxwidth + '+1+1')

canv = Canvas(bg='white')
canv.pack(fill=BOTH, expand=1)

for i in range(len(l)):
    canv.create_line(10, 200 + 50 * i, 800, 200 + 50 * i)

for j in range(len(sorting_list)):
    for i in sorting_list[j]:
        draw_swap(200 + 50 * i[0], 200 + 50 * i[1], (800//len(sorting_list)) + ((800//len(sorting_list)) * j))

mainloop()