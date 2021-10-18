# python的文件操作
# 写入
def write_file(filepath, content):
    """
        方法：文件写入
        参数：
            filepath：文件路径
            content：写入的内容
        返回值：None
    """
    with open(file=filepath, mode='w', encoding='utf-8') as f:
        f.write(str(content))

# 读取
def read_file(filepath):
    """
        方法名：文件读取
        参数：
            filepath：文件路径
        返回值：返回值文件的内容，类型为str
    """
    with open(file=filepath, mode='r', encoding='utf-8') as f:
        result = f.readline()

    return result




# 调用文件写入方法
# write_file('./test.txt', "接口自动化测试")

# 调用文件读取方法
# a = read_file('./test.txt')
# print(a)