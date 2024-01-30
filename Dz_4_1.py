import re

path = r"D:\Projects\start_python\modul_4\modul_4\employee_salary.txt"

def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as ys:
            read_ys = ys.read()
            pattern = r"\b\d+\b"
            find_only_num = re.findall(pattern, read_ys)
            find_complet_num = [int(num) for num in find_only_num]
            total = sum(find_complet_num)
            average = total / len(find_complet_num) # ділення з залишком свідомо залишив
            print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
    except Exception as e:
        print(f"Error{e}")

total_salary(path)