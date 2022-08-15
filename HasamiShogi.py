# Description: Hasami Shogi board game simulation


class HasamiShogi:
    """A class that has several data members and methods which work
    together to simulate a game of Hasami Shogi"""
    def __init__(self, gameboard=None):
        """Initializes private data members, including game state, active player, red captured,
        black captured, etc"""
        if gameboard is None:
            list_number = ["  ", "1 ", "2 ", "3 ", "4 ", "5 ", "6 ", "7 ", "8 ", "9 "]
            list_a = ["a ", "R ", "R ", "R ", "R ", "R ", "R ", "R ", "R ", "R "]
            list_b = ["b ", ". ", ". ", ". ", ". ", ". ", ". ", ". ", ". ", ". "]
            list_c = ["c ", ". ", ". ", ". ", ". ", ". ", ". ", ". ", ". ", ". "]
            list_d = ["d ", ". ", ". ", ". ", ". ", ". ", ". ", ". ", ". ", ". "]
            list_e = ["e ", ". ", ". ", ". ", ". ", ". ", ". ", ". ", ". ", ". "]
            list_f = ["f ", ". ", ". ", ". ", ". ", ". ", ". ", ". ", ". ", ". "]
            list_g = ["g ", ". ", ". ", ". ", ". ", ". ", ". ", ". ", ". ", ". "]
            list_h = ["h ", ". ", ". ", ". ", ". ", ". ", ". ", ". ", ". ", ". "]
            list_i = ["i ", "B ", "B ", "B ", "B ", "B ", "B ", "B ", "B ", "B "]
            game_board = [list_number, list_a, list_b, list_c, list_d, list_e, list_f, list_g, list_h, list_i]
            gameboard = game_board

        self._game_state = "UNFINISHED"
        self._active_player = "BLACK"
        self._red_captured = 0
        self._black_captured = 0
        self._game_board = gameboard
        self._converted_x_coordinate = 0
        self._converted_y_coordinate = 0

    def get_game_state(self):
        """Returns the game state: Unfinished, red won, or black won"""
        return self._game_state

    def get_active_player(self):
        """Returns the active player: red or black"""
        return self._active_player

    def get_num_captured_pieces(self, team):
        """Takes as a parameter the team color, and
        returns the number of captured pieces for said team"""
        if team == "RED":
            # print(f"Number of captured red: {self._red_captured}")
            return self._red_captured
        elif team == "BLACK":
            return self._black_captured

    def _convert_coordinates(self, square_location):
        """Converts coordinates from what user entered to
        private data members that acn be used for the rest of the
        program"""
        # x coordinate is number
        self._converted_x_coordinate = int(square_location[1])
        # y coordinate is letter
        letter = square_location[0]
        if letter == "a":
            self._converted_y_coordinate = 1
        elif letter == "b":
            self._converted_y_coordinate = 2
        elif letter == "c":
            self._converted_y_coordinate = 3
        elif letter == "d":
            self._converted_y_coordinate = 4
        elif letter == "e":
            self._converted_y_coordinate = 5
        elif letter == "f":
            self._converted_y_coordinate = 6
        elif letter == "g":
            self._converted_y_coordinate = 7
        elif letter == "h":
            self._converted_y_coordinate = 8
        elif letter == "i":
            self._converted_y_coordinate = 9

    def get_square_occupant(self, square_location):
        """Takes as a parameter any square location, and translates it to the space on the board.
        Returns contents of said space on board.  Used in many methods in class"""
        self._convert_coordinates(square_location)
        contents = self._game_board[self._converted_y_coordinate][self._converted_x_coordinate]
        if contents == "B ":
            return "BLACK"
        if contents == "R ":
            return "RED"
        if contents == ". ":
            return "NONE"

    def _get_square_content(self, square_location):
        """Takes as a parameter any square location, and translates it to the space on the board.
        Returns contents of said space on board.  Used in many methods in class"""
        self._convert_coordinates(square_location)
        return self._game_board[self._converted_y_coordinate][self._converted_x_coordinate]

    def _check_if_move_is_legal(self, current_position, desired_position):
        """Checks if move is legal.  Pawns can move horizontally or vertically,
        and they cannot jump other pieces.  Works with the make move method.
        If move is not legal, will return False"""
        desired_square = self._get_square_content(desired_position)
        horizontally_legal = ""
        vertically_legal = ""
        legal = ""

        # check if move goes to an occupied position
        if desired_square != ". ":
            # print("Desired square isn't empty")
            return False
        # check if move is legal horizontally
        if current_position[0] == desired_position[0]:
            horizontally_legal = True
        # check if move is legal vertically
        if current_position[1] == desired_position[1]:
            vertically_legal = True
        # ensure that move is legal either horizontally or vertically
        if horizontally_legal == True or vertically_legal == True:
            legal = True
        if legal != True:
            # print("Pawn is not moving horizontally or vertically")
            return False
        # check if there are any pieces blocking trajectory, returns False if so
        # check if moving horizontally
        if horizontally_legal == True:
            self._convert_coordinates(current_position)
            current_x_coordinate = self._converted_x_coordinate
            self._convert_coordinates(desired_position)
            desired_x_coordinate = self._converted_x_coordinate
            # set range
            if current_x_coordinate > desired_x_coordinate:
                first = desired_x_coordinate
                second = current_x_coordinate
            else:
                first = current_x_coordinate
                second = desired_x_coordinate
            # check spaces in range are empty
            for space in range(first + 1, second):
                if self._game_board[self._converted_y_coordinate][space] != ". ":
                    # print("You can't skip a piece")
                    return False
        # check if moving vertically
        elif vertically_legal == True:
            self._convert_coordinates(current_position)
            current_y_coordinate = self._converted_y_coordinate
            self._convert_coordinates(desired_position)
            desired_y_coordinate = self._converted_y_coordinate
            # set range
            if current_y_coordinate > desired_y_coordinate:
                first = desired_y_coordinate
                second = current_y_coordinate
            else:
                first = current_y_coordinate
                second = desired_y_coordinate
            # check that spaces in range are empty
            for space in range(first + 1, second):
                if self._game_board[space][self._converted_x_coordinate] != ". ":
                    # print("You can't skip a piece")
                    return False

    def _move_pawn(self, current_position, desired_position):
        """Changes the gameboard to reflect new position, returns updated gameboard"""
        # change pawn's place on gameboard once it's determined that move is legal
        # save contents of current position
        current_position_contents = self._get_square_content(current_position)
        # make current position blank
        self._game_board[self._converted_y_coordinate][self._converted_x_coordinate] = ". "
        # convert x, y coordinates of desired position
        self._convert_coordinates(desired_position)
        # set desired position contents to previous position's contents
        self._game_board[self._converted_y_coordinate][self._converted_x_coordinate] = current_position_contents
        # self.print_gameboard()

    def _remove_captured_pieces(self, list_of_coordinates):
        """Gets called by various check for captures methods and updates game board to
        remove captured pieces, switching list_of_coordinates to blank spaces"""
        # iterate through list of pieces to remove and change coordinates to blank space
        for coordinate in list_of_coordinates:
            coordinate_y = int(coordinate[0])
            coordinate_x = int(coordinate[1])
            self._game_board[coordinate_y][coordinate_x] = ". "

    def _set_captured_piece_red(self, number_to_increase):
        """If a red piece has been captured, increases red captured piece and returns number"""
        self._red_captured += number_to_increase

    def _set_captured_piece_black(self, number_to_increase):
        """If a black piece has been captured, increased black captured piece and returns number"""
        self._black_captured += number_to_increase

    def _set_game_state(self, winner):
        """Changes game state from default unfinished if red or black wins and returns state"""
        if winner == "RED":
            self._game_state = "RED_WON"
        if winner == "BLACK":
            self._game_state = "BLACK_WON"

    def _check_for_standard_captures(self, desired_position):
        captured_red_pieces = 0
        captured_black_pieces = 0
        potential_captured_piece = 0
        captured_piece_list = []
        if self._active_player == "RED":
            player = "R "
            enemy = "B "
        else:
            player = "B "
            enemy = "R "
        # first, gets coordinates of new position
        self._convert_coordinates(desired_position)
        directions = ["UP", "DOWN", "LEFT", "RIGHT"]
        for direction in directions:
            skip_status = "FINE"
            if direction == "UP":
                first_start = self._converted_y_coordinate - 1
                if first_start < 3:
                    skip_status = "SKIP"
                second_start = first_start - 1
                first_stop = second_start
                second_stop = 1
                step = -1
                second_index = self._converted_x_coordinate
                x_coordinate = self._converted_x_coordinate
            if direction == "DOWN":
                first_start = self._converted_y_coordinate + 1
                if first_start > 8:
                    skip_status = "SKIP"
                second_start = first_start + 1
                first_stop = second_start
                second_stop = 10
                step = 1
                second_index = self._converted_x_coordinate
                x_coordinate = self._converted_x_coordinate
            if direction == "LEFT":
                first_start = self._converted_x_coordinate - 1
                if first_start < 3:
                    skip_status = "SKIP"
                second_start = first_start - 1
                first_stop = second_start
                second_stop = 1
                step = -1
                first_index = self._converted_y_coordinate
                y_coordinate = self._converted_y_coordinate
            if direction == "RIGHT":
                first_start = self._converted_x_coordinate + 1
                if first_start > 8:
                    skip_status = "SKIP"
                second_start = first_start + 1
                first_stop = second_start
                second_stop = 10
                step = 1
                first_index = self._converted_y_coordinate
                y_coordinate = self._converted_y_coordinate
            if skip_status != "SKIP":
                for square in range(first_start, first_stop, step):
                    potential_captured_piece = 0
                    if direction == "UP" or direction == "DOWN":
                        y_coordinate = square
                        first_index = square
                    if direction == "LEFT" or direction == "RIGHT":
                        x_coordinate = square
                        second_index = square
                    if self._game_board[y_coordinate][x_coordinate] == enemy:
                        coordinate = str(first_index)
                        coordinate += str([second_index][0])
                        captured_piece_list.append(coordinate)
                        potential_captured_piece += 1
                        for second_square in range(second_start, second_stop, step):
                            if direction == "UP" or direction == "DOWN":
                                y_coordinate = second_square
                                first_index = second_square
                            if direction == "LEFT" or direction == "RIGHT":
                                x_coordinate = second_square
                                second_index = second_square
                            if self._game_board[y_coordinate][x_coordinate] == enemy:
                                coordinate = str(first_index)
                                coordinate += str([second_index][0])
                                captured_piece_list.append(coordinate)
                                potential_captured_piece += 1
                            if self._game_board[y_coordinate][x_coordinate] == player:
                                # print(potential_captured_piece_list)
                                self._remove_captured_pieces(captured_piece_list)
                                if player == "B ":
                                    captured_red_pieces += potential_captured_piece
                                else:
                                    captured_black_pieces += potential_captured_piece
                                break
        if captured_red_pieces > 0:
            return captured_red_pieces
        elif captured_black_pieces > 0:
            return captured_black_pieces
        else:
            return 0

    def _check_for_corner_captures(self, desired_position):
        """Is called by check_for_captures() method and checks specifically for corner captures.
        Returns number of pieces captured"""
        captured_red_pieces = 0
        captured_black_pieces = 0
        potential_captured_piece = 0
        list_of_corner_capture_locations = ["b1", "a2", "a8", "b9", "h1", "i2", "h9", "i8"]
        # Special case for corner capture.
        if desired_position not in list_of_corner_capture_locations:
            return 0
        # check upper left corner
        if desired_position == "a2" or desired_position == "b1":
            if self._active_player == "BLACK":
                if self._get_square_content("a2") == "B " and self._get_square_content("b1") == "B " and self._get_square_content("a1") == "R ":
                    self._remove_captured_pieces(["11"])
                    captured_red_pieces += 1
                    return captured_red_pieces
                else:
                    return 0
            if self._active_player == "RED":
                if self._get_square_content("a2") == "R " and self._get_square_content("b1") == "R " and self._get_square_content("a1") == "B ":
                    self._remove_captured_pieces(["11"])
                    captured_black_pieces += 1
                    return captured_black_pieces
                else:
                    return 0
        # check upper right corner
        if desired_position == "a8" or desired_position == "b9":
            if self._active_player == "BLACK":
                if self._get_square_content("a8") == "B " and self._get_square_content("b9") == "B " and self._get_square_content("a9") == "R ":
                    self._remove_captured_pieces(["19"])
                    captured_red_pieces += 1
                    return captured_red_pieces
                else:
                    return 0
            if self._active_player == "RED":
                if self._get_square_content("a8") == "R " and self._get_square_content("b9") == "R " and self._get_square_content("a9") == "B ":
                    self._remove_captured_pieces(["19"])
                    captured_black_pieces += 1
                    return captured_black_pieces
                else:
                    return 0
        # check lower left corner
        if desired_position == "h1" or desired_position == "i2":
            if self._active_player == "BLACK":
                if self._get_square_content("h1") == "B " and self._get_square_content("i2") == "B " and self._get_square_content("i1") == "R ":
                    self._remove_captured_pieces(["91"])
                    captured_red_pieces += 1
                    return captured_red_pieces
                else:
                    return 0
            if self._active_player == "RED":
                if self._get_square_content("h1") == "R " and self._get_square_content("i2") == "R " and self._get_square_content("i1") == "B ":
                    self._remove_captured_pieces(["91"])
                    captured_black_pieces += 1
                    return captured_black_pieces
                else:
                    return 0
        # check lower right corner
        if desired_position == "i8" or desired_position == "h9":
            if self._active_player == "BLACK":
                if self._get_square_content("i8") == "B " and self._get_square_content("h9") == "B " and self._get_square_content("i9") == "R ":
                    self._remove_captured_pieces(["99"])
                    captured_red_pieces += 1
                    return captured_red_pieces
                else:
                    return 0
            if self._active_player == "RED":
                if self._get_square_content("i8") == "R " and self._get_square_content("h9") == "R " and self._get_square_content("i9") == "B ":
                    self._remove_captured_pieces(["99"])
                    captured_black_pieces += 1
                    return captured_black_pieces
                else:
                    return 0

    def _check_for_captures(self, desired_position):
        """Once piece has been moved, checks to see if any captures have been made. Calls on
        three different methods to check for horizontal capture, vertical capture, and corner capture.
        If capture has been made, calls method for setting captured red or black pieces"""
        captured_red_pieces = 0
        captured_black_pieces = 0
        if self._active_player == "RED":
            # captured_black_pieces = self._check_for_horizontal_capture(desired_position)
            captured_black_pieces = self._check_for_standard_captures(desired_position)
            captured_black_pieces += self._check_for_corner_captures(desired_position)
            if captured_black_pieces > 0:
                self._set_captured_piece_black(captured_black_pieces)
        if self._active_player == "BLACK":
            # captured_red_pieces = self._check_for_horizontal_capture(desired_position)
            captured_red_pieces = self._check_for_standard_captures(desired_position)
            captured_red_pieces += self._check_for_corner_captures(desired_position)
            if captured_red_pieces > 0:
                self._set_captured_piece_red(captured_red_pieces)

    def _check_for_win(self):
        """Gets called by make move method.  If one player has one, then calls on
        set_game_state method with winner as the parameter"""

        # Looks at pieces captured
        if self._red_captured > 7:
            self._set_game_state("BLACK")
        elif self._black_captured > 7:
            self._set_game_state("RED")

    def _change_active_player(self):
        """Gets called at the end of make move method.
        Switches active player after other team has had their turn"""
        if self._active_player == "RED":
            self._active_player = "BLACK"
        elif self._active_player == "BLACK":
            self._active_player = "RED"

    def make_move(self, current_position, desired_position):
        """This is the central method for coordinating everything involved
        in moving a piece, and thus calls on many other methods.  Takes as
        parameters the current square and the desired square.  First
        checks if move is legal, and returns False if not. Next calls
        on move pawn method to actually change the game board.  Next calls on
        check captive method to check for
        any captures.  Then calls on check for win to determine
        if game has been won. Then calls on change active player method to
        change active player. Then if all conditions are met, returns True"""
        # part 1: determine if move is legal
        # get current square from get_square_occupant method and save to variable
        current_square = self._get_square_content(current_position)
        current_player = self.get_active_player()
        current_state = self.get_game_state()
        # make sure that it is the correct player's turn, R should match R and B should match B:
        if current_square[0] != current_player[0]:
            # print("Not your turn")
            return False
        # make sure that the game has not been won:
        if current_state != "UNFINISHED":
            return False
        # check if move is legal:
        legal = self._check_if_move_is_legal(current_position, desired_position)
        if legal is False:
            self._change_active_player()
            return False
        # move piece:
        self._move_pawn(current_position, desired_position)
        self._check_for_captures(desired_position)
        self._check_for_win()
        self._change_active_player()
        # self.print_gameboard()
        return True

    def print_gameboard(self):
        """Prints gameboard for testing purposes"""
        for item in self._game_board:
            print("".join(item))


