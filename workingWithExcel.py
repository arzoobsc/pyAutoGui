from openpyxl import Workbook

wb = Workbook()

sheet = wb.active
print(sheet.title)

data = [
    ("id", "Name", "Phone Number"),
    ("1795343", "Arzoo Parwez", "9163115554"),
    ("1795343", "Arzoo Parwez", "9163115554")
]
for row in data:
    sheet.append(row)

wb.create_sheet("another_sheet")
sheet2 = wb['another_sheet']
sheet2.append([1, 2, 3])

# sheet.append(["id", "Name", "Phone Number"])
# sheet.append(["1795343", "Arzoo Parwez", "9163115554"])
wb.save("result\\demo.xlsx")
