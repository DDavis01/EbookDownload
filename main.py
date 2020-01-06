import utility

BookInfo = ['0133594149','Computer Networking: A Top-Down Approach','Kurose & Ross,','2016']
BookInfo2 =['9780073529608','Microelectronic Circuit Design ','Jaeger & Blalock','2015']
link = utility.search(BookInfo2,1)
utility.downloadBook(BookInfo2,link)