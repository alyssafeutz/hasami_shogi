# Testing suite for hasami shogi game

import unittest
from HasamiShogi import *


class TestCase(unittest.TestCase):
    """Class to test hasami shogi game"""
    # Check that first player is black
    def test1_valid_player(self):
        board = HasamiShogi()
        expected = "BLACK"
        self.assertEqual(board.get_active_player(), expected)

    # Check that red cannot move out of turn
    def test2_valid_player(self):
        board = HasamiShogi()
        expected = False
        self.assertEqual(board.make_move("a1", "b1"), expected)

    # Check that black cannot make invalid diagonal movie
    def test3_valid_move(self):
        board = HasamiShogi()
        expected = False
        self.assertEqual(board.make_move("i1", "h2"), expected)

    # Check that black can make valid horizontal move
    def test4_valid_move(self):
        board = HasamiShogi()
        expected = True
        self.assertEqual(board.make_move("i1", "b1"), expected)

    # Check that it is then red's turn and can make a valid horizontal move
    def test5_valid_move(self):
        board = HasamiShogi()
        board.make_move("i1", "b1")
        expected = True
        self.assertEqual(board.make_move("a2", "b2"), expected)

    # Check that it is then black's turn and can make a valid vertical move
    def test6_valid_move(self):
        board = HasamiShogi()
        board.make_move("i1", "b1")
        board.make_move("a2", "c2")
        expected = True
        self.assertEqual(board.make_move("b1", "b3"), expected)

    # Check that correct game state is returned
    def test7_valid_state(self):
        board = HasamiShogi()
        board.make_move("i1", "b1")
        board.make_move("a2", "c2")
        board.make_move("b1", "b3")
        expected = "UNFINISHED"
        self.assertEqual(board.get_game_state(), expected)

    # Check that valid capture is made
    def test8_valid_black_capture(self):
        board = HasamiShogi()
        board.make_move("i1", "b1")
        board.make_move("a2", "c2")
        board.make_move("b1", "b3")
        board.make_move("a6", "c6")
        board.make_move("b3", "c3")
        board.make_move("a4", "c4")
        expected = 1
        self.assertEqual(board.get_num_captured_pieces("BLACK"), expected)

    # Check that after valid capture is made, piece has been removed
    def test9_valid_board(self):
        board = HasamiShogi()
        board.make_move("i1", "b1")
        board.make_move("a2", "c2")
        board.make_move("b1", "b3")
        board.make_move("a6", "c6")
        board.make_move("b3", "c3")
        board.make_move("a4", "c4")
        expected = "NONE"
        self.assertEqual(board.get_square_occupant("c3"), expected)

    # Check that after player cannot move into a capture
    def test10_valid_move(self):
        board = HasamiShogi()
        board.make_move("i1", "b1")
        board.make_move("a2", "c2")
        board.make_move("b1", "b3")
        board.make_move("a6", "c6")
        board.make_move("b3", "c3")
        board.make_move("a4", "c4")
        board.make_move("i5", "c5")
        expected = 1
        self.assertEqual(board.get_num_captured_pieces("BLACK"), expected)

    # Check that three pieces in a row can be captured
    def test11_valid_move(self):
        board = HasamiShogi()
        board.make_move("i1", "b1")
        board.make_move("a2", "c2")
        board.make_move("b1", "b3")
        board.make_move("a6", "c6")
        board.make_move("b3", "c3")
        board.make_move("a4", "c4")
        board.make_move("i5", "c5")
        board.make_move("a3", "c3")
        board.make_move("i2", "i1")
        board.make_move("a7", "c7")
        board.make_move("i1", "c1")
        expected = 3
        self.assertEqual(board.get_num_captured_pieces("RED"), expected)

    # Check that upper right corner capture works
    def test12_valid_corner_capture(self):
        board = HasamiShogi()
        board.make_move("i9", "b9")
        board.make_move("a8", "e8")
        board.make_move("i7", "b7")
        board.make_move("a6", "g6")
        board.make_move("b7", "b8")
        board.make_move("a3", "d8")
        board.make_move("b8", "a8")
        expected = "NONE"
        self.assertEqual(board.get_square_occupant("a9"), expected)

    # Check that upper left corner capture works
    def test13_valid_corner_capture(self):
        board = HasamiShogi()
        board.make_move("i1", "b1")
        board.make_move("a2", "h2")
        board.make_move("i3", "b3")
        board.make_move("a6", "g6")
        board.make_move("b3", "b2")
        board.make_move("a8", "d8")
        board.make_move("b2", "a2")
        expected = "NONE"
        self.assertEqual(board.get_square_occupant("a1"), expected)

    # Check that lower left corner capture works
    def test14_valid_corner_capture(self):
        board = HasamiShogi()
        board.make_move("i2", "d2")
        board.make_move("a1", "h1")
        board.make_move("i8", "d8")
        board.make_move("a3", "h3")
        board.make_move("d8", "d9")
        board.make_move("h3", "h2")
        board.make_move("d9", "d7")
        board.make_move("h2", "i2")
        expected = "NONE"
        self.assertEqual(board.get_square_occupant("i1"), expected)

    # Check that lower right corner capture works
    def test15_valid_corner_capture(self):
        board = HasamiShogi()
        board.make_move("i8", "d8")
        board.make_move("a9", "h9")
        board.make_move("i2", "d2")
        board.make_move("a7", "h7")
        board.make_move("d2", "d1")
        board.make_move("h7", "h8")
        board.make_move("d1", "d3")
        board.make_move("h8", "i8")
        expected = "NONE"
        self.assertEqual(board.get_square_occupant("i9"), expected)

    # check for corner capture
    def test16_valid_corner_capture(self):
        game_board = [["  ", "1 ", "2 ", "3 ", "4 ", "5 ", "6 ", "7 ", "8 ", "9 "],
                      ["a ", "R ", "R ", "R ", "R ", "R ", "R ", ". ", "R ", "B "],
                      ["b ", ". ", ". ", ". ", ". ", ". ", ". ", ". ", ". ", ". "],
                      ["c ", ". ", ". ", ". ", ". ", ". ", ". ", ". ", ". ", "R "],
                      ["d ", ". ", ". ", ". ", ". ", ". ", ". ", ". ", ". ", ". "],
                      ["e ", ". ", ". ", ". ", ". ", ". ", ". ", ". ", ". ", ". "],
                      ["f ", ". ", ". ", ". ", ". ", ". ", ". ", ". ", ". ", ". "],
                      ["g ", ". ", ". ", ". ", ". ", ". ", ". ", ". ", ". ", ". "],
                      ["h ", ". ", ". ", ". ", ". ", ". ", ". ", ". ", ". ", ". "],
                      ["i ", "B ", "B ", "B ", "B ", "B ", "B ", "B ", "B ", ". "]]
        board = HasamiShogi(game_board)
        board.make_move("i6", "g6")
        board.make_move("c9", "b9")
        expected = "NONE"
        self.assertEqual(board.get_square_occupant("a9"), expected)

    # check for corner capture
    def test17_valid_corner_capture(self):
        game_board = [["  ", "1 ", "2 ", "3 ", "4 ", "5 ", "6 ", "7 ", "8 ", "9 "],
                      ["a ", "B ", "R ", "R ", ". ", "R ", "R ", ". ", "R ", "B "],
                      ["b ", ". ", ". ", ". ", ". ", ". ", ". ", ". ", ". ", ". "],
                      ["c ", "R ", ". ", ". ", ". ", ". ", ". ", ". ", ". ", "R "],
                      ["d ", ". ", ". ", ". ", ". ", ". ", ". ", ". ", ". ", ". "],
                      ["e ", ". ", ". ", ". ", ". ", ". ", ". ", ". ", ". ", ". "],
                      ["f ", ". ", ". ", ". ", ". ", ". ", ". ", ". ", ". ", ". "],
                      ["g ", ". ", ". ", ". ", ". ", ". ", ". ", ". ", ". ", ". "],
                      ["h ", ". ", ". ", ". ", ". ", ". ", ". ", ". ", ". ", ". "],
                      ["i ", ". ", "B ", "B ", "B ", "B ", "B ", "B ", "B ", ". "]]
        board = HasamiShogi(game_board)
        board.make_move("i6", "g6")
        board.make_move("c1", "b1")
        expected = "NONE"
        self.assertEqual(board.get_square_occupant("a1"), expected)

    # check for corner capture
    def test18_valid_corner_capture(self):
        game_board = [["  ", "1 ", "2 ", "3 ", "4 ", "5 ", "6 ", "7 ", "8 ", "9 "],
                      ["a ", "B ", "R ", "R ", ". ", "R ", "R ", ". ", "R ", "B "],
                      ["b ", ". ", ". ", ". ", ". ", ". ", ". ", ". ", ". ", ". "],
                      ["c ", ". ", ". ", ". ", ". ", ". ", ". ", ". ", ". ", "R "],
                      ["d ", ". ", ". ", ". ", ". ", ". ", ". ", ". ", ". ", ". "],
                      ["e ", ". ", ". ", ". ", ". ", ". ", ". ", ". ", ". ", ". "],
                      ["f ", ". ", ". ", ". ", ". ", ". ", ". ", ". ", ". ", ". "],
                      ["g ", "B ", ". ", ". ", ". ", ". ", ". ", ". ", ". ", ". "],
                      ["h ", ". ", ". ", ". ", ". ", ". ", ". ", ". ", ". ", ". "],
                      ["i ", "R ", "B ", "B ", ". ", "B ", "B ", "B ", "B ", ". "]]
        board = HasamiShogi(game_board)
        board.make_move("g1", "h1")
        expected = "NONE"
        self.assertEqual(board.get_square_occupant("i1"), expected)

    # check for corner capture
    def test19_valid_corner_capture(self):
        game_board = [["  ", "1 ", "2 ", "3 ", "4 ", "5 ", "6 ", "7 ", "8 ", "9 "],
                      ["a ", "B ", "R ", "R ", ". ", "R ", "R ", ". ", "R ", "B "],
                      ["b ", ". ", ". ", ". ", ". ", ". ", ". ", ". ", ". ", ". "],
                      ["c ", ". ", ". ", ". ", ". ", ". ", ". ", ". ", ". ", "R "],
                      ["d ", ". ", ". ", ". ", ". ", ". ", ". ", ". ", ". ", ". "],
                      ["e ", ". ", ". ", ". ", ". ", ". ", ". ", ". ", ". ", ". "],
                      ["f ", ". ", ". ", ". ", ". ", ". ", ". ", ". ", ". ", ". "],
                      ["g ", "B ", ". ", ". ", ". ", ". ", ". ", ". ", ". ", "B "],
                      ["h ", ". ", ". ", ". ", ". ", ". ", ". ", ". ", ". ", ". "],
                      ["i ", ". ", "B ", "B ", ". ", "B ", "B ", ". ", "B ", "R "]]
        board = HasamiShogi(game_board)
        board.make_move("g9", "h9")
        expected = "NONE"
        self.assertEqual(board.get_square_occupant("i9"), expected)

    # check for valid number of captured pieces after several captures
    def test20_valid_captured_pieces(self):
        board = HasamiShogi()
        board.make_move("i1", "g1")
        board.make_move("a2", "g2")
        board.make_move("i3", "g3")
        board.make_move("a4", "g4")
        board.make_move("i5", "g5")
        board.make_move("a6", "g6")
        board.make_move("i7", "g7")
        board.make_move("a8", "g8")
        board.make_move("i9", "g9")
        expected = 3
        self.assertEqual(board.get_num_captured_pieces("BLACK"), expected)

    # check for recognition of red win
    def test22_valid_red_win(self):
        board = HasamiShogi()
        board.make_move("i1", "g1")
        board.make_move("a2", "g2")
        board.make_move("i3", "g3")
        board.make_move("a4", "g4")
        board.make_move("i5", "g5")
        board.make_move("a6", "g6")
        board.make_move("i7", "g7")
        board.make_move("a8", "g8")
        board.make_move("i9", "e9")
        board.make_move("a3", "i3")
        board.make_move("e9", "e6")
        board.make_move("a5", "i5")
        board.make_move("e6", "e5")
        board.make_move("a7", "i7")
        board.make_move("e5", "d5")
        board.make_move("a9", "i9")
        board.make_move("g1", "f1")
        board.make_move("g4", "d4")
        board.make_move("f1", "f2")
        board.make_move("g6", "d6")
        board.make_move("i2", "h2")
        board.make_move("g8", "g2")
        board.make_move("f2", "f4")
        board.make_move("i3", "i2")
        expected = "RED_WON"
        self.assertEqual(board.get_game_state(), expected)

    # check that game play cannot continue after win
    def test23_game_play_stops(self):
        board = HasamiShogi()
        board.make_move("i1", "g1")
        board.make_move("a2", "g2")
        board.make_move("i3", "g3")
        board.make_move("a4", "g4")
        board.make_move("i5", "g5")
        board.make_move("a6", "g6")
        board.make_move("i7", "g7")
        board.make_move("a8", "g8")
        board.make_move("i9", "e9")
        board.make_move("a3", "i3")
        board.make_move("e9", "e6")
        board.make_move("a5", "i5")
        board.make_move("e6", "e5")
        board.make_move("a7", "i7")
        board.make_move("e5", "d5")
        board.make_move("a9", "i9")
        board.make_move("g1", "f1")
        board.make_move("g4", "d4")
        board.make_move("f1", "f2")
        board.make_move("g6", "d6")
        board.make_move("i2", "h2")
        board.make_move("g8", "g2")
        board.make_move("f2", "f4")
        board.make_move("i3", "i2")
        self.assertFalse(board.make_move("f4", "f5"))

    # check that piece cannot move into occupied position
    def test24_occupied_position(self):
        board = HasamiShogi()
        self.assertFalse(board.make_move("i1", "a1"))

    # check that piece cannot move into occupied position
    def test25_occupied_position(self):
        board = HasamiShogi()
        expected = "RED"
        self.assertEqual(board.get_square_occupant("a1"), expected)

    # check that piece cannot move into occupied position
    def test26_occupied_position(self):
        board = HasamiShogi()
        expected = "BLACK"
        self.assertEqual(board.get_square_occupant("i9"), expected)


if __name__ == "__main__":
    unittest.main()
