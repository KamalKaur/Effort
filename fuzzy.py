
import fuzzy

names = [ 'Catherine', 'Katherine', 'Katarina',
          'Johnathan', 'Jonathan', 'John',
          'Teresa', 'Theresa',
          'Smith', 'Smyth',
          'Jessica',
          'Joshua',
          ]

soundex = fuzzy.Soundex(4)

for n in names:
    print '%-10s' % n, soundex(n)
