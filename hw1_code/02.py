import arrow
print("当前的时间是:")
print(arrow.now())
print("输入一个时间(时/分/秒)(以24小时为记):")
print("H:")
h = int(input())
print("M:")
m = int(input())
print("S:")
s = int(input())
print("其一秒后的时间是:")
if s != 59 :
    s = s+1
else :
    s = 0
    if m != 59:
        m = m+1
    else :
        m = 0
        if(h != 23) :
            h = h+1
        else :
            h = 0
print(f'{h}时 {m}分 {s}秒')
if(h == 0 & m == 0 & s == 0):
    print("已经到下一天了")
