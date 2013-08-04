import store
import movie

def main():
    
    store = store.Store()
    addMovies(store)
    while 1:
        result = input("Enter command or Exit")
        if result == "Exit":
            break
        elif result.startswith("rent"):
            name = result.split()[1]
            try:
                rental = store.rentMovie(name)
            except store.NoMovie as e:
                print(e)
            except store.NoInventory as e:
                print(e)
        
            
def addMovies(store):
    store.addMovie(movie.Movie("Lord of the Rings",5.50,100));
    store.addMovie(movie.Movie("Wizard of Oz",2.50,10));
    store.addMovie(movie.Movie("Pulp Fiction",5.00,20));
    
    
if __name__ == '__main__':
    main()