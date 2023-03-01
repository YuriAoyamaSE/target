data = {'SP': 67836.43,
        'RJ': 36678.66,
        'MG': 29229.88,
        'ES': 27165.48,
        'Outros': 19849.53}


def calculate_percentage(data: dict) -> dict:
    amount = sum(data.values())

    for state, value in data.items():
        data[state] = value/amount

    return data


"""Simple print for report"""
percentage = calculate_percentage(data)
for state, value in percentage.items():
    print(f"{state}: {round(value*100,2)} %")
