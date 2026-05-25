import csv
import pprint

def read_csv_file():
    try:
        with open('aidata.csv', 'r', newline="", encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                yield row
    except Exception as e:
        print(f"Failed to read file {e}")

def filter_row(rows):
    for row in rows:
        if 'claude-opus-4-7-thinking' in row['Favorite Model'].lower():
            yield row

def transform_to_integers(rows):
    for row in rows:
        yield {
            'email': row['Email'],
            'name': row['Name'],
            'agent_lines': int(row['Agent Lines']),
            'tab_lines': int(row['Tab Lines']),
            'ai_lines': int(row['Ai Lines']),
            'model': row['Favorite Model']
        }

def calculate_usage_per_user(rows):
    user_summary = {}

    for row in rows:
        name = row['name']

        if name not in user_summary:
            user_summary[name] = {
                'email': row['email'],
                'model_used': row['model'],
                'total_agent_lines': 0,
                'total_tab_lines': 0,
                'total_ai_lines': 0
            }
    
            user_summary[name]['total_agent_lines'] += row['agent_lines']
            user_summary[name]['total_tab_lines'] += row['tab_lines']
            user_summary[name]['total_ai_lines'] += row['ai_lines']

            total_ai = user_summary[name]['total_ai_lines']
            agent_lines = user_summary[name]['total_agent_lines']
            tab_lines = user_summary[name]['total_tab_lines']
            
            user_summary[name]['agent_percentage'] = round((agent_lines / total_ai) * 100, 2) if total_ai > 0 else 0
            user_summary[name]['tab_percentage'] = round((tab_lines / total_ai) * 100, 2) if total_ai > 0 else 0

    return user_summary


raw_rows = read_csv_file()
filtered_rows = filter_row(raw_rows)
transformed_rows = transform_to_integers(filtered_rows)
final_usage_report = calculate_usage_per_user(transformed_rows)

pprint.pprint(final_usage_report)