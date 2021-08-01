from tkinter import *
from tkinter.filedialog import asksaveasfilename, askopenfilename
from MyQR import myqr
import tkinter.messagebox as messagebox


class App:
    def __init__(self):
        root = Tk()
        root.title('二维码生成器')
        self.path = StringVar()
        self.img_path = StringVar()

        cvs_path = Canvas(root)
        cvs_path.grid(row=0, column=0, columnspan=3, pady=5)
        lab_path = Label(cvs_path, text='保存路径:').grid(row=0, column=0)
        entry_path = Entry(cvs_path, textvariable=self.path).grid(row=0, column=1)
        butt_path = Button(cvs_path, text='选择路径', command=self.get_path).grid(row=0, column=2)

        cvs_img = Canvas(root)
        cvs_img.grid(row=1, column=0, columnspan=3, pady=5)
        lab_img = Label(cvs_img, text='选择图片:').grid(row=1, column=0)
        entry_img = Entry(cvs_img, textvariable=self.img_path).grid(row=1, column=1)
        butt_img = Button(cvs_img, text='选择图片', command=self.get_img).grid(row=1, column=2)

        lab_content = Label(root, text='二维码内容:').grid(row=2, column=0, columnspan=3)
        self.text_content = Text(root, width=40, height=10)

        self.text_content.grid(row=3, column=0, columnspan=3)

        butt_gen = Button(root, text='生成', command=self.gen).grid(row=4, column=0, columnspan=3, pady=5)

        root.mainloop()

    def get_path(self):
        file_path = asksaveasfilename(defaultextension='.png')
        self.path.set(file_path)

    def get_img(self):
        _path = askopenfilename(
            filetypes=[("files", "*.gif"), ("files", "*.bmp"), ("files", "*.png"), ("files", "*.jpg")])
        self.img_path.set(_path)

    def gen(self):
        save_name = self.path.get().split('/')[-1]
        save_dir = self.path.get().replace(save_name, '')
        word = self.text_content.get("1.0", "end").replace("\n", "")
        pic = self.img_path.get()
        try:
            myqr.run(word, version=3, save_name=save_name, save_dir=save_dir, picture=pic, colorized=True)
            messagebox.showinfo(title="成功", message="二维码已生成")
        except Exception as e:
            if word:
                messagebox.showinfo(title="错误", message="暂不支持中文")
            else:
                messagebox.showinfo(title="错误", message="内容不能为空")


if __name__ == '__main__':
    """
    打包：
    pyinstaller -D -w -F demo_myqr.py  --name=CreateQR
    """
    app = App()
