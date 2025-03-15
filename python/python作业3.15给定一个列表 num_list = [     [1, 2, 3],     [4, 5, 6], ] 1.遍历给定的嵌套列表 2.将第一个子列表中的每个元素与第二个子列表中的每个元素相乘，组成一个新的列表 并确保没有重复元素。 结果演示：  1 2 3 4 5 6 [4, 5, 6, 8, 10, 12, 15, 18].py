num_list = [
    [1, 2, 3],
    [4, 5, 6],
]

# 使用集合来存储结果，确保没有重复元素
result_set = set()

# 遍历第一个子列表
for i in num_list[0]:
    # 遍历第二个子列表
    for j in num_list[1]:
        # 将元素相乘并添加到集合中
        result_set.add(i * j)

# 将集合转换为列表并排序
result_list = sorted(list(result_set))

print(result_list)