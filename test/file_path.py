import os

if __name__ == "__main__":
    path_or_repo_id = str("/home/admin/model/downloads/chatGLM2-6B")
    full_filename = os.path.join("", "config.json")
    if os.path.isdir(path_or_repo_id):
        resolved_file = os.path.join(os.path.join(path_or_repo_id, ""), "config.json")
        print(resolved_file)
        listdir = os.listdir(resolved_file)
        if not os.path.isfile(resolved_file):
            print("not exist")