from jinja2 import Environment, FileSystemLoader

def render_template(template_dir, template_name, context):
    env = Environment(loader=FileSystemLoader(template_dir))
    template = env.get_template(template_name)
    return template.render(context)
