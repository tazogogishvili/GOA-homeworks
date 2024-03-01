
# declaring variables How many books do I want to read?

book_read_target = 20
book_write_target = 10

book_i_readed = int(input("how many book you read: "))
book_i_write = int(input("how many book you write: "))


print(book_read_target >= book_i_readed and book_write_target >= book_i_write)
print(book_read_target == book_i_readed and book_write_target == book_i_write)
print(book_read_target == book_i_readed and book_write_target > book_i_write)
print(book_read_target >= book_i_readed or book_write_target >= book_i_write)


