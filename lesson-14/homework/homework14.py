# 1
import json
with open('students.json', 'r') as file:
    data = json.load(file)

for student in data:
    print('Name:', student['name'])
    print('Age:', student['age'])
    print('Grade:', student['grade'])
    print('-' * 20)

# 3
import json

FILE_NAME = 'books.json'

def load_books():
    try:
        with open(FILE_NAME, 'r', encoding='utf-8') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_books(books):
    with open(FILE_NAME, 'w', encoding='utf-8') as file:
        json.dump(books, file, indent=4)

def add_book():
    title = input('Enter the book title: ')
    author = input("Enter the author's name: ")
    year = input('Enter the publication year: ')

    books = load_books()
    books.append({'title': title, 'author': author, 'year': year})
    save_books(books)
    print('Book added successfully!')

def list_books():
    books = load_books()
    if books:
        print('\n Book Collection')
        for index, book in enumerate(books, 1):
            print(f"{index}. {book['title']} - {book['author']} ({book['year']})")
    else:
        print('\nNo books found!')


def main():
    while True:
        print('\nBook Database')
        print('1. Add a new book')
        print('2. View all books')
        print('3. Exit the program')
        
        choice = input('Choose an option (1/2/3): ')

        if choice == '1':
            add_book()
        elif choice == '2':
            list_books()
        elif choice == '3':
            print('Exiting the program.')
            break
        else:
            print('Invalid option! Please choose 1, 2, or 3.')

main()

# 4
