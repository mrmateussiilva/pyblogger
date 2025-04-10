import os
from .parser import parse_markdown
from .template_engine import render_template
from .utils import copy_static

def build_site(content_dir, template_dir, output_dir, static_dir):
    os.makedirs(output_dir, exist_ok=True)

    for filename in os.listdir(content_dir):
        if filename.endswith(".md"):
            post_data = parse_markdown(os.path.join(content_dir, filename))
            html = render_template(template_dir, "post.html", post_data)

            out_path = os.path.join(output_dir, filename.replace(".md", ".html"))
            with open(out_path, "w", encoding="utf-8") as f:
                f.write(html)

    copy_static(static_dir, output_dir)
