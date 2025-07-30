from tkinter import *
from tkinter import ttk  

cg = ['갑', '을', '병', '정', '무', '기', '경', '신', '임', '계']
gg = ['자', '축', '인', '묘', '진', '사', '오', '미', '신', '유', '술', '해']

def calc_ganji():
    try:
        year = int(year_entry.get())
        base_year = 1984
        diff = year - base_year
        tg = cg[diff % 10]
        dz = gg[diff % 12]
        result_label.config(text=f"{year}년은 \"{tg}{dz}\"년입니다", foreground="green")
    except ValueError:
        result_label.config(text="유효한 연도를 입력해주세요", foreground="red")

window = Tk()
window.title("60갑자 계산기")
window.geometry('400x300')
window.configure(bg='#f0f0f0')

style = ttk.Style()
style.configure('TFrame', background='#f0f0f0')
style.configure('TButton', font=('맑은 고딕', 10), background='#4CAF50')
style.configure('TLabel', font=('맑은 고딕', 11), background='#f0f0f0')
style.configure('Title.TLabel', font=('맑은 고딕', 14, 'bold'), background='#f0f0f0')

main_frame = ttk.Frame(window, padding="20 20 20 20", style='TFrame')
main_frame.pack(fill=BOTH, expand=True)

title_label = ttk.Label(main_frame, text="60갑자 계산기", style='Title.TLabel')
title_label.pack(pady=(0, 20))

input_frame = ttk.Frame(main_frame, style='TFrame')
input_frame.pack(fill=X, pady=10)

year_label = ttk.Label(input_frame, text="연도 입력:", style='TLabel')
year_label.pack(side=LEFT, padx=(0, 10))

year_entry = ttk.Entry(input_frame, width=15, font=('맑은 고딕', 11))
year_entry.pack(side=LEFT)
year_entry.focus()

button_frame = ttk.Frame(main_frame, style='TFrame')
button_frame.pack(pady=20)

calc_button = ttk.Button(button_frame, text="천간지지 확인", command=calc_ganji)
calc_button.pack(side=LEFT, padx=5)

clear_button = ttk.Button(button_frame, text="지우기",
                         command=lambda: [year_entry.delete(0, END), result_label.config(text="")])
clear_button.pack(side=LEFT, padx=5)

result_frame = ttk.Frame(main_frame, style='TFrame')
result_frame.pack(fill=X, pady=10)

result_label = ttk.Label(result_frame, text="", font=('맑은 고딕', 12, 'bold'))
result_label.pack()

window.bind('<Return>', lambda event: calc_ganji())

window.mainloop()
