As the name suggests this project is intended to 'automatically rename' files. 

More often than not, we download torrents which contain file names in a very abrupt fashion,
there are irritating periods in between and the episode names are almost always missing. 

What this project would do is that it will take files names with formats such as S11E04.X264.HDTV.KILLERS and convert them to a much simpler format such as S11E04 THE SNUKE.

To do that I first scrape the names from Wikipedia which has very consistent entries for list of episodes for any show using BeautifulSoup and then rename them by using REGEX for pattern matching to verify episode name and it's format and finally OS library to rename the system files accordingly.