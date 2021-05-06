import utils
import sorts

bookshelf = utils.load_books('books_small.csv')
for i in bookshelf:
  print(i['title'])
print(ord("a"), ord(" "), ord("A"))
for i in bookshelf:
  print(i['title_lower'])

def by_title_ascending(book_a, book_b):
  return book_a['title_lower'] > book_b['title_lower']

sort1 = sorts.bubble_sort(bookshelf, by_title_ascending)
for i in bookshelf:
  print(i['title'])