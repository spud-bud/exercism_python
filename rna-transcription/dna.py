transcription_dict = {'G':'C', 'C':'G', 'T':'A', 'A':'U'}
# def to_rna(dna):
#     result = []
#     for letter in dna:
#         result.append(transcription_dict[letter])
#     return ''.join(result)

def to_rna(dna):
    result = ''
    for letter in dna:
        result += transcription_dict[letter]
    return result
