# import re
#
# string = " !лучший, Лучший лучшая лучшее, выражение, выражениям"
# # exp = "1"
# exp = "[лЛ]учш[А-Я|а-я]+"
#
#
# compiled_regex = re.compile(exp)
#
# print(
#     re.findall(compiled_regex, string)
# )
# sale, discount номер 1


# x = "лучш, перв, сам, лидер, флагман, гарант, идеал, идеальн, абсолют, исключитель, совершенн, единственн"

x = "уникальн, оптимальн, бесподобн, непревзойденн, восхитительн, прекрасн"
x = map(str.strip, x.split(","))

x = [f"re.compile('[{word[0].lower()}{word[0].upper()}]{word[1:]}[А-Я|а-я]+')" for word in x]


print(x)