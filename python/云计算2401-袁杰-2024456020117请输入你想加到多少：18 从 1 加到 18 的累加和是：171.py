# 使用 while 循环实现累加计算器
def sum_with_while(n):
    total = 0
    i = 1
    while i <= n:
        total += i
        i += 1
    return total

# 使用 for 循环实现累加计算器
def sum_with_for(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

# 主程序
if __name__ == "__main__":
    # 获取用户输入
    num = int(input("请输入你想加到多少："))

    # 使用 while 循环计算累加和
    result_while = sum_with_while(num)
    print(f"使用 while 循环：从 1 加到 {num} 的累加和是：{result_while}")

    # 使用 for 循环计算累加和
    result_for = sum_with_for(num)
    print(f"使用 for 循环：从 1 加到 {num} 的累加和是：{result_for}")