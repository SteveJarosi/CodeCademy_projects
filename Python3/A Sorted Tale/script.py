import utils
import sorts

bookshelf = utils.load_books('books_small.csv')
for i in bookshelf:
    print(f'Title: {i["title"]}\nAuthor: {i["author"]}')
print(ord("a"), ord(" "), ord("A"))
for i in bookshelf:
    print(i['title_lower'])
print()


def by_title_ascending(book_a, book_b):
    return book_a['title_lower'] > book_b['title_lower']


sort1 = sorts.bubble_sort(bookshelf, by_title_ascending)
for i in bookshelf:
    print(f'Title: {i["title"]}\nAuthor: {i["author"]}')
print()


def by_author_ascending(book_a, book_b):
    return book_a['author_lower'] > book_b['author_lower']


bookshelf_v1 = bookshelf[:]
# or bookshelf_v1 = bookshelf.copy()

sort2 = sorts.bubble_sort(bookshelf, by_author_ascending)
for i in bookshelf:
    print(f'Title: {i["title"]}\nAuthor: {i["author"]}')

bookshelf_v2 = bookshelf[:]
sorts.quicksort(bookshelf_v2, by_author_ascending)
print()
for i in bookshelf:
    print(f'Title: {i["title"]}\nAuthor: {i["author"]}')


def by_total_length(book_a, book_b):
    return (len(book_a['author'])+len(book_a['title'])) > (len(book_b['author'])+len(book_b['title']))


long_bookshelf = utils.load_books('books_large.csv')
print()
sort3 = sorts.bubble_sort(bookshelf, by_total_length)

for i in bookshelf:
    print(f'Title: {i["title"]}\nAuthor: {i["author"]}')
print()
# sort4 = sorts.bubble_sort(long_bookshelf, by_total_length)
sorts.quicksort(long_bookshelf, by_total_length)
for i in long_bookshelf:
    print(
        f'Title: {i["title"]}\nAuthor: {i["author"]} Length: {len(i["author"])+len(i["title"])}')
print()
