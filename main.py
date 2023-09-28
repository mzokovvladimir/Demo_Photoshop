import os
# імпортування віджетів
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QLabel, QPushButton, QListWidget, QHBoxLayout, \
    QVBoxLayout, QMessageBox
# потрібна константа Qt.KeepAspectRatio для зміни розмірів із збереженням пропорцій
from PyQt5.QtCore import Qt
# оптимізоване для показу на екрані зображення
from PyQt5.QtGui import QPixmap

from PIL import Image, ImageChops, ImageFont, ImageDraw, ImageFilter
from PIL.ImageQt import ImageQt  # для перевода графики из Pillow в Qt
from PIL.ImageFilter import BLUR, CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE, EMBOSS, FIND_EDGES, SMOOTH, \
    SMOOTH_MORE, SHARPEN, GaussianBlur, UnsharpMask


class ImageProcessor:
    def __init__(self):
        self.image = None
        self.dir = None
        self.filename = None
        self.save_dir = "Modified/"

    def load_image(self, filename: str):
        """ при завантаженні запам'ятовуємо шлях та ім'я файлу """
        self.filename = filename
        fullname = os.path.join(workdir, filename)
        self.image = Image.open(fullname)

    def save_image(self):
        """ зберігає копію файлу у підпапці """
        path = os.path.join(workdir, self.save_dir)
        if not (os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)
        fullname = os.path.join(path, self.filename)

        self.image.save(fullname)

    def __save_show_image(self):
        self.save_image()
        self.show_image(os.path.join(workdir, self.save_dir, self.filename))

    def do_b_w(self):
        self.image = self.image.convert("L")
        self.__save_show_image()
        """self.save_image()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.show_image(image_path)"""

    def turn_left(self):
        self.image = self.image.transpose(Image.ROTATE_90)
        """self.save_image()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.show_image(image_path)"""
        self.__save_show_image()

    def turn_right(self):
        self.image = self.image.transpose(Image.ROTATE_270)
        """self.save_image()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.show_image(image_path)"""
        self.__save_show_image()

    def do_flip(self):
        self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
        """self.save_image()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.show_image(image_path)"""
        self.__save_show_image()

    def do_blur(self):
        self.image = self.image.filter(BLUR)
        """self.save_image()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.show_image(image_path)"""
        self.__save_show_image()

    def do_sharpen(self):
        self.image = self.image.filter(SHARPEN)
        """self.save_image()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.show_image(image_path)"""
        self.__save_show_image()

    def do_contour(self):
        self.image = self.image.filter(CONTOUR)
        """self.save_image()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.show_image(image_path)"""
        self.__save_show_image()

    def do_detail(self):
        self.image = self.image.filter(DETAIL)
        """self.save_image()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.show_image(image_path)"""
        self.__save_show_image()

    def do_edge_enhance(self):
        self.image = self.image.filter(EDGE_ENHANCE)
        """self.save_image()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.show_image(image_path)"""
        self.__save_show_image()

    def do_edge_enhance_more(self):
        self.image = self.image.filter(EDGE_ENHANCE_MORE)
        """self.save_image()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.show_image(image_path)"""
        self.__save_show_image()

    def do_emboss(self):
        self.image = self.image.filter(EMBOSS)
        """self.save_image()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.show_image(image_path)"""
        self.__save_show_image()

    def do_find_edges(self):
        self.image = self.image.filter(FIND_EDGES)
        """self.save_image()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.show_image(image_path)"""
        self.__save_show_image()

    def do_smooth(self):
        self.image = self.image.filter(SMOOTH)
        """self.save_image()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.show_image(image_path)"""
        self.__save_show_image()

    def do_smooth_more(self):
        self.image = self.image.filter(SMOOTH_MORE)
        """self.save_image()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.show_image(image_path)"""
        self.__save_show_image()

    def do_gaussian_blur(self):
        self.image = self.image.filter(GaussianBlur)
        """self.save_image()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.show_image(image_path)"""
        self.__save_show_image()

    def do_unsharp_mask(self):
        self.image = self.image.filter(UnsharpMask)
        """self.save_image()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.show_image(image_path)"""
        self.__save_show_image()

    def show_image(self, path):
        lb_image.hide()
        pixmap_image = QPixmap(path)
        w, h = lb_image.width(), lb_image.height()
        pixmap_image = pixmap_image.scaled(w, h, Qt.KeepAspectRatio)
        lb_image.setPixmap(pixmap_image)
        lb_image.show()


def choose_workdir():
    global workdir
    workdir = QFileDialog.getExistingDirectory()


def show_filenames_list():
    extensions: list[str] = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']
    choose_workdir()
    filenames = filter_image(os.listdir(workdir), extensions)

    lw_files.clear()
    for filename in filenames:
        lw_files.addItem(filename)


