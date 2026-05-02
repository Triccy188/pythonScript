import os
from builder import create_project


if __name__ == "__main__":
    project_name = input("Enter the name for your new project: ")
    base_path = os.path.join(os.getcwd(), project_name)
    create_project(base_path)
    print(f"Project '{project_name}' created successfully at {base_path}")
    print("Folders created: app/api, app/core, app/model, repositories, schemas, services")
    print("Files populated with standard boilerplate code.")
