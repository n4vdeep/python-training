rate = 0.97
dollar = float(input("How many dollars have you got? "))

msg = "The amount in Euros is: "
euros = rate * dollar
print(f"{msg} €{str(euros)}")

ranking = ['John', 'Sen', 'Marry']
rank_num = int(input("Enter rank number: "))
rank_num = rank_num - 1
print(ranking[rank_num])

ranking = ['John', 'Sen', 'Marry']
name = input("Enter player name for position: ")
index = ranking.index(name) + 1
print(index)