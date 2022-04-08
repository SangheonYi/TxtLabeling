from tkinter import *


#  예제 1) tkinter 파이썬 GUI 레이블(label)
# tkinter를 사용하여 텍스트를 나타내보자

# 1. 루트화면 (root window) 생성
tk = Tk() 
# 2. 텍스트 표시
label = Label(tk,text='Hello World!') 
# 3. 레이블 배치 실행
label.pack()
# 4. 메인루프 실행
tk.mainloop()
