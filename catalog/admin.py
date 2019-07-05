from django.contrib import admin

from catalog.models import Author, Genre, Book, BookInstance, Language
# Register your models here.

# admin.site.register(Book)
# admin.site.register(Author)
admin.site.register(Genre)
# admin.site.register(BookInstance)
admin.site.register(Language)

# definition of admin class
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    # fields allows the page to be layed out differently, by doing it like below, 
    # firstName and lastName will be placed on separate lines, and the Dates(tm) will
    # br put on their own line.
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]

# Registration of admin class with assoc'd model
admin.site.register(Author, AuthorAdmin)

class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # this list_display changes the display of the admin "book" site,
    # by creating this variable, the book's information is displayed in the order
    # of the class variables defined in models.py :)
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'borrower', 'due_back', 'id')
    list_filter = ('status', 'due_back')
    
    fieldsets = (
        (None, {
            'fields': ('book','imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back','borrower')
        }),
    )
    # by adding the fieldsets variable , you can add sections to the page.
    # in the example below, the first section uses None as the title, which
    # allows the section to have no title, in the section with no title, the
    # fields specified are: book, imprint, and the id of the bookInstance.
    # this list_filter adds a section to our page that allows filtrations,
    # eg. what time our books is back, the status of the book.
    