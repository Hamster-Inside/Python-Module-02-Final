from test_and_mock import check_first_line_more_than


def test_one(requests_mock):
    data = '007279035BE63272C81B84BD8B07D25D7E5:10\n010B55A0CE243B3AA85FC808ACBEB97FFA3:2'
    requests_mock.get('https://api.pwnedpasswords.com/range/a94a8', text=data)
    assert check_first_line_more_than(9) == True


def two(requests_mock):
    data = '007279035BE63272C81B84BD8B07D25D7E5:10\n010B55A0CE243B3AA85FC808ACBEB97FFA3:2'
    requests_mock.get('https://api.pwnedpasswords.com/range/a94a8', text=data)
    assert check_first_line_more_than(11) == False
