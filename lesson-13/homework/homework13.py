# 1
from datetime import datetime
birth_date_str = input('Enter your birthdate (YYYY-MM-DD): ')
birth_date = datetime.strptime(birth_date_str, '%Y-%m-%d')
today = datetime.today()
years = today.year - birth_date.year
months = today.month - birth_date.month
days = today.day - birth_date.day
if days < 0:
    months -= 1
    last_month = (today.month - 1) if today.month > 1 else 12
    last_month_days = (datetime(today.year, last_month + 1, 1) - datetime(today.year, last_month, 1)).days
    days += last_month_days

if months < 0:
    years -= 1
    months += 12

print(f'You are {years} years, {months} months, {days} days old.')

# 2
from datetime import datetime, timedelta
birth_date_str = input('Enter your birthdate (YYYY-MM-DD): ')
birth_date = datetime.strptime(birth_date_str, '%Y-%m-%d')
today = datetime.today()
next_birthday = datetime(today.year, birth_date.month, birth_date.day)
if next_birthday < today:
    next_birthday = datetime(today.year + 1, birth_date.month, birth_date.day)

days_remaining = (next_birthday - today).days

print(f'{days_remaining} days left till your birthday.')

# 3
from datetime import datetime, timedelta
current_datetime_str = input('Current date and time (YYYY-MM-DD HH:MM): ')
current_datetime = datetime.strptime(current_datetime_str, "%Y-%m-%d %H:%M")
hours = int(input('How many hours will the meeting last? '))
minutes = int(input('How many minutes will the meeting last? '))
meeting_duration = timedelta(hours=hours, minutes=minutes)
end_datetime = current_datetime + meeting_duration
print(f'The meeting will end at {end_datetime.strftime('%Y-%m-%d %H:%M')}.')

# 4
from datetime import datetime
import pytz
current_datetime_str = input('Enter the date and time (YYYY-MM-DD HH:MM): ')
current_timezone_str = input('Enter your current country timezone (e.g., Asia/Tashkent): ').strip()
target_timezone_str = input('Enter the target timezone (e.g., Asia/Tokyo): ').strip()
current_datetime = datetime.strptime(current_datetime_str, "%Y-%m-%d %H:%M")

try:
    current_timezone = pytz.timezone(current_timezone_str)
    target_timezone = pytz.timezone(target_timezone_str)
    localized_datetime = current_timezone.localize(current_datetime)
    converted_datetime = localized_datetime.astimezone(target_timezone)

    print(f'The time in {target_timezone_str} will be: {converted_datetime.strftime('%Y-%m-%d %H:%M %Z')}')
except Exception as e:
    print('Invalid timezone. Please check the timezone name and try again.')

# 5
import time

seconds = int(input('Enter the number of seconds for the countdown: '))

while seconds > 0:
    print(f'Time left: {seconds} seconds', end='\r')
    time.sleep(1)
    seconds -= 1

print('\nCountdown complete!')

# 6
email = input('Enter your email address: ')

if '@' in email and '.' in email and email.index('@') < email.rindex('.'):
    print('Valid email!')
else:
    print('Invalid email!')

# 7
phone = input('Enter a phone number (998XXXXXXXXX): ').strip()

if phone.startswith("998") and phone.isdigit() and len(phone) == 12:
    formatted_phone = f"+{phone[:3]} {phone[3:5]} {phone[5:8]}-{phone[8:10]}-{phone[10:]}"
    print('Formatted Phone Number:', formatted_phone)
else:
    print('Invalid phone number! Please enter a 12-digit number')

# 8
import re

def is_valid_password(password):
    if len(password) < 8:
        return 'Password must be at least 8 characters.'
    if not re.search(r'[A-Z]', password):
        return 'Password must contain at least one uppercase letter.'
    if not re.search(r'[a-z]', password):
        return 'Password must contain at least one lowercase letter.'
    if not re.search(r'\d', password):
        return 'Password must contain at least one digit.'
    return 'Valid password!'

password = input('Enter your password: ')
print(is_valid_password(password))

# 9
def find_word_occurrences(text, word):
    words = text.split()
    positions = [i + 1 for i, w in enumerate(words) if w.lower() == word.lower()]
    
    if positions:
        print(f"The word '{word}' appears {len(positions)} times at positions: {positions}")
    else:
        print(f"The word '{word}' was not found in the text.")

text = input('Enter a text: ')
word = input('Enter the word you want to find: ')

print('-' * 50)
find_word_occurrences(text, word)

# 10
import re

def extract_dates(text):
    pattern = r'\b\d{2}[./-]\d{2}[./-]\d{4}\b' 
    dates = re.findall(pattern, text)
    
    if dates:
        print('Found dates:', dates)
    else:
        print('No dates found in the text.')

text = input('Enter a text: ')
print("-" * 50)
extract_dates(text)
