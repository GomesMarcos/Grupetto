def test_when_score_is_created_and_its_bigger_than_players_max_score_update_players_max_score(mock_player, mock_score):
    assert mock_player.max_score == 0
    mock_score.score = 5
    mock_score.save()
    assert mock_player.max_score == mock_score.score

    save_mock_score(2, mock_score, mock_player)
    save_mock_score(5, mock_score, mock_player)


def save_mock_score(score, mock, mock_player):
    mock_player.max_score = 5
    mock.score = score
    mock.save()
    assert mock_player.max_score == 5
