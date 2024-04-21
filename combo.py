def get_keys(dictionary):
    keys = []
    for key in dictionary.keys():
        keys.append(key)
        if isinstance(dictionary[key], dict):
            sub_keys = get_keys(dictionary[key])
            for sub_key in sub_keys:
                keys.append(f"{key}.{sub_key}")
    return keys

def get_address(dictionary):
    if isinstance(dictionary, dict):
        if "address" in dictionary.keys():
            return dictionary["address"]
        else:
            for key in dictionary.keys():
                address = get_address(dictionary[key])
                if address:
                    return address
    return None

def get_tags(dictionary):
    tags = []
    for key in dictionary.keys():
        if key == "tags":
            tags.extend(dictionary[key])
        elif isinstance(dictionary[key], dict):
            sub_tags = get_tags(dictionary[key])
            tags.extend(sub_tags)
    return tags

# Пример словаря
dictionary = {
    "name": "John Doe",
    "age": 30,
    "address": "123 Main Street",
    "tags": ["Lorem", "ipsum", "dolor"],
    "nested": {
        "title": "Lorem ipsum",
        "content": "Lorem ipsum dolor sit amet",
        "tags": ["consectetur", "adipisicing"]
    }
}

# Получение полных ключей
keys = get_keys(dictionary)
print("Полные ключи:")
for key in keys:
    print(key)

# Получение адреса из первого индекса
address = get_address(dictionary)
print("\nАдрес из первого индекса:")
print(address)

# Получение тегов (подзаголовков) "incididunt"
tags = get_tags(dictionary)
print("\nТеги (подзаголовки) 'incididunt':")
for tag in tags:
    print(tag)
