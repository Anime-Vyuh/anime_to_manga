import cv2
import tkinter as tk
from tkinter import filedialog,messagebox

def anime_img():
    global img_file;
    img = filedialog.askopenfile()
    img_file = cv2.imread(img.name)

def manga_img():
    convert = cv2.cvtColor(img_file,cv2.COLOR_RGB2GRAY)
    inverted_img = 255 - convert
    blur_img = cv2.GaussianBlur(inverted_img,(25,25),0)
    final_inversion  = 255 - blur_img
    sketch_img = cv2.divide(convert,final_inversion,scale=255.0)
    cv2.imwrite("manga_enhanced_image.png",sketch_img)
    messagebox.showinfo("Success","File saved")

def main():
    root = tk.Tk()
    root.geometry("425x425+450+180")
    root.title("Anime to Manga")
    canva = tk.Canvas(root,bg="black",bd=5)
    canva.place(x=0,y=0,width=430,height=430)
    root.minsize(425,425)
    root.maxsize(425,425)
    head = tk.Label(root,text="Mina-san Konnichiwa",font=("arial",20,"bold"),fg="black",bg="grey")
    head.place(x=85,y=15)
    frame = tk.LabelFrame(root,bg="gray").place(x=50,y=90,width=330,height=280)
    select = tk.Label(frame,text="Select an Anime Picture",font=("arial",15,"bold"),fg="white",bg="black").place(x=110,y=120)
    convert = tk.Label(frame,text="Download img as Manga",font=("arial",15,"bold"),bg="white",fg="black").place(x=110,y=235)

    anime = tk.Button(frame,text="Choose Anime Picture",bg="blue",fg="white",bd=5,command=anime_img)
    anime.place(x=130,y=160,width=180,height=50)

    manga = tk.Button(frame,text="Image To Manga form",bg="blue",fg="white",bd=5,command=manga_img)
    manga.place(x=130,y=285,width=180,height=50)
    root.mainloop()

if __name__ == '__main__':
    main()
    