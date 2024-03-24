import os, random, shutil


def moveimg(fileDir, tarDir):
    pathDir = os.listdir(fileDir)  # 原始路径
    filenumber = len(pathDir)
    rate = 0.8  # 抽取图片的比例
    picknumber = int(filenumber * rate)  # 按照rate比例从文件夹中取一定数量图片
    sample = random.sample(pathDir, picknumber)  # 随机选取picknumber数量的样本图片
    print(sample)
    for name in sample:
        shutil.move(fileDir + name, tarDir + "\\" + name)
    return


def movelabel(file_list, file_label_train, file_label_val):
    for i in file_list:
        if i.endswith('.jpg'):
            filename = file_label_train + "\\" + i[:-4] + '.txt'
            if os.path.exists(filename):
                shutil.move(filename, file_label_val)
                print(i + "处理成功！")


if __name__ == '__main__':
    fileDir = r"D:\12045\PycharmProjects\yolov5-5.0\yolov5-5.0\DataSet\Images" + "\\"  # 源图片文件夹路径
    tarDir = r'D:\12045\PycharmProjects\yolov5-5.0\yolov5-5.0\DataSet\train_image'  # 图片移动到新的文件夹路径
    moveimg(fileDir, tarDir)
    file_list = os.listdir(tarDir)
    file_label_train = r"D:\12045\PycharmProjects\yolov5-5.0\yolov5-5.0\DataSet\Label"  # 源图片标签路径
    file_label_val = r"D:\12045\PycharmProjects\yolov5-5.0\yolov5-5.0\DataSet\train_label"  # 标签
    # 移动到新的文件路径
    movelabel(file_list, file_label_train, file_label_val)