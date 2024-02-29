#!/usr/bin/env python3

import csv
import re

def contains_domain(address, domain):
    """
    The function takes address and domain as parameters, 
    and its primary objective is to check whether an email address belongs to the old domain(abc.edu).

    To do this, we will use a regular expression stored in the variable named domain_pattern. 
    This variable will now match email addresses of a particular domain. 
    If the old domain is found, then the function returns true.
    """

    domain_pattern = r'[\w\.-]+@'+domain+'$'
    if re.match(domain_pattern, address):
        return True
    return False

def replace_domain(address, old_domain, new_domain):
    """
    The replace_domain function takes in one email address at a time, 
    as well as the email's old domain name and its new domain name. 
    This function's primary objective is to replace the email addresses containing the old domain name with new domain name.

    In order to replace the domain name, we will use the regular expression module 
    and make a pattern that identifies sub-strings containing the old domain name within email addresses. 
    We will then store this pattern in a variable called old_domain_pattern. Next, 
    we will use substitution function sub() from re module to replace the old domain name with the new one 
    and return the updated email address.
    """

    old_domain_pattern = r'' + old_domain + '$'
    address = re.sub(old_domain_pattern, new_domain, address)
    return address


"""
we're going to call the above defined functions: contains_domain() and replace_domain from the main(). 
This will allow us to find the old domain email address, replace it with the newer one, 
and write the updated list to a CSV file in the data directory.

In the previous sections, you might have seen variables named old_domain and new_domain, 
which are passed as parameters to the functions. Let's declare them here within main().
"""

def main():
    old_domain, new_domain = 'abc.edu', 'xyz.edu'
    csv_file_location = '<csv-file-location>'
    report_file =  '<data-directory>' + '/updated_user_emails.csv'
    user_email_list = []
    old_domain_email_list = []
    new_domain_email_list = []

    with open(csv_file_location, 'r') as f:
        user_data_list = list(csv.reader(f))
        user_email_list = [data[1].strip() for data in user_data_list[1:]]

    for email_address in user_email_list:
        if contains_domain(email_address, old_domain):
            old_domain_email_list.append(email_address)
            replaced_email = replace_domain(email_address, old_domain, new_domain)
            new_domain_email_list.append(replaced_email)

    email_key = ' ' + 'Email Address'
    email_index = user_data_list[0].index(email_key)

    for user in user_data_list[1:]:
        for old_domain, new_domain in zip(old_domain_email_list, new_domain_email_list):
            if user[email_index] == ' ' + old_domain:
                user[email_index] = ' ' + new_domain
        f.close()

    with open(report_file, 'w+') as output_file:
        writer = csv.writer(output_file)
        writer.writerows(user_data_list)
        output_file.close()

main()