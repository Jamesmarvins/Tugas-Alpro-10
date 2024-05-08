def count_emails_custom(filename_custom):
    email_counts_custom = {}
    with open(filename_custom, 'r') as file_custom:
        for line_custom in file_custom:
            if line_custom.startswith('From:'):
                email_custom = line_custom.split()[1]
                email_counts_custom[email_custom] = email_counts_custom.get(email_custom, 0) + 1
    return email_counts_custom

filename_input = input("Masukkan nama file: ")
email_counts_result = count_emails_custom(filename_input)
print(email_counts_result)