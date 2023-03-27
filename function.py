

def calculateMonth(daysWorked: int, otHours: int, daysLate: int) -> float:
    # validate input
    bonus = 0
    if daysWorked <= 0 or otHours < 0 or daysLate < 0:
        raise ValueError("Invalid input")

    normal = daysWorked * 340

    if otHours > 3  :
        ot = 0
    elif  3 >= otHours >= 0: 
        ot = (otHours)* 60 

    if daysWorked >= 30:
        if daysLate == 0:
            bonus = 1000
    else:
        bonus = 0

    total = normal + ot + bonus

    return total
