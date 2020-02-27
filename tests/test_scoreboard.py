from scoreboard.scoreboard import ScoreBoard


class TestScoreBoard:

    def test_returns_result_when_local_score_one(self):
        score_board = ScoreBoard()

        score_board.add_one_for_local()

        assert score_board.result() == '1-0'
