class GetAndPrint(object):
    def __init__(self):
        self.x = ""
    def get_string(self):
        print("请输入字符串")
        self.x = input()
    def print_string(self):
        print(self.x.upper())

gap = GetAndPrint()
gap.get_string()
gap.print_string()
