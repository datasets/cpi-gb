import csv
import requests

lookup = {
    'JAN': '01', 'FEB': '02', 'MAR': '03', 'APR': '04', 'MAY': '05', 'JUN': '06',
    'JUL': '07', 'AUG': '08', 'SEP': '09', 'OCT': '10', 'NOV': '11', 'DEC': '12'
}
url = 'https://www.ons.gov.uk/generator?format=csv&uri=/economy/inflationandpriceindices/timeseries/cdko/mm23'
def download_cache(): 
    response = requests.get(url)
    with open('cache/cpi-uk.csv', mode='w') as file:
        file.write(response.text)

def process():
    skip = False
    annual_data = []
    
    with open('data/cpi-uk-annual.csv', mode='w', newline='') as annual_file:
        with open('data/cpi-uk-monthly.csv', mode='w', newline='') as monthly_file:
            with open('cache/cpi-uk.csv', mode='r') as input_file:
                reader = csv.reader(input_file)
                annual_writer = csv.writer(annual_file)
                monthly_writer = csv.writer(monthly_file)
                
                annual_writer.writerow(['Year', 'Price Index'])
                monthly_writer.writerow(['Date', 'Price Index'])

                for idx, data in enumerate(reader):
                    # Skip first 8 rows
                    if idx < 8:
                        continue
                    elif not data or not data[0] or skip:
                        skip = True
                        continue
                    
                    parts = data[0].split(' ')
                    if len(parts) > 1:
                        data[0] = f"{parts[0]}-{lookup.get(parts[1], '01')}-01"
                        monthly_writer.writerow(data)
                    else:
                        data[0] = parts[0]
                        annual_writer.writerow(data)
                        annual_data.append([int(data[0]), float(data[1])])

    # Compute inflation (CDSI) and save to inflation.csv
    with open('data/inflation-uk.csv', mode='w', newline='') as inflation_file:
        inflation_writer = csv.writer(inflation_file)
        inflation_writer.writerow(['Year', 'CDSI'])
        
        for i in range(1, len(annual_data)):
            year, price_index = annual_data[i]
            prev_price_index = annual_data[i - 1][1]
            cds = ((price_index - prev_price_index) / prev_price_index) * 100
            inflation_writer.writerow([year, round(cds, 1)])

process()
