def count_vowels(string):
    num_vowels=0
    for char in string:
        if char in "aeiouAEIOU":
           num_vowels = num_vowels+1
    return print('Jumlah huruf hidup adalah : ', num_vowels)

count_vowels('programmer')
