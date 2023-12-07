from PIL import Image

from pixelmatch.contrib.PIL import pixelmatch
img_a = Image.open(r"D:\MyGraduate\code\diffusion_shapely_value\images\origin_imgs\mona_lisa_resize.png")

img_b = Image.open(r"D:\MyGraduate\code\diffusion_shapely_value\images\generate_imgs\first_images\g5.png")
print(img_a.size, img_b.size)
img_diff = Image.new("RGBA", img_a.size)

# note how there is no need to specify dimensions
mismatch = pixelmatch(img_a, img_b, img_diff, includeAA=True)

img_diff.save(r"D:\MyGraduate\code\diffusion_shapely_value\result\pixel_difference\diff15.png")