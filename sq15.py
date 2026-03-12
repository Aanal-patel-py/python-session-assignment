class FileManager:
    def __init__(self,*filenames,mode='r+'):
        self.filenames=filenames
        self.mode=mode
        self.files={}

    def __enter__(self):
        for f in self.filenames:
            print(f)
            try:
                self.files[f]=open(f,self.mode)
            except FileNotFoundError:
                print(f"{f} file not found")
        print(self.files.values())
        return self

        
    def __exit__(self, exc_type, exc, tb):
        for f in self.files.values():
            f.close()

    def read_line(self,filename):
        return self.files[filename].readline()

    def write_line(self,filename,content):
        self.files[filename].write(content)

    def copy_content(self,src,des):
        x= self.files[src].read()
        self.files[des].write(x)

with FileManager("file1.txt","file2.txt","file3.txt") as files: #here file is the object 
    # files.files["file1.txt"].write("abc")
    # x=files.files["file2.txt"].read()
    # print(x)
    # z=files.read_line("file1.txt")
    # print(z)
    # files.write_line("file1.txt","xyz")

    files.copy_content("file1.txt","file2.txt")
