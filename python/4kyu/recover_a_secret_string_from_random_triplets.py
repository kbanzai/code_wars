# https://www.codewars.com/kata/53f40dff5f9d31b813000774

def recoverSecret(triplets):
    def is_head(alphabet):
        for triplet in triplets:
            if alphabet in triplet[1:]:
                return False
        return True

    alphabets = set([alphabet for triplet in triplets for alphabet in triplet])
    secret = ""
    while alphabets:
        for alphabet in alphabets:
            if is_head(alphabet):
                secret += alphabet
                alphabets.remove(alphabet)
                new_triplets = []
                for triplet in triplets:
                    if alphabet in triplet:
                        triplet.remove(alphabet)
                    new_triplets.append(triplet)
                triplets = new_triplets
                break
    return secret