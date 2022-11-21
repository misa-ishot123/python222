# word1 = input("введение слово(1/2):").lower()
# word2 = input("введение слово(2/2):").lower()
#
# s_w1 = sorted(word1)
# s_w2 = sorted(word2)
# # = запись знчение == сравнение
# if s_w1 == s_w2:
#     print(word1, "and" , word2, "are анаграммами")
#
# else:
#     print(word1, "and", word2, "are not анаграмы")

q1 = input("In what year was the first vid published of orel and reshka?\n"
           "a) 2018, b) 2011, c) 2012, c) 2009\n"
           "--> ").strip().lower()
if q1 == "b":
    print("Correct")
else:
    print("No, incorrect the right answer is B")
    quit()

q2 = input("2 + 2 rovno?\n"
           "a) 4, b) 9, c) 2, c) 7\n"
           "--> ").strip().lower()
if q2 == "a":
    print("Correct")
else:
    print("No, incorrect")
    quit()

q3 = input("how many cookies can misa eat??\n"
           "a) Everything, b) depends from who, c) 5 , d) no i'm not eating that)\n"
           "--> ").strip().lower()
if q3 == "b":
    print("Correct")
else:
    print("No, incorrect")
    quit()


