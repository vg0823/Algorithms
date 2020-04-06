
def can_two_movies_fill_flight(movie_lengths, flight_length):

    # Determine if two movie runtimes add up to the flight length
    movie_lengths_set = set()
    result = False
    for i in movie_lengths:
        movie_lengths_set.add(i)
    
    for i in movie_lengths:
        if (flight_length - i) in movie_lengths_set:
            result = True
            break
    print(flight_length)
    return result

result = can_two_movies_fill_flight([3, 8], 6)
print(result)