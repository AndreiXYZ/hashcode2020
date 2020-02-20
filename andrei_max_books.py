def solution(books, libraries, max_timesteps):
    libraries_signups = []
    library_books = []
    print('max timesteps:', max_timesteps)
    for timestep in range(max_timesteps):
        remaining_timesteps = max_timesteps - timestep

        libraries = sorted(libraries, key=lambda library : 
                    (remaining_timesteps-library._signup_days)*library._amount_of_books_per_day,
                    reverse=True)       
        
        if len(libraries):
            lib = libraries[0]
            libraries_signups.append(lib.id)
            # Now pick whatever books
            num_books_lib = (remaining_timesteps-lib._signup_days)*lib._amount_of_books_per_day
            library_books.append(lib._book_ids[:num_books_lib])
            del libraries[0]
    
    return libraries_signups, library_books

    