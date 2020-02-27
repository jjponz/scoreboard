from scoreboard.scoreboard import ScoreBoard


class TestScoreBoard:

    def test_returns_score_when_local_score_one_points(self):
        score_board = ScoreBoard()

        score_board.add_one_for_local()

        assert score_board.result() == '001-000'

    def test_returns_score_when_local_score_two_points(self):
        score_board = ScoreBoard()
        score_board.add_one_for_local()

        score_board.add_two_for_local()

        assert score_board.result() == '003-000'

    def test_returns_score_when_local_score_nine_points(self):
        score_board = ScoreBoard()

        score_board.add_two_for_local()
        for point in range(7):
            score_board.add_one_for_local()

        assert score_board.result() == '009-000'

    def test_returns_score_when_local_score_ten_points(self):
        score_board = ScoreBoard()

        for point in range(10):
            score_board.add_one_for_local()

        assert score_board.result() == '010-000'
