from jinja2 import FileSystemLoader, Environment
import os


class Templater:

    def __init__(self,
                 template_name="console.j2",
                 searchpath=os.path.join(
                     os.path.dirname(os.path.abspath(__file__)), "templates")):
        templateLoader = FileSystemLoader(searchpath)
        self.templateEnv = Environment(loader=templateLoader)
        self.template_name = template_name

    def get_template(self):
        return self.templateEnv.get_template(self.template_name)
