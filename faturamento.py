# • O menor valor de faturamento ocorrido em um dia do mês;
# • O maior valor de faturamento ocorrido em um dia do mês;
# • Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

import json


def billings(json_file: json) -> dict:
    with open(json_file) as json_data:
        data = json.load(json_data)

    billings = [billing_day['valor']
                for billing_day in data if billing_day['valor'] != 0]

    avg_billing = sum(billings) / len(billings)
    max_billing = max(billings)
    min_billing = min(billings)
    above_avg = [value for value in billings if value > avg_billing]

    return {'min_billing': min_billing,
            'max_billing': max_billing,
            'days_above_avg': len(above_avg)}


report = billings('dados.json')
print(f"""Menor valor de faturamento: {report['min_billing']}
Maior valor de faturamento: {report['max_billing']}
Número de dias com faturamento acima da média: {report['days_above_avg']}""")
