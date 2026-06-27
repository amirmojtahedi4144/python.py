import re
def check_email_coolness(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.fullmatch(email_regex, email):
        print(f"ایمیل '{email}' تایید شد!ایمیل شما ساخته شد!")
        return
    else:
        print(f"اوه اوه! ایمیل '{email}' یه خورده قاطی پاتیه. دوباره امتحان کن!")
        return
check_email_coolness("super.star@coolmail.com")
check_email_coolness("john.doe123@company.net")
check_email_coolness("not-an-email")
check_email_coolness("another@domain.co.uk")
check_email_coolness("hmm@bad.c")