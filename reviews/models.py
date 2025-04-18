from django.db import models
from django.contrib import auth



# A company that publishes books
# Publisher (id (primary key) (default), name, website, email)
# __str__ --> "name"
class Publisher (models.Model):
    name = models.CharField (
        "Publisher Name",
        max_length = 50,
        help_text = "The name of the publisher"
    )
    website = models.URLField (
        "Publisher Site",
        help_text = "The website of the publisher"
    )
    email = models.EmailField (
        "Publisher Email Address",
        help_text = "The e-mail address of the publisher"
    )

    def __str__ (self):
        return self.name



# A contributor to a book, e.g. author, editor, co-author
# Contributor (id (primary key) (default), first_names, last_names,
#              email)
# __str__ --> "last_name, first_name"
class Contributor (models.Model):
    first_names = models.CharField (
        "First Name",
        max_length = 50,
        help_text = "The first name/names of the contributor"
    )
    last_names = models.CharField (
        "Last Name",
        max_length = 50,
        help_text = "The last name/names of the contributor"
    )
    email = models.EmailField (
        "Contributor Email Address",
        help_text = "The e-mail address of the contributor"
    )

    def __str__ (self):
        return self.last_name + ", " + self.first_name



# A published book
# Book  (id (primary key) (default), title, publication_date, isbn,
#        publisher (foreign key), contributors (many-to-many))
# __str__ --> "title"
class Book (models.Model):
    title = models.CharField (
        "Book Title",
        max_length = 70,
        help_text = "The title of the book"
    )
    publication_date = models.DateField (
        "Publication Date",
        help_text = "The publication date of the book"
    )
    isbn = models.CharField (
        "ISBN",
        max_length = 20,
        help_text = "The ISBN of the book"
    )
    publisher = models.ForeignKey (
        Publisher,
        on_delete = models.CASCADE
    )
    contributors = models.ManyToManyField (
        'Contributor',
        through = "BookContributor"
    )

    def __str__ (self):
        return self.title



# Intermediate table between Book and Contributor
# BookContributor (id (primary key) (default), book (foreign key),
#                  contributor (foreign key), role)
# role = Author xor Co-Author xor Editor
class BookContributor (models.Model):
    class ContributorRole (models.TextChoices):
        AUTHOR = "AUTHOR", "Author"
        CO_AUTHOR = "CO_AUTHOR", "Co-Author"
        EDITOR = "EDITOR", "Editor"

    book = models.ForeignKey (
        Book,
        on_delete = models.CASCADE
    )
    contributor = models.ForeignKey (
        Contributor,
        on_delete = models.CASCADE
    )
    role = models.CharField (
        "Contributor Role",
        choices = ContributorRole.choices,
        max_length = 20,
        help_text = "The role of the contributor"
    )



# A user review for a book
# Review (id (primary key) (default), content, rating, date_created,
#         date_edited (date last edited), reviewer (foreign key),
#         book (foreign key))
class Review (models.Model):
    content = models.TextField (
        help_text = "The content/text of the review"
    )
    rating = models.IntegerField (
        help_text = "The rating given by the reviewer"
    )
    date_created = models.DateTimeField (
        auto_now_add = True,
        help_text = "The date and time the review was created"
    )
    date_edited = models.DateTimeField (
        null = True,
        help_text = "The date and time the review was last edited"
    )
    creator = models.ForeignKey (
        auth.get_user_model(),
        on_delete = models.CASCADE
    )
    book = models.ForeignKey (
        Book,
        on_delete = models.CASCADE,
        help_text = "The book the review was made for"
    )