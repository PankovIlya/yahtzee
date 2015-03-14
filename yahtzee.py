import combinatorics as cmb

"""
Planner for Yahtzee
Simplifications:  only allow discard and roll, only score against upper level
"""


def score(hand):
    """
    Compute the maximal score for a Yahtzee hand according to the
    upper section of the Yahtzee score card.
    """
    res = 0
    dscor = {}
    for itm in hand:
        dscor.setdefault(itm, 0)
        dscor[itm] += 1
        
    for itm in dscor:
        val = dscor[itm]*itm
        if val > res:
            res = val
            
    return res


def expected_value(held_dice, num_die_sides, num_free_dice):
    """
    Compute the expected value based on held_dice given that there
    are num_free_dice to be rolled, each with num_die_sides.
    """
    set_free = cmb.permutationsr([x for x in xrange(1, num_die_sides+1)],
                                 num_free_dice)
    held = list(held_dice)
    sum_comb = 0.0
    for itm in set_free:
        sum_comb += score(held + itm)
        

    return sum_comb/len(set_free)


def gen_all_holds(hand):
    """
    Generate all possible choices of dice from hand to hold.
    """
    res = []
    for lst in cmb.boolean(list(hand)):
        res.append(tuple(lst))
            
    return set(res)



def strategy(hand, num_die_sides):
    """
    Compute the hold that maximizes the expected value when the
    discarded dice are rolled.
    """
    set_hold_die = gen_all_holds(hand)
    res = (0, ([]))
    for item in set_hold_die:
        val = expected_value(item, num_die_sides, len(hand)-len(item))
        if val > res[0]:
            res = (val, item)

    return res


def run_example():
    """
    Compute the dice to hold and expected score for an example hand
    """
    num_die_sides = 6
    hand = (1,)
    hand_score, hold = strategy(hand, num_die_sides)
    print "Best strategy for hand", hand, "is to hold", hold, "with expected score", hand_score
    
if __name__ == "__main__":   

    a = (1,2,2,5)
    print gen_all_holds(a)
    print score(a)
    held = tuple([2,2])
    print expected_value(held, 6, 2)
    run_example()
