class Author:
    def __init__(self, name):
        self.name = name
        self.books = []

    def publish(self, title):
        self.books.append(title)

    def __str__(self):
        title = ','.join(self.books) or 'No publish books'
        return f'{self.name}, Books: {title}'

def main():
    urgessa = Author('M. J. Urgessa')
    urgessa.publish('Floring Estimater')
    urgessa.publish('Weight Tracker')
    print(urgessa)

    #urgessa = Author('Urgessa')
    #print(urgessa)

main()
