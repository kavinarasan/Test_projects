
movies = []
mv_run = True

def add_movie():
    print('*********Add movie*********')
    m_name = input('Enter movie name: ')
    m_dir_name = input('Enter Director name: ')
    m_year = input('Enter movie release year: ')
    movie = {'name': m_name.lower(), 'director': m_dir_name.lower(), 'year_of_release': m_year}
    movies.append(movie)

def get_movie():
    print(movies)

def delete_movie():
    print('*********Delete movie*********')
    del_name = input('Enter movie name: ')
    for mv in movies:
        if mv.get('name') == del_name.lower():
            movies.remove(mv)
            print('Movie deleted\n',movies)

def input_get():
    inp_str = ('1.Enter A to add movie / director / year of release \n2.Enter D to delete a movie by name \n3.Enter G to get details about a movie \n4.Enter q to quit.')
    print(inp_str)
    valid_inp = ('a', 'd', 'g', 'q')
    action = input('Enter your choice : ')

    while action.lower() not in valid_inp:
        action = input(f'Give Valid input\n{inp_str}')

    return action

def mv_check():
    while mv_run:
        act = input_get()
        if act.lower() == 'a':
            add_movie()

        elif act.lower() == 'g':
            get_movie()

        elif act.lower() == 'd':
            delete_movie()

        elif act.lower() == 'q':
            break

if __name__ == '__main__':
    mv_check()
