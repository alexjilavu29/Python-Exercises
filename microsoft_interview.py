# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    pass

    # This method stores each sequence of consequent dominos as a list of its own.

    # The cur variable holds the current domino to be added to the sequence.
    cur = []

    # The sequence variable holds the current found sequence.
    sequence = []

    # The seqs variable holds all the found sequences.
    seqs = []

    # We go through the list 2 by 2 in order to move faster through the dominos.
    for i in range(0, len(A) - 1, 2):

        # We append the current domino values.
        cur.append(A[i])
        cur.append(A[i + 1])

        # The first case is for the beginning of the list.
        if sequence == []:
            sequence.extend(cur)

        # If the current domino fits with the last one in the sequence:
        elif sequence[-1] == cur[0]:
            # We add it to the sequence.
            sequence.append(cur[1])

        # If the current domino does not fit in the sequence:
        elif sequence[-1] != cur[0]:
            # We add the last sequence to the list of sequences.
            seqs.append(sequence)
            # We begin a new sequence.
            sequence = []
            sequence.extend(cur)

        # We reset the current domino.
        cur = []

    # We add the lest found sequence to the list.
    seqs.append(sequence)

    # Afterwords, we tackle each combination of dominos beginning with each sequence in the list.

    # The buffer variable holds the number of dominos eliminated from the left of the current one. We add this variable to avoid unnecessary verifications of invalid combinations.
    buffer = 0

    # The min_out variable holds to minimum number of variables to eliminate from the list.
    min_out = 99999

    # If the buffer is bigger than the minimum number of dominos the eliminate from a previous case, we stop the algorithm.
    while min_out >= buffer:
        # The value to pair with the current domino is stored in the pair variable.
        pair = seqs[0][-1]

        # The cur_pos variable holds the current position discussed.
        cur_pos = 1

        # The out variable counts the number of eliminated dominos.
        out = 0
        # We use an auxiliary list of sequences because we have to eliminate items from it.
        aux = []
        aux.extend(seqs)
        # print(aux)
        while cur_pos < len(aux):
            if aux[cur_pos][0] != pair:
                out += len(aux[cur_pos]) - 1
                aux.pop(cur_pos)

            else:
                pair = aux[cur_pos][-1]
                cur_pos += 1

            # print(aux)

        # If the buffer dominos + the dominos eliminated to the right of the current one is lower than the previous minimum number, we found a better combination.
        if buffer + out < min_out:
            min_out = out + buffer

        # We have to keep in mind that some sequences have bigger numbers of dominos in them.
        buffer += len(seqs[0]) - 1
        seqs.pop(0)

    return min_out





