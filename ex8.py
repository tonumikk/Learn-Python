# define a variable that is a set of variables of any kind
formatter = "%r %r %r %r"

# print formatter and insert number into variables
print formatter % (1, 2, 3, 4)
# print formatter and insert words into variables
print formatter % ("one", "two", "three", "four")
# print formatter and insert True or False into variables
print formatter % (True, False, False, True)
# print formatter and insert itselt into variables
print formatter % (formatter, formatter, formatter, formatter)
# print formatter and enter sentences
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)
           
