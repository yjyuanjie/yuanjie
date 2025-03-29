a = "boy"
s = "rwerbfsofsfy"

# 检查a中的每个字母是否都在s中出现
result = all(char in s for char in a)

print(result)