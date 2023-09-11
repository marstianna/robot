import os

if __name__ == "__main__":
    join = os.path.join(os.path.join("/home/admin/model/downloads/chatGLM2-6", ""), "tokenizer_config.json")
    print(join)
    print(os.listdir(join))