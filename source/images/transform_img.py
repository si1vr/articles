import os
from PIL import Image

def convert_images_to_webp(source_folder):
    for root, _, files in os.walk(source_folder):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
                file_path = os.path.join(root, file)
                img = Image.open(file_path)
                webp_file_name = f"{os.path.splitext(file)[0]}@{img.width}x{img.height}.webp"
                webp_file_path = os.path.join(root, webp_file_name)
                img.save(webp_file_path, 'webp')
                print(f"Converted {file_path} to {webp_file_path}")

def replace_image_paths_in_md(md_folder, source_folder):
    for root, _, files in os.walk(md_folder):
        for file in files:
            if file.lower().endswith('.md'):
                md_file_path = os.path.join(root, file)
                with open(md_file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                for img_file in os.listdir(source_folder):
                    if img_file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
                        original_file_name = os.path.splitext(img_file)[0]
                        img = Image.open(os.path.join(source_folder, img_file))
                        webp_file_name = f"{original_file_name}@{img.width}x{img.height}.webp"
                        content = content.replace(img_file, webp_file_name)
                with open(md_file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"Updated image paths in {md_file_path}")

if __name__ == "__main__":
    source_folder = "./"  # 当前文件夹
    md_folder = "./../"  # 上一级文件夹
    convert_images_to_webp(source_folder)
    replace_image_paths_in_md(md_folder, source_folder)