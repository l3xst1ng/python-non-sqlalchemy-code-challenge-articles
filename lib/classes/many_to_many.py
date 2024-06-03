class Article:
    all = []  # Class variable to store all article instances

    def __init__(self, author, magazine, title):
        # Checking if the title is a string and has a length between 5 and 50 characters
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError('Title must be a string between 5 and 50 characters')
        self._title = title
        self.author = author  
        self.magazine = magazine  
        Article.all.append(self)  

    @property
    def title(self):
        return self._title  

    @property
    def author(self):
        return self._author  

    @author.setter
    def author(self, new_author):
        # Checking if the new author is an instance of the Author class
        if isinstance(new_author, Author):
            self._author = new_author
        else:
            raise TypeError("Author must be an instance of Author")

    @property
    def magazine(self):
        return self._magazine  # Getter method for the magazine attribute

    @magazine.setter
    def magazine(self, new_magazine):
        # Checking if the new magazine is an instance of the Magazine class
        if isinstance(new_magazine, Magazine):
            self._magazine = new_magazine
        else:
            raise TypeError("Magazine must be an instance of Magazine")


class Author:
    def __init__(self, name):
        self.name = name  

    @property
    def name(self):
        return self._name  # Getter method for the name attribute

    @name.setter
    def name(self, new_name):
        # Checking if the new name is a non-empty string
        if not isinstance(new_name, str):
            raise TypeError("Name must be a string")
        if len(new_name) == 0:
            raise ValueError("Name must be a non-empty string")
        self._name = new_name

    def articles(self):
        # Return a list of articles written by the author
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        # Return a list of unique magazines the author has contributed to
        return list({article.magazine for article in self.articles()})

    def add_article(self, magazine, title):
        # Create and return a new article associated with the author and magazine
        return Article(self, magazine, title)

    def topic_areas(self):
        # Return a list of unique topic areas (categories) the author has written about
        areas = list({magazine.category for magazine in self.magazines()})
        return areas if areas else None


class Magazine:
    _all = []  # Storing all magazine instances

    def __init__(self, name, category):
        self.name = name  
        self.category = category  
        Magazine._all.append(self)  

    @property
    def name(self):
        return self._name  

    @name.setter
    def name(self, new_name):
        # Check if the new name is a string with a length between 2 and 16 characters
        if isinstance(new_name, str) and 2 <= len(new_name) <= 16:
            self._name = new_name
        else:
            raise ValueError("Name must be a string between 2 and 16 characters")

    @property
    def category(self):
        return self._category  

    @category.setter
    def category(self, new_category):
        # Checking if the new category is a non-empty string
        if isinstance(new_category, str) and len(new_category) > 0:
            self._category = new_category
        else:
            raise ValueError("Category must be a non-empty string")

    def articles(self):
        # Returning a list of articles published in the magazine
        article_list = []
        for article in Article.all:
            if article.magazine == self:
                article_list.append(article)
        return article_list

    def contributors(self):
        # Returning a list of unique authors who have contributed to the magazine
        author_set = set()
        for article in self.articles():
            author_set.add(article.author)
        return list(author_set)

    def article_titles(self):
        # Returning a list of titles of articles published in the magazine
        titles = [] # storing the titles of all the articles published in the magazine 
        for article in self.articles():
            titles.append(article.title)
        return titles if titles else None

    def contributing_authors(self):
        # Returning a list of authors who have written more than 2 articles for the magazine
        author_counts = {}
        for article in self.articles():
            author = article.author
            if author in author_counts:
                author_counts[author] += 1
            else:
                author_counts[author] = 1

        contributing_authors = []
        for author, count in author_counts.items():
            if count > 2:
                contributing_authors.append(author)
        return contributing_authors if contributing_authors else None

    @classmethod
    def top_publisher(cls):
        # Returning the magazine with the most published articles
        if not cls._all:
            return None
        
        top_magazine = None
        max_articles = 0
        for magazine in cls._all:
            article_count = len(magazine.articles())
            if article_count > max_articles:
                top_magazine = magazine
                max_articles = article_count
        
        return top_magazine