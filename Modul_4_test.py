# # r'D:\Projects\start_python\modul_4\modul_4\test.txt'
# with open('raw_data.bin', 'wb') as fh:
#     fh.write(b'Hello world!')

# Перетворення списку чисел у байт-рядок
# numbers = [0, 128, 255]
# byte_numbers = bytes(numbers)
# print(byte_numbers)  # Виведе байтове представлення чисел

from pathlib import Path

p = Path("example.txt")
p.write_text("Hello, world!")
print(p.read_text()) 
print("Exists:", p.exists()) 