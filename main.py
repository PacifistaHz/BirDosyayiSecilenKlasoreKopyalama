import os
import shutil

klasorYolu = r"C:/Users/hzgra/PycharmProjects/WriteOdd/pythonProject"

print("Klasörün önceki hali: ", os.listdir(klasorYolu))
shutil.copyfile(r"C:/Users/hzgra/PycharmProjects/WriteOdd/pythonProject/test.txt",
                r"C:/Users/hzgra/PycharmProjects/WriteOdd/pythonProject/test2.txt")
print("Klasörün sonraki hali: ",os.listdir(klasorYolu))

print("Klasörün taşınma önceki haki: ", os.listdir(r"C:/Users/hzgra/PycharmProjects/WriteOdd/pythonProject/.venv"))
shutil.move(r"C:/Users/hzgra/PycharmProjects/WriteOdd/pythonProject/test.txt",
            r"C:/Users/hzgra/PycharmProjects/WriteOdd/pythonProject/.venv/test.txt")
print("Klasörün taşınma sonraki hali: ",os.listdir(r"C:/Users/hzgra/PycharmProjects/WriteOdd/pythonProject/.venv"))

print("Klasörün taşınma önceki hali: ", os.listdir(r"C:/Users/hzgra/PycharmProjects/WriteOdd/pythonProject/.venv"))
shutil.move(r"C:/Users/hzgra/PycharmProjects/WriteOdd/pythonProject/testKlasoru", r"C:/Users/hzgra/PycharmProjects/WriteOdd/pythonProject/.venv")
print("Klasörün taşınma sonraki hali: ",os.listdir(r"C:/Users/hzgra/PycharmProjects/WriteOdd/pythonProject/.venv"))