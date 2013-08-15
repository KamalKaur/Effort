import difflib

bart_stations = ['Punjab', 'Mumbai', 'India', 'America',
                 'Delhi','Maharashtra','Harvinder Kaur','Kamaljeet Kaur', 'Ravinder singh',]

while True:
    text = raw_input('Enter BART station: ')
    if not text: break  # Pressing Enter quits
    guess = difflib.get_close_matches(text, bart_stations, n=2, cutoff=0)[0]
    print('Closest match: {g}'.format(g = guess))
