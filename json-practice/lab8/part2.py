import json
input_json_file = 'data/schacon.repos.json'
output_csv_file = 'chacon.csv'

# Reads in json
with open(input_json_file, 'r') as file:
    data = json.load(file)

# Open CSV file
with open(output_csv_file, 'w') as csv_file:
    csv_file.write('name,html_url,updated_at,visibility\n')

    # Limit output to 5 lines
    for repo in data[:5]:
        # Pulls out following 4 fields
        name = repo['name']
        html_url = repo['html_url']
        updated_at = repo['updated_at']
        visibility = repo['visibility']

        # Assemble fields into comma-separated line
        line = f'{name},{html_url},{updated_at},{visibility}\n'

        # Append to chacon.csv
        csv_file.write(line)
