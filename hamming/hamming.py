def distance(dna1, dna2):
    hamming_list = [a != b for (a,b) in zip(dna1,dna2)]
    return sum(hamming_list)
