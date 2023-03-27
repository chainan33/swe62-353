from function import calculateMonth


def test_calculateMonth_case():

    #ไม่มี ot ไม่มีเลทงาน
    assert calculateMonth(20, 0, 0) == 6800

    #ไม่มี ot มีเลทงาน 
    assert calculateMonth(18, 0, 2) == 6120

    #มี OT ไม่มีเลทงาน
    assert calculateMonth(20, 3, 0) == 6980

    #มี ot มีเลทงาน
    assert calculateMonth(18, 3, 2) == 6300

    #ไม่มี ot ไม่มีเลทงาน
    assert calculateMonth(30, 0, 0) == 11200

    #
    assert calculateMonth(31, 0, 1) == 10540

