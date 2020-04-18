import shutil
import os
import walk


def move(src, dest):
    shutil.copyfile(src, dest)


x = [os.path.join(r, file) for r, d, f in os.walk("C:\\Users\\lopezme\\ganomaly\\rawdata\\") for file in f]
print(x)
abnormal = 0
normal = 0
for file in x:
    if file.find("post_disaster") > 0:
        abnormal = abnormal + 1
        move(file, "C:\\Users\\lopezme\\ganomaly\\experiments\\data\\xbd\\test\\1.abnormal\\abnormal_tst_img_" + str(abnormal) + ".png")
    else:
        normal = normal + 1
        move(file, "C:\\Users\\lopezme\\ganomaly\\experiments\\data\\xbd\\test\\0.normal\\normal_tst_img_" + str(normal) + ".png")
        move(file, "C:\\Users\\lopezme\\ganomaly\\experiments\\data\\xbd\\train\\0.normal\\normal_tst_img_" + str(normal) + ".png")
    print(file)

