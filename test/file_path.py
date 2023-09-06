import os

if __name__ == "__main__":
    join = os.path.join(os.path.dirname(os.path.dirname(__file__)), "knowledge_base")
    print(join)
    print(os.listdir(join))