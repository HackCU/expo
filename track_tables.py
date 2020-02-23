import pandas as pd


if __name__ == '__main__':
    df = pd.read_csv('data/data.csv')
    tracks_dicts = {
        'General': 'A',
        'All Beginner': 'B',
        'Best UX/UI': 'C',
        'Sustainability': 'D',
        'Social Impact': 'E',
        'Most Random': 'F',
        'Empowering Underrepresented People in Tech': 'G'
    }
    track_nums = {
        'A': 0,
        'B': 0,
        'C': 0,
        'D': 0,
        'E': 0,
        'F': 0,
        'G': 0
    }
    arr = []
    my_dict = {}


    for val in df['tracks'].values:
        letter = tracks_dicts.get(val)
        if letter != None:
            num = track_nums[letter]
            arr.append(f'{letter}{num}')
            track_nums[letter]+=1
        else:
            if val not in my_dict:
                my_dict[val] = 0
            else:
                my_dict[val]+=1
            num = my_dict[val]
            arr.append(f'{val}{num}')
        print(arr)
    df['table'] = arr
    print(len(arr))
    print(df) 
    df.to_csv('data/final.csv')