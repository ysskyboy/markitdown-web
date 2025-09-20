from markitdown import MarkItDown

# 初始化MarkItDown
md = MarkItDown()

# 转换测试文件
try:
    result = md.convert("test_file.txt")
    print("转换成功！")
    print("\n转换结果：")
    print(result.text_content)
except Exception as e:
    print(f"转换失败：{str(e)}")