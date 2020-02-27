from scoreboard.scoreboard import ScoreBoard


class TestScoreBoard:

    def test_returns_result_when_local_score_nine_points(self):
        score_board = ScoreBoard()

        for point in range(9):
            score_board.add_one_for_local()

        assert score_board.result() == '009-000'

    def test_returns_result_when_local_score_ten_points(self):
        score_board = ScoreBoard()

        for point in range(10):
            score_board.add_one_for_local()

        assert score_board.result() == '010-000'
