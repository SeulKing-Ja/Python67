Table = [
    [9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9],
]

# แสดงตารางเกม
def display():
    # วนลูปแสดงแต่ละแถวและแต่ละคอลัมน์
    for row in Table:
        for col in row:
            if col == 'X':
                print("X", end=" ")
            else:
                print(col, end=" ")
        print()  # ขึ้นบรรทัดใหม่หลังจากแสดงแต่ละแถว

def position_diff(row1,row2,col1,col2):
    # """คำนวณระยะทางระหว่างสองตำแหน่ง"""
    return max(abs(row1-row2),abs(col1-col2))

# ขอให้ผู้ใช้ป้อนจำนวนระเบิด
n = int(input("Enter Number Mine : "))
if n >= 1 and n <=5:
    mine_location = []
    # รับตำแหน่งของระเบิดจากผู้ใช้
    for i in range(n):
        row,col = input(F"Enter {i+1} Location [Row,Col] :").split(" ")
        row,col = int(row),int(col)
        mine_location.append([row-1,col-1])  # ปรับ index ให้ตรงกับตาราง (เริ่มจาก 0)

    # วนลูปผ่านแต่ละตำแหน่งของระเบิด
    for pos in range(len(mine_location)):
        mine_row = mine_location[pos][0]
        mine_col = mine_location[pos][1]

        # วนลูปผ่านแต่ละเซลล์ในตาราง
        for row in range(len(Table)):
            for col in range(len(Table)):
                # ถ้าเป็นตำแหน่งของระเบิด ให้ใส่ 'X'
                if mine_row == row and mine_col == col:
                    Table[row][col] = 'X'
                # ถ้าไม่ใช่ระเบิด ให้คำนวณระยะทางไปยังระเบิดที่ใกล้ที่สุด
                elif Table[row][col] != 'X':
                    # คำนวณระยะทางและอัปเดตค่าในตาราง
                    Table[row][col] = min(Table[row][col],position_diff(mine_row,row,mine_col,col))
    # แสดงตารางผลลัพธ์
        display()
        print()
else:
    print("Input Number Mine Error")