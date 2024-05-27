class Article:
    def __init__(self, title, author, magazine):
        self.title = title
        self.author = author
        self.magazine = magazine

    def get_title(self):
        return self._title

    def set_title(self, new_title):
        if hasattr(self, "title"):
            raise AttributeError("Title cannot be changed")
        else:
            if isinstance(new_title, str):
                if 5 <= len(new_title) <= 50:
                    self._title = new_title
                else:
                    raise ValueError("Title must be between 5 and 50 characters")
            else:
                raise TypeError("Title must be a string")

    def get_author(self):
        return self._author

    def set_author(self, new_author):
        if isinstance(new_author, Author):
            self._author = new_author
        else:
            raise TypeError("Author must be an instance of Author")

    def get_magazine(self):
        return self._magazine

    def set_magazine(self, new_magazine):
        if isinstance(new_magazine, Magazine):
            self._magazine = new_magazine
        else:
            raise TypeError("Magazine must be an instance of Magazine")

    title = property(get_title, set_title)
    author = property(get_author, set_author)
    magazine = property(get_magazine, set_magazine)


class Author:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self._name

    def set_name(self, new_name):
        if hasattr(self, "name"):
            raise AttributeError("Name cannot be changed")
        else:
            if isinstance(new_name, str):
                if len(new_name):
                    self._name = new_name
                else:
                    raise ValueError("Name must be longer than 0 characters")
            else:
                raise TypeError("Name must be a string")

    def get_articles(self):
        return [article for article in Article.all if self == article.author]

    def get_magazines(self):
        return list({article.magazine for article in self.get_articles()})

    def add_article(self, magazine, title):
        return Article(title, self, magazine)

    def get_topic_areas(self):
        topic_areas = list({magazine.category for magazine in self.get_magazines()})
        if topic_areas:
            return topic_areas
        else:
            return None

    name = property(get_name, set_name)
    articles = property(get_articles)
    magazines = property(get_magazines)
    topic_areas = property(get_topic_areas)


class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    def get_name(self):
        return self._name

    def set_name(self, new_name):
        if isinstance(new_name, str):
            if 2 <= len(new_name) <= 16:
                self._name = new_name
            else:
                raise ValueError("Name must be between 2 and 16 characters")
        else:
            raise TypeError("Name must be a string")

    def get_category(self):
        return self._category

    def set_category(self, new_category):
        if isinstance(new_category, str):
            if len(new_category):
                self._category = new_category
            else:
                raise ValueError("Category must be longer than 0 characters")
        else:
            raise TypeError("Category must be a string")

    def get_articles(self):
        return [article for article in Article.all if self == article.magazine]

    def get_contributors(self):
        return list({article.author for article in self.get_articles()})

    def get_article_titles(self):
        article_titles = [article.title for article in self.get_articles()]
        if article_titles:
            return article_titles
        else:
            return None

    def get_contributing_authors(self):
        authors = {}
        list_of_authors = []
        for article in self.get_articles():
            if article.author in authors:
                authors[article.author] += 1
            else:
                authors[article.author] = 1

        for author in authors:
            if authors[author] >= 2:
                list_of_authors.append(author)

        if list_of_authors:
            return list_of_authors
        else:
            return None

    name = property(get_name, set_name)
    category = property(get_category, set_category)
    articles = property(get_articles)
    contributors = property(get_contributors)
    article_titles = property(get_article_titles)
    contributing_authors = property(get_contributing_authors)
    
    
    