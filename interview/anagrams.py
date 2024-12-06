anagrams = ['taste', 'art', 'inlets', 'stressed', 'glean', 'dog', 'feat', 'desserts',
'notes', 'brag', 'below', 'night', 'part', 'care', 'silent', 'tops',
'angle', 'study', 'vase', 'listen', 'earth', 'hater', 'tar', 'god',
'trap', 'angel', 'stop', 'race', 'live', 'state', 'tinsel', 'baker',
'evil', 'iceman', 'grab', 'fate', 'stone', 'elbow', 'break', 'rat', 'cinema']

anagrams_d: dict[str, list[str]] = {}

for n in anagrams:
    sorted_word = ''.join(sorted(list(n)))
    if sorted_word in anagrams_d:
        anagrams_d[sorted_word].append(n)
    else:
        anagrams_d[sorted_word] = [n]

    anagrams_d = {value[0]: value for key, value in anagrams_d.items()}

print(anagrams_d)