def show_сhosen_іmage():
    if lw_files.currentRow() >= 0:
        filename = lw_files.currentItem().text()
        workimage.load_image(filename)
        workimage.show_image(os.path.join(workdir, workimage.filename))


def filter_image(files, extensions: list[str]) -> list[str]:
    """result: list = []
    for filename in files:
        for ext in extensions:
            if filename.endswith(ext):
                result.append(filename)
    return result"""
    return [filename for filename in files for ext in extensions if filename.endswith(ext)]


def show_info():
   my_info = QMessageBox()
   my_info.setText('DemoPhotoshop!\nVer.1.0')
   my_info.exec_()


app = QApplication([])
win = QWidget()
win.resize(1200, 750)
win.setWindowTitle('Demo Photoshop')
lb_image = QLabel("Зображення")
# відцентровуємо надпис
lb_image.setAlignment(Qt.AlignCenter)
btn_dir = QPushButton("Директорія")
lw_files = QListWidget()

# готуємо 1й ряд кнопок
btn_left = QPushButton("Left")
btn_right = QPushButton("Right")
btn_flip = QPushButton("Flip")
btn_sharpen = QPushButton("Sharp")
btn_b_w = QPushButton("B/W")
btn_blur = QPushButton("Blur")
btn_contour = QPushButton("Contour")
btn_detail = QPushButton("Detail")

# готуємо 2й ряд кнопок
btn_edge_enhance = QPushButton("Edge_enhance")
btn_edge_enhance_more = QPushButton("Edge_enhance_more")
btn_emboss = QPushButton("Emboss")
btn_find_edges = QPushButton("Find_edges")
btn_smooth = QPushButton("Smooth")
btn_smooth_more = QPushButton("Smooth_more")
btn_gaussian_blur = QPushButton("Gaussian_Blur")
btn_unsharp_mask = QPushButton("Unsharp_Mask")

btn_info = QPushButton('INFO')

# Основний рядок
row = QHBoxLayout()
# Поділяється на 2 стовпчики
col1 = QVBoxLayout()
col2 = QVBoxLayout()
# у першому - кнопка вибору директорії
col1.addWidget(btn_dir)
# а також - список файлів
col1.addWidget(lw_files)
# у другому - зображення
col2.addWidget(lb_image, 95)
# кнопка з довідковою інформацією
col2.addWidget(btn_info)

# 1й рядок кнопок
row_tools1 = QHBoxLayout()
row_tools1.addWidget(btn_left)
row_tools1.addWidget(btn_right)
row_tools1.addWidget(btn_flip)
row_tools1.addWidget(btn_sharpen)
row_tools1.addWidget(btn_b_w)
row_tools1.addWidget(btn_blur)
row_tools1.addWidget(btn_contour)
row_tools1.addWidget(btn_detail)

# 2й рядок кнопок
row_tools2 = QHBoxLayout()
row_tools2.addWidget(btn_edge_enhance)
row_tools2.addWidget(btn_edge_enhance_more)
row_tools2.addWidget(btn_emboss)
row_tools2.addWidget(btn_find_edges)
row_tools2.addWidget(btn_smooth)
row_tools2.addWidget(btn_smooth_more)
row_tools2.addWidget(btn_gaussian_blur)
row_tools2.addWidget(btn_unsharp_mask)

col2.addLayout(row_tools1)
col2.addLayout(row_tools2)

row.addLayout(col1, 20)
row.addLayout(col2, 80)
win.setLayout(row)

win.show()

btn_dir.clicked.connect(show_filenames_list)

workdir: str = ''
# поточне робоче зображення для роботи
workimage = ImageProcessor()
lw_files.currentRowChanged.connect(show_сhosen_іmage)

btn_b_w.clicked.connect(workimage.do_b_w)
btn_left.clicked.connect(workimage.turn_left)
btn_right.clicked.connect(workimage.turn_right)
btn_sharpen.clicked.connect(workimage.do_sharpen)
btn_flip.clicked.connect(workimage.do_flip)
btn_blur.clicked.connect(workimage.do_blur)
btn_contour.clicked.connect(workimage.do_contour)
btn_detail.clicked.connect(workimage.do_detail)

btn_edge_enhance.clicked.connect(workimage.do_edge_enhance)
btn_edge_enhance_more.clicked.connect(workimage.do_edge_enhance_more)
btn_emboss.clicked.connect(workimage.do_emboss)
btn_find_edges.clicked.connect(workimage.do_find_edges)
btn_smooth.clicked.connect(workimage.do_smooth)
btn_smooth_more.clicked.connect(workimage.do_smooth_more)
btn_gaussian_blur.clicked.connect(workimage.do_gaussian_blur)
btn_unsharp_mask.clicked.connect(workimage.do_unsharp_mask)

btn_info.clicked.connect(show_info)

app.exec_()
