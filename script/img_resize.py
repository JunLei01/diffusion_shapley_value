from PIL import Image


def ResizeImage(filein, fileout, scale=1):
    """
    改变图片大小
    :param filein: 输入图片
    :param fileout: 输出图片
    :param width: 输出图片宽度
    :param height: 输出图片宽度
    :param type: 输出图片类型（png, gif, jpeg...）
    :return:
    """
    img = Image.open(filein)
    width = 1024
    height = 1472
    type = img.format
    out = img.resize((width, height), Image.ANTIALIAS)
    # 第二个参数：
    # Image.NEAREST ：低质量
    # Image.BILINEAR：双线性
    # Image.BICUBIC ：三次样条插值
    # Image.ANTIALIAS：高质量
    out.save(fileout, type)


if __name__ == "__main__":
    print("开始运行")
    filein = r'D:\graduate\code\diffusion_shapely_value\images\origin_imgs\mona_lisa.png'
    fileout = r'D:\graduate\code\diffusion_shapely_value\images\origin_imgs\mona_lisa_resize.png'
    ResizeImage(filein, fileout, scale=4)