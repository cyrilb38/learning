# python3

PRIME = 1000000007
X = 263

def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def hash_string(s, prime, x):
    ans = 0
    for c in reversed(s):
        ans = (ans * x + ord(c)) % prime
    return ans

def get_occurrences(pattern, text):
    
    bucket_size = len(text) - len(pattern) + 1
    hash_table = [None for _ in range(bucket_size)]
    
    # first hash of the text (initialization). As usual we start by the end of the text (polynomial hashing)
    hash_table[-1] = hash_string(text[len(text) - len(pattern):], PRIME, X)

    # pre compute the rest of the hashes of the text. 
    # first we calculate y = x ** |P| (we do it in a loop to avoid overflow)
    y = 1
    for _ in range(len(pattern)):
        y = (X * y) % PRIME 

    # then we go through each position of the text to calculate its hash
    for i in range(len(text) - len(pattern) - 1, -1, -1):
        hash_table[i] = (X * hash_table[i+1] + ord(text[i]) - y * ord(text[i + len(pattern)]) ) % PRIME
    
    # calculate the hash of the pattern
    phash = hash_string(pattern, PRIME, X)

    # print(hash_table, phash)

    # now we go through every position of the text to see their hash in hash_table and compare it with phash
    # if they are equal, we compare them
    res = []
    for i in range(len(hash_table)):
         if hash_table[i] == phash:
              if text[i:i+len(pattern)] == pattern:
                   res.append(i)
    
    return res

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

