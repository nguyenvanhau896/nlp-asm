file_name = ["p2-q-1.txt", "p2-q-2.txt", "p2-q-3.txt",
             "p2-q-4.txt", "p2-q-5.txt"]

def write_file(file_index, content):
    path = "../output/" + file_name[file_index]
    with open(path, "w") as f:
        f.write(content)  
    return path