from jinja2 import Environment, FileSystemLoader
import os

# script to compile jinja2 templates into raw html

template_dir = './templates'

env = Environment(loader=FileSystemLoader(template_dir))

compile = [x for x in os.listdir(template_dir) if '_' not in x and x.endswith('.html')]
print(compile)

for file in compile:
    template = env.get_template(file)
    output = template.render()
    with open(file, 'w') as fh:
        fh.write(output)