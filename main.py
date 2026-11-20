import os
import shutil

# News image entry (Python 3.13, standard library only): the image is
# entry.png beside this file; the program copies it to /output/entry.png.
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
dst = os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.png")
os.makedirs(os.path.dirname(dst), exist_ok=True)
shutil.copyfile(src, dst)
