full_dot = '●'
empty_dot = '○'
def create_character(name, STR, INT, CHA):
    if not isinstance(name,str):
        return 'The character name should be a string'
    if name == '':
        return 'The character should have a name'
    if len(name) >10:
        return 'The character name is too long'
    if ' ' in name:
        return 'The character name should not contain spaces'
    if not isinstance(STR, int) or not isinstance(INT, int) or not isinstance(CHA, int):
        return 'All stats should be integers'
    if STR < 1 or INT < 1 or CHA < 1:
        return 'All stats should be no less than 1'
    if STR > 4 or INT > 4 or CHA > 4:
        return 'All stats should be no more than 4'
    if STR+INT+CHA != 7:
        return 'The character should start with 7 points'
    return f'{name}\nSTR {STR*full_dot}{(10-STR)*empty_dot}\nINT {INT*full_dot}{(10-INT)*empty_dot}\nCHA {CHA*full_dot}{(10-CHA)*empty_dot}'
