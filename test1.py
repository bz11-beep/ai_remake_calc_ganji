from tkinter import *

cg = ['갑', '을', '병', '정', '무', '기', '경', '신', '임', '계']
gg = ['자', '축', '인', '묘', '진', '사', '오', '미', '신', '유', '술', '해']

window = Tk()
window.title("60갑자 계산기")
window.geometry('300x150')

Label(window, text="천간지지 계산 년도 입력").grid(column=0, row=0, padx=10, pady=10)
lable1 = Entry(window)
lable1.grid(column=1, row=0)

def calc_ganji():
    year = int(lable1.get())
    base_year = 1984
    diff = year - base_year
    tg = cg[diff % 10]
    dz = gg[diff % 12]
    result_label.config(text=f"{year}년은 {tg}{dz}년입니다")

but = Button(window, text="천간지지 확인", command=calc_ganji)
but.grid(column=0, row=1, columnspan=2, pady=10)

result_label = Label(window, text="")
result_label.grid(column=0, row=2, columnspan=2)

window.mainloop()
