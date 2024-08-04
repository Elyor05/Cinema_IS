# создаем класс "CinemaTicketSystem"
class CinemaTicketSystem:
    # создаем атрибуты класса
    def __init__(self):
        # фильмы, пользователи и билеты будут у нас записаны в словари
        self.movies = {}
        self.users = {}
        self.tickets = {}
        # а для счета можно использовать integer
        self.movie_counter = 0
        self.user_counter = 0
        self.ticket_counter = 0

# Функции = Методы класса - которые нужны для реализации функционала
    def addMovie(self, movieName):  # за аргумент берем название фильма
        self.movie_counter += 1
        self.movies[self.movie_counter] = movieName  # в словарь записываем название фильма под ключом значения счетчика
        return self.movie_counter

    def showAllMovies(self):
        if not self.movies:  # если словарь пустой, то выведет что нет фильмов в каталоге
            print("No movies available.")
        else:
            for movie_id, movie_name in self.movies.items():  # в случае словаря можно использовать 2 переменные и метод
                print(f"ID: {movie_id}, Movie: {movie_name}") # .items() для записи отдельно ключей и значений

    # тот же самый метод как и addMovie
    def addUser(self, userName):
        self.user_counter += 1
        self.users[self.user_counter] = userName
        return self.user_counter

    def buyTicket(self, userId, movieId):
        if userId not in self.users:
            print("User ID not found.")
            return None
        if movieId not in self.movies:
            print("Movie ID not found.")
            return None

        self.ticket_counter += 1
        self.tickets[self.ticket_counter] = {  # здесь мы записываем на ключ счетчика еще один словарь
            "userId": userId,
            "movieId": movieId
        }
        return self.ticket_counter

    def cancelTicket(self, ticketId):
        if ticketId in self.tickets:  # если находит внешний ключ, то удаляет и возвращает True
            del self.tickets[ticketId]
            return True
        return False  # в противном случае, нет


def main():
    # создаем объект 'cinema_system' от класса "CinemaTicketSystem"
    cinema_system = CinemaTicketSystem()

    print("\nЗдравствуйте, у вас есть следующие доступные функции:")

    while True:  # это позволит после каждого совершенного действия возвращаться в главное меню
        print("\n1. Добавить новый фильм")
        print("2. Показать все доступные фильмы")
        print("3. Добавить нового пользователя")
        print("4. Купить билет")
        print("5. Отменить покупку билета")
        print("6. Выход")

        choice = input()

        # в зависимости от того что выберет персонал кинотеатра, будет выполнена определенная задача

        if choice == '1':
            movie_name = input("Введите название фильма: ")
            movie_id = cinema_system.addMovie(movie_name)  # через название объекта мы имеем доступ к методам его класса
            print(f"Фильм '{movie_name}' добавлен с ID {movie_id}.")

        elif choice == '2':
            print("Список всех фильмов:")
            cinema_system.showAllMovies()

        elif choice == '3':
            user_name = input("Введите имя пользователя: ")
            user_id = cinema_system.addUser(user_name)
            print(f"Пользователь '{user_name}' зарегистрирован с ID {user_id}.")

        elif choice == '4':
            user_id = int(input("Введите ID пользователя: "))
            movie_id = int(input("Введите ID фильма: "))
            ticket_id = cinema_system.buyTicket(user_id, movie_id)
            if ticket_id:
                print(f"Билет куплен. ID билета: {ticket_id}.")  # True
            else:
                print("Не удалось купить билет. Проверьте ID пользователя и фильма.")  # False

        elif choice == '5':
            ticket_id = int(input("Введите ID билета для отмены: "))
            if cinema_system.cancelTicket(ticket_id):
                print(f"Билет с ID {ticket_id} успешно отменен.")  # True
            else:
                print("Не удалось отменить билет. Билет с таким ID не найден.")  # False

        elif choice == '6':
            print("Выход из программы. До свидания!")
            break  # выход из программы которая прекращает работу 'while' на 61 строке

        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()  # так как main() и сама функция , её тоже надо будет вызвать
