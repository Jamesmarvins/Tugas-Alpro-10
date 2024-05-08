def count_email_domains_custom(filename_custom):
    email_domains_custom = {}
    with open(filename_custom, 'r') as file_custom:
        for line_custom in file_custom:
            if line_custom.startswith('From '):
                email_custom = line_custom.split()[1]
                domain_custom = email_custom.split('@')[1]
                email_domains_custom[domain_custom] = email_domains_custom.get(domain_custom, 0) + 1
    return email_domains_custom

filename_input = input("Masukkan nama file: ")
result_custom = count_email_domains_custom(filename_input)
print(result_custom)