# game = HasamiShogiGame()
# game.print_gameboard()
# print(game.get_square_occupant("a1"))
# print(game.get_square_occupant("a9"))
# print(game.get_square_occupant("i5"))
#
# game.make_move("i1", "d1")
# game.make_move("a2", "b2")
# game.make_move("d1", "d2")
# game.make_move("a1", "i1")
# game.make_move("i3", "d3")
# game.make_move("b2", "b3")
# game.make_move("d3", "d9")
# game.make_move("a3", "i3")

# game.make_move("i5", "f5")
# game.make_move("a3", "g3")
# game.make_move("i2", "g2")
# game.make_move("a5", "e5")
# game.make_move("i2", "e2")
# game.make_move("e5", "e1")
# game.make_move("i8", "e8")
# game.make_move("e5", "e7")
# game.make_move("i6", "e6")
# game.make_move("g3", "g5")
# game.make_move("i7", "i5")
# game.make_move("a8", "d8")
# game.make_move("i5", "h5")
# game.make_move("d8", "g8")
# game.make_move("e6", "c6")
# game.make_move("a2", "a3")
# game.make_move("c6", "c8")
# game.make_move("a1", "a2")
# game.make_move("c8", "a8")
# game.make_move("a2", "a1")
# game.make_move("i9", "b9")
# game.make_move("a7", "b7")
# game.make_move("e8", "e7")
# game.make_move("b7", "b8")
# game.make_move("e7", "b7")
# game.make_move("a1", "a2")
# game.make_move("b7", "b5")
# game.make_move("a6", "d6")
# game.make_move("b5", "a5")
# game.make_move("d6", "d9")
# game.make_move("i1", "a1")
# game.make_move("d9", "d8")

# game.make_move("b5", "a5")
# game.make_move("d6", "d9")
# game.make_move("i1", "a1")
# game.make_move("d9", "d8")
# print(game.get_game_state())
# print(game.get_num_captured_pieces("BLACK"))
