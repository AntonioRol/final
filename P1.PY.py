def credit_card_penalty(balance, days_late):
    if days_late < 15:
        result = balance * 0.05
        return result
    elif days_late >= 15 and days_late <= 30:
        result = balance * 0.10
        return result
    elif days_late >= 31 and days_late <= 60:
        result = balance * 0.15
        return result
    else:
        result = balance * 0.20
        return result


print "Penalty 1", credit_card_penalty(15000,18)
print "penalty 2", credit_card_penalty(7000,31)
print "penalty 3", credit_card_penalty(300,70)
print "penalty 4", credit_card_penalty(1000,3)

