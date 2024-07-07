# task 1 

import re  

# user emails in a string 
user_emails = "Emails: user1@domain.com, user2@exclude.com, user3@domain.com"

#function to read the string and determine all containing variable wrong_domain 
def find_to_exclude(wrong_domain, user_emails):
    delete_pattern = rf"\b[A-Za-z0-9._%+-]+@{re.escape(wrong_domain)}\b"
    find_and_delete = re.findall(delete_pattern, user_emails)
    return find_and_delete

#function revieces a list of emails and puts the doamins in a list, the function calls for a 
# to the other function and then deletes emails using for loop, prints results 
def return_new_list(user_emails):
    wrong_domain = "exclude.com"
    all_domains = re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", user_emails)
    delete_domains = find_to_exclude(wrong_domain, user_emails)
    new_list = [email for email in all_domains if email not in delete_domains]
    print(new_list)


#call the function
return_new_list(user_emails)
