# for types in typeofclasses:
#     for classlist in classlists:
#         for type in types:
#             if type in classlist:
#                 for file, val in allvalidwordscounts_test[classlist].items():
#                     multinomresult[file] = {'positive': 0, 'negative': 0, 'truthful': 0, 'deceptive': 0}
#                     for word, count in file[val]:  # not done yet
#                         multinomresult[file][type] += (
#                                 math.log(allvalidwordscounts_train[classlist][file][word] + 1) / allwordsnum[
#                             classlist] + sizeofdict * val)
#                 multinomresult += math.log(priorsNC[key] / sizeofall)

# use this file to learn naive-bayes classifier
# Expected: generate nbmodel.txt

# import sys


# if __name__ == "main":
#    model_file = "nbmodel.txt"
#    input_path = str(sys.argv[0])

# withnum = re.compile(r'\d+')
