import os
import re

def update_md_files(md_dir, img_dir):
    for root, _, files in os.walk(md_dir):
        for file in files:
            if file.lower().endswith('.md'):
                md_path = os.path.join(root, file)
                with open(md_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                blog_name = os.path.splitext(file)[0]
                blog_img_dir = os.path.join(img_dir, blog_name)
                if not os.path.exists(blog_img_dir):
                    continue

                for img_file in os.listdir(blog_img_dir):
                    if img_file.lower().endswith(('.png', '.jpg', '.jpeg')):
                        base_name, ext = os.path.splitext(img_file)
                        webp_file_pattern = re.escape(base_name) + r'@\d+x\d+\.webp'
                        webp_files = [f for f in os.listdir(blog_img_dir) if re.match(webp_file_pattern, f)]
                        if webp_files:
                            webp_file = webp_files[0]
                            img_pattern = re.escape(img_file)
                            content = re.sub(img_pattern, webp_file, content)

                with open(md_path, 'w', encoding='utf-8') as f:
                    f.write(content)

def main():
    md_files_dir = 'source/_posts'
    img_files_dir = 'source/images/blog'
    update_md_files(md_files_dir, img_files_dir)

if __name__ == '__main__':
    main()