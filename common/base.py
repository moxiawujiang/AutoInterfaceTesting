import os

def get_project_path():
    project_path=os.path.dirname(os.path.dirname(__file__))
    return project_path
