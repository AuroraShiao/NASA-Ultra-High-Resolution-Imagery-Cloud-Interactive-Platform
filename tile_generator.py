# tile_generator.py
# Usage:
#   python tile_generator.py input.tif --out tiles_output
#
# 這個程式會：
# 1) 優先使用 libvips 的 `vips dzsave`（若系統有 vips 指令）來產生 tiles（速度快、記憶體友善）
# 2) 若無 vips，使用 Pillow 產生 DeepZoom style tiles（較慢，可能需要較多記憶體）

import os
import sys
import argparse
import shutil
import subprocess
from math import ceil, log2
from PIL import Image
Image.MAX_IMAGE_PIXELS = None  # 解除 Pillow 大圖保護（小心使用）

def has_vips():
    return shutil.which("vips") is not None

def run_vips(input_path, out_dir, basename="image"):
    # vips dzsave input.tif out_dir/image --tile-size 256 --overlap 1 --suffix .jpg[Q=90]
    out_base = os.path.join(out_dir, basename)
    cmd = [
        "vips", "dzsave", input_path, out_base,
        "--tile-size", "256",
        "--overlap", "1",
        "--suffix", ".jpg[Q=90]"
    ]
    print("Running vips:", " ".join(cmd))
    subprocess.check_call(cmd)
    # vips dzsave 會產生 out_dir/image.dzi 與 out_dir/image_files
    print("vips dzsave finished.")

def pil_deepzoom(input_path, out_dir, tile_size=256, overlap=1, format="jpg", quality=90, basename="image"):
    print("Pillow fallback: generating DeepZoom tiles (this can be slow for very large images).")
    os.makedirs(out_dir, exist_ok=True)
    img = Image.open(input_path).convert("RGB")
    width, height = img.size
    max_dim = max(width, height)
    max_level = int(ceil(log2(max_dim)))
    # DeepZoom levels convention: highest_level = max_level, level 0 is smallest (1px)
    levels = list(range(0, max_level+1))
    # We'll create folders: out_dir/{basename}_files/{level}/
    files_dir = os.path.join(out_dir, f"{basename}_files")
    os.makedirs(files_dir, exist_ok=True)
    for level in levels:
        # level_size = ceil(original_size / 2^(max_level - level))
        scale = 2 ** (max_level - level)
        level_w = int(ceil(width / scale))
        level_h = int(ceil(height / scale))
        print(f"Generating level {level} size {level_w}x{level_h} ...")
        # create the resized image for this level:
        level_img = img.resize((level_w, level_h), Image.LANCZOS)
        # cut into tiles
        level_dir = os.path.join(files_dir, str(level))
        os.makedirs(level_dir, exist_ok=True)
        cols = int(ceil(level_w / tile_size))
        rows = int(ceil(level_h / tile_size))
        for r in range(rows):
            for c in range(cols):
                left = c * tile_size
                upper = r * tile_size
                right = min(left + tile_size, level_w)
                lower = min(upper + tile_size, level_h)
                tile = level_img.crop((left, upper, right, lower))
                tile_path = os.path.join(level_dir, f"{c}_{r}.{format}")
                tile.save(tile_path, quality=quality)
        # free memory
        level_img.close()
    img.close()
    # write .dzi XML (DeepZoomImage)
    dzi_path = os.path.join(out_dir, f"{basename}.dzi")
    with open(dzi_path, "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        f.write('<Image TileSize="{}" Overlap="{}" Format="{}" xmlns="http://schemas.microsoft.com/deepzoom/2008">\n'.format(tile_size, overlap, format))
        f.write('  <Size Width="{}" Height="{}"/>\n'.format(width, height))
        f.write('</Image>\n')
    print("Pillow DeepZoom generation finished.")
    print(f"Generated: {dzi_path} and folder {files_dir}")

def main():
    parser = argparse.ArgumentParser(description="Generate DeepZoom tiles from a single image.")
    parser.add_argument("image", help="Input image path (e.g., .tif, .jpg)")
    parser.add_argument("--out", default="tiles_output", help="Output folder (will be created)")
    args = parser.parse_args()
    input_path = args.image
    out_dir = args.out
    basename = "image"

    if not os.path.exists(input_path):
        print("Input not found:", input_path)
        sys.exit(1)
    os.makedirs(out_dir, exist_ok=True)

    if has_vips():
        try:
            run_vips(input_path, out_dir, basename=basename)
            return
        except subprocess.CalledProcessError as e:
            print("vips failed:", e)
            print("Falling back to Pillow implementation.")

    # fallback
    pil_deepzoom(input_path, out_dir, tile_size=256, overlap=1, format="jpg", quality=90, basename=basename)

if __name__ == "__main__":
    main()
