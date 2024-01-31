import re

path = r"D:\Projects\start_python\modul_4\modul_4\cats.txt"

def get_cats_info(path):
    try:
        with open(path, 'r', encoding='UTF-8') as cats:
            list_cats=[]
            read_cats = cats.readlines()

            for cat in read_cats:
                divide_into_parts= cat.strip().split(',')
                cat_id, cat_name, cat_age = divide_into_parts
                cats_info={"id": cat_id, "name": cat_name, "age": cat_age}
                list_cats.append(cats_info)

    except Exception as e:
        print(f"Error: {e}")
    return list_cats

cats_info = get_cats_info(path)
print(cats_info)