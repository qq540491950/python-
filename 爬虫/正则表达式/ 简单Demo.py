import re

content = "Hello 1234567 World_This is a Regex Demo"
print(len(content))
# result = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}', content)
# 贪婪模式
# result = re.match('^He.*(\d+).*Demo$', content)
# 非贪婪模式
result = re.match('^He.*?(\d+).*Demo$', content)
print(result)
print(result.group(1))
print(result.span())
