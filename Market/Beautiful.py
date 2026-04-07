# Text colors
def black(text):
    print(f'\033[90m{text}\033[0m')

def green(text):
    print(f'\033[92m{text}\033[0m')

def red(text):
    print(f'\033[91m{text}\033[0m')

def yellow(text):
    print(f'\033[93m{text}\033[0m')

def blue(text):
    print(f'\033[94m{text}\033[0m')

def purple(text):
    print(f'\033[95m{text}\033[0m')

def cyan(text):
    print(f'\033[96m{text}\033[0m')

def white(text):
    print(f'\033[97m{text}\033[0m')


# Background colors
def white_bg(text):
    print(f'\033[100m{text}\033[0m')

def red_bg(text):
    print(f'\033[101m{text}\033[0m')

def green_bg(text):
    print(f'\033[102m{text}\033[0m')

def yellow_bg(text):
    print(f'\033[103m{text}\033[0m')

def blue_bg(text):
    print(f'\033[104m{text}\033[0m')

def purple_bg(text):
    print(f'\033[105m{text}\033[0m')

def cyan_bg(text):
    print(f'\033[106m{text}\033[0m')


def style(text, color=None, bg=None, bold=False, underline=False):
    codes = []

    if bold:
        codes.append('1')
    if underline:
        codes.append('4')
    if color:
        codes.append(f'38;5;{color}')
    if bg:
        codes.append(f'48;5;{bg}')

    code = ';'.join(codes)
    print(f'\033[{code}m{text}\033[0m')



if __name__ == "__main__":
    for i in range(256):
        print(f'\033[38;5;{i}m{i:3}\033[0m', end=' ')
        if i % 16 == 15:
                print()