import csv

with open('aidata.csv', 'r', newline="", encoding="utf-8") as file:
    csv_reader = csv.DictReader(file)

    list_of_dicts = []
    for row in csv_reader:
        list_of_dicts.append(row)

    models_analytics = {}
    for row in list_of_dicts:
        model = row['Favorite Model']
        if model not in models_analytics:
            models_analytics[model] = 1
        else:
            models_analytics[model] += 1

    print(models_analytics)

    user_per_usage = []
    for row in list_of_dicts:
        row['Ai Lines'] = int(row['Ai Lines'])
        user_per_usage.append({'name': row['Name'], 'Ai Lines': row['Ai Lines']})

    user_per_usage.sort(key=lambda x: x['Ai Lines'], reverse=True)
    user_per_usage = user_per_usage[0:10]

    print(user_per_usage)