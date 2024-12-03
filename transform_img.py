import os
from PIL import Image
import re
import re

def convert_images_to_webp(source_dir, target_dir):
    for root, _, files in os.walk(source_dir):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                img_path = os.path.join(root, file)
                img = Image.open(img_path)
                webp_path = os.path.join(target_dir, os.path.relpath(root, source_dir), f"{os.path.splitext(file)[0]}@{img.width}x{img.height}.webp")
                os.makedirs(os.path.dirname(webp_path), exist_ok=True)
                img.save(webp_path, 'webp')
                yield img_path, webp_path

def update_md_files(md_dir, img_mappings):
    for root, _, files in os.walk(md_dir):
        for file in files:
            if file.lower().endswith('.md'):
                md_path = os.path.join(root, file)
                with open(md_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                for old_path, new_path in img_mappings.items():
                    content = re.sub(re.escape(old_path), new_path, content)
                with open(md_path, 'w', encoding='utf-8') as f:
                    f.write(content)

def main():
    source_images_dir = 'source/images'
    target_images_dir = 'source/images'
    md_files_dir = 'source/_posts'

    img_mappings = {}
    for old_path, new_path in convert_images_to_webp(source_images_dir, target_images_dir):
        img_mappings[old_path] = new_path

    update_md_files(md_files_dir, img_mappings)

if __name__ == '__main__':
    main()