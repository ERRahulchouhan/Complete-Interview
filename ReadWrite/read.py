import csv

cols = ["Name" , "Age"]
rows = [["Rahul",12],
        ["Sonu" , 43]]

# with open("rahul.csv" , "w") as file:
#     csvwriter =csv.writer(file)
#     csvwriter.writerow(cols)
#     csvwriter.writerows(rows)


with open("rahul.csv" , "w") as file:
        csvwriter =csv.writer(file)
        csvwriter.writerow(cols)
        csvwriter.writerow(rows)