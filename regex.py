import re
import csv
from itertools import zip_longest


text = """
Welcome to the corporate portal. For general inquiries, please contact our 
front desk team at office-admin@globaltech.com or call us at +919876543210. 
You can also view our full services list online at ://globaltech.com.

If you are looking for technical assistance, the support desk is open 24/7. 
Reach out to tech.support2026@sub.domain.org or ring the hotline at +916123456789. 
Documentation is hosted securely at https://globaltech.net.

BILLING AND ACCOUNTS:
For invoice issues, mail billing_dept@finance-core.co.in. The direct line 
for the accounts manager is +917778889991. Payments can be submitted directly 
through the main web portal located at http://pay-globaltech.com.

TRICKY STRINGS (Your regex should ignore these based on our previous fixes):
- Do not match standard numbers like 1234567890 or partial codes like +91123.
- An email domain like invalid@com should be skipped.
- The website pattern must NOT pull 'finance-core.co.in' out of the billing email.
- Fake web links like missingdotcom or http://fake should not break things.

Finally, you can reach our international media liaison at press-release@media.globaltech.co 
or dial +918881112223. Check out our public blog entries at ://globaltech.com.
"""

def extract_data(data):
    email_regex = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    phone_regex = r'\+91[1-9]\d{9}'
    url_regex = r'(?<![\w.@])(?:https?://)?(?:www\.)?[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)+'

    email = re.findall(email_regex, data) 
    phone = re.findall(phone_regex, data) 
    website = re.findall(url_regex, data) 
    return {
        'email': email,
        'phone': phone,
        'website': website
    }

# print(extract_data(text))

def save_to_csv(data):
    dict_data = extract_data(data)
    rows = zip_longest(dict_data['email'], dict_data['phone'], dict_data['website'], fillvalue="")
    try:
        with open('text.csv', 'w+', newline="", encoding='utf-8') as file:
            writer = csv.writer(file)

            writer.writerow(['email', 'phone', 'website'])

            writer.writerows(rows)
    except Exception as e:
        print(f"Failed to Write data {e}")

    print("CSV file created successfully")

save_to_csv(text)