total = float(input("Total: "))
tip_percent = float(input("Tip %: "))
people = int(input("People: "))

each_person_pays = total * (1 + (tip_percent / 100)) / people

print(f"Each person pays: {each_person_pays:.2f}")
