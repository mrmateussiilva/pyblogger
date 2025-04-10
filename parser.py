import markdown
import yaml

def parse_markdown(path):
    with open(path, "r", encoding="utf-8") as f:
        raw = f.read()

    front_matter, content = raw.split('---\n', 2)[1:]
    metadata = yaml.safe_load(front_matter)
    html = markdown.markdown(content)
    metadata["content"] = html
    return metadata
