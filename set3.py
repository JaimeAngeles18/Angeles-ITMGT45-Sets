'''Programming Set 3

This assignment will develop your ability to manipulate data.
'''

def relationship_status(from_member, to_member, social_graph):
    from_follows_to = to_member in social_graph.get(from_member, {}).get("following", [])
    to_follows_from = from_member in social_graph.get(to_member, {}).get("following", [])
    if from_follows_to and to_follows_from:
        return "friends"
    elif from_follows_to:
        return "follower"
    elif to_follows_from:
        return "followed by"
    else:
        return "no relationship"

    
    '''Relationship Status.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data

    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    pass


def tic_tac_toe(board):
    n = len(board)
    for row in board:
        first_symbol = row[0]
        if first_symbol != "" and all(cell == first_symbol for cell in row):
            return first_symbol
    for col_index in range(n):
        first_symbol = board[0][col_index]
        if first_symbol != "" and all(board[row_index][col_index] == first_symbol for row_index in range(n)):
            return first_symbol
    first_symbol = board[0][0]
    if first_symbol != "" and all(board[i][i] == first_symbol for i in range(n)):
        return first_symbol
    first_symbol = board[0][n - 1]
    if first_symbol != "" and all(board[i][n - 1 - i] == first_symbol for i in range(n)):
        return first_symbol
    return "NO WINNER"
    '''Tic Tac Toe.

    Tic Tac Toe is a common paper-and-pencil game.
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    pass

def eta(first_stop, second_stop, route_map):
    if first_stop == second_stop:
        return 0

    total_time = 0
    current_stop = first_stop
    for _ in range(len(route_map)):
        next_leg = None
        for (origin, destination), info in route_map.items():
            if origin == current_stop:
                next_leg = (origin, destination)
                break

        if not next_leg:
            return None
        total_time += route_map[next_leg]["travel_time_mins"]
        current_stop = next_leg[1]
        if current_stop == second_stop:
            return total_time
    return None
    '''ETA.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see "mod-4-ipa-1-sample-data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    pass