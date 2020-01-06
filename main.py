import utility

BookInfo = ['0133594149','Computer Networking: A Top-Down Approach','Kurose & Ross,','2016']
BookInfo2 =['9780073529608','Microelectronic Circuit Design ','Jaeger & Blalock','2015']
CSV = 'textbooks.csv'
BookList = utility.parseBookInfo(CSV)
link = utility.search(BookList[0],1)
utility.downloadBook(BookList[0],link)