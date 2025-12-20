import re

def my_pydash(data, path, default=None):
    if data is None or not path:
        return default

    path = re.sub(r"\[(\d+)\]", r".\1", path)
    path = re.sub(r"\[['\"]([^'\"]+)['\"]\]", r".\1", path)
    print(path)

    keys = [k for k in path.split(".") if k]

    try:
        for key in keys:
            # Convert numeric keys to int for lists
            key = int(key) if key.isdigit() else key
            data = data[key]
        return data

    except (KeyError, IndexError, TypeError):
        return default

item = {
    "data": {
        "value": {
            "product name": "MacBook Pro",
            "prices": [1000, 1200]
        }
    },
    "sections": [
        {
            "trackingData": [
                {"table_name": "orders"}
            ]
        }
    ]
}

print("Value : ",my_pydash(item, "data.value.product name"))
print("Value : ",my_pydash(item, 'data["value"]["product name"]'))
print("Value : ",my_pydash(item, "data.value.prices[1]"))
print("Value : ",my_pydash(item, "sections[0].trackingData[0].table_name"))
print("Value : ",my_pydash(item, "sections[0].trackingData[0].pydash_get_name","Pydash.get()"))

