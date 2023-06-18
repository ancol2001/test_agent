import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2

# global
file_path = ""
image = ""
#image_new = ""

# Ham chon anh
def select_image():
    global file_path  #
    file_path = filedialog.askopenfilename()
    if file_path:
        image_label.config(text="\nĐã chọn: " + file_path + "\n")

# Ham bien doi sang mau xam'
def convert_to_gray():
    global file_path  #
    if file_path:
        global image
        image = cv2.imread(file_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # cv2.imshow("Ảnh Xám", gray_image)
        # cv2.waitKey(0)
        show_images(image)
        print(" Gray : OK\n")

# Phat hien khuon mat
def detect_face():
    global file_path
    # Load the cascade
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    # Read the input image
    image = cv2.imread(file_path)

    # Convert into grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Draw rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
    show_images(image)

# Hien thi hinh anh
# Anh goc
def show_old():
    global file_path
    image = cv2.imread(file_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    print("Hien thi anh goc\n")
    show_images(image)
    

# Ham hien thi  
def show_images(image_befor):
    # Tao cua so doc lap
    window = tk.Toplevel()
    window.title("Opencv")
    
    # Tạo đối tượng Image
    image_befor = Image.fromarray(image_befor)
    
    # Chuyển đổi đối tượng Image sang định dạng hỗ trợ bởi tkinter
    processed_image_tk = ImageTk.PhotoImage(image_befor)
    
    # Hiển thị hình ảnh
    processed_label = tk.Label(window, image=processed_image_tk)
    processed_label.pack(side=tk.RIGHT)
    
    # Chạy vòng lặp chính GUI
    window.mainloop()

# Save image 
def save_image():
    # global file_path
    global image
    save_path = filedialog.asksaveasfilename(defaultextension=".jpg")
    if save_path:
        cv2.imwrite(save_path, image)
        print("Luu anh : OK\n")

# Giao dien chinh
window = tk.Tk()
window.title("AnP Photoshop 2023")
window.geometry("550x250")
window.resizable(False, False)


# Thay đổi logo (tuỳ chọn)
logo_image = Image.open("hihi.png")
logo_image = logo_image.resize((100, 100))
logo_image = ImageTk.PhotoImage(logo_image)
window.iconphoto(True, logo_image)
label = tk.Label(window, text="\nAnPobe Photoshop v1.0\n")
label.pack()

image_label = tk.Label(window, text="Chưa chọn ảnh")
image_label.pack()

select_button = tk.Button(window, text="Chọn ảnh", command=select_image)
select_button.pack(side=tk.LEFT ,padx=10)

button_open = tk.Button(window, text="Mở ảnh chọn", command=show_old)
button_open.pack(side=tk.LEFT,padx=10)

button1 = tk.Button(window, text="Ảnh Xám", command=convert_to_gray)
button1.pack(side=tk.RIGHT,padx=10)

button2 = tk.Button(window, text="Face Detection", command=detect_face)
button2.pack(side=tk.RIGHT,padx=10)

#save
button3 = tk.Button(window, text="Save", command=save_image)
button3.pack(side=tk.BOTTOM, pady=20)

# window.update()
window.mainloop()
