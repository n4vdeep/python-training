filenames = ["1.Raw data.txt", "2.Reports.txt", "3.Presentations.txt"]

for filename in filenames:
    filename = filename.replace(".", "-", 1)
    print(filename)

new_files = ("1.Raw data.txt", "2.Reports.txt", "3.Presentations.txt")
x = new_files.index('2.Reports.txt')
print(x)
