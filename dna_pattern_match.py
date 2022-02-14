# Pattern: AGCTC
# Match: GC
# Match: AGC
# Nonmatch: GG
#
#
# Pattern: AG.TC
# Match: CTC
# Match: GG
# Nonmatch: GGG

def pattern_match(pattern, candidate):
    m_pointer = 0

    for char in pattern:
        if candidate[m_pointer] == char or char == '.':
            m_pointer += 1
        else:
            m_pointer = 0

        if m_pointer == len(candidate):
            return "Match"

    return "Not a match"

