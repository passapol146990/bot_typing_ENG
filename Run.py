from tkinter import *
from tkinter.ttk import Notebook
from tkinter import messagebox
from tkinter import ttk
from website import*
font1 = ('Angsana New',25)
font2 = ('Angsana New',20)
font3 = ('Angsana New',15)
font4 = ('Angsana New',10)
wpm = ['wpm',0,0.01,0.1]

def show_message():
    messagebox.showinfo("Message", "Hello, this is your GUI app!")

def main():
    root = Tk()
    root.geometry("700x500")
    root.title("Auto write typing Study v.1.0")

    warning_text = Label(root, text="", font=font3)
    warning_text.pack()

    frame0 = Frame(root,width=400,height=180)
    frame0.pack()
    frame3 = Frame(root,width=400,height=180)

    Tap = Notebook(root)
    frame1 = Frame(Tap,width=400,height=180)
    def create_tap(token_ID):
        if token_ID == True:
            warning_text.config(text="Welcome to auto Write typing. v.1.0")

            Tap.add(frame1,text="typing Study")
            frame0.destroy()
            messagebox.showinfo("Successfully","เข้าสู่ระบบสำเร็จ")
            Tap.pack(expand=False, fill=BOTH, padx= 5, pady=5)
            frame3.pack()
            
        else:
            warning_text.config(text="@contact Facebook : พัสพล พลังชีวิต")



    def jen_tokens():
        # ฟังก์ชันเช็คคีย์    
        token_check = key.get()
        username = Username.get()
        create_tap(True)
        
# ฟังก์ชันเช็คคีย์
    key = StringVar()
    set_key = Entry(frame0, textvariable=key, width=30)
    set_key.pack()

# ฟังก์ชันเข้าสู่ระบบอัตโนมัติ
    Username = StringVar()
    user = Entry(frame0, textvariable=Username, width=30)
    user.pack()

    button = Button(frame0, text="login", command=jen_tokens)
    button.pack(pady=5)
    # jen_tokens() #///////////////////////////////////////////////////////////////////////
    title2 = Label(frame3, text="เลือกวินาทีในการพิมพ์", font=font1)
    title2.pack(pady=5)
    option_var = StringVar()
    option_var.set("Select an option")
    option_menu = ttk.OptionMenu(frame3, option_var, *wpm)
    option_menu.pack(pady=20)
    result_label = Label(frame3, text="", font=font3)
    result_label.pack()

    def setSpeedWriter1():
        session1 =  messagebox.showwarning("กำลังจะพิมพ์...","เมื่อกด ok รอจนกว่าจะพิมพ์เสร็จ")
        if session1 == "ok":
            selected_option = option_var.get()
            result_label.config(text='ชี้แจง : ยิ่ง WPM น้อยยิ่งพิมพ์เร็ว')
            try:
                wpm = float(selected_option)
                autoWrite(wpm)
                result_label.config(text='พิมพ์สำเร็จ')
            except:
                session1 =  messagebox.showwarning("แจ้งเตือน!","กรุณาเลือก WPM")
        else:
            print(session1)

    title_f1 = Label(frame1, text="กดเพื่มเริ่มทำงาน พิมพ์ typing test", font=font1)
    title_f1.pack(pady=5)
    btn_typing1 = Button(frame1, text="Write typing", command=setSpeedWriter1)
    btn_typing1.pack(pady=5)
    
    root.mainloop() 

if __name__ == "__main__":
    main()
drive.quit()
print('off line')