from argparse import ArgumentParser
# from library_xmlrpc import LibraryAPI
from library_odoorpc import LibraryAPI

parser = ArgumentParser()
parser.add_argument(
    "command",
    choices=["list", "add", "set", "del"])
parser.add_argument("params", nargs="*")  # 可选参数
args = parser.parse_args()

host, port, db = "localhost", 8069, "odoo-dev"
user, pwd = "admin", "admin"
api = LibraryAPI(host, port, db, user, pwd)


if args.command == "list":
    title = args.params[:1]
    if len(title) != 0:
        title = title[0]
    books = api.search_read(title)
    for book in books:
        print("%(id)d %(name)s" % book)

if args.command == "add":
    title = args.params[0]
    book_id = api.create(title)
    print("Book added with ID %d for title %s." % (book_id, title))

if args.command == "set":
    if len(args.params) != 2:
        print("set command requires a Title and ID.")
    else:
        book_id, title = int(args.params[0]), args.params[1]
        api.write(book_id, title)
        print("Title of Book ID %d set to %s." % (book_id, title))

if args.command == "del":
    book_id = int(args.params[0])
    api.unlink(book_id)
    print("Book with ID %s was deleted." % book_id)