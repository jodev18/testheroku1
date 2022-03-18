chord_list = ['A','Bb','B','C','C#','D','D#','E','F','F#','G','G#']

def get_chord_transposed(chord,step):
    global chord_list
    current_index = chord_list.index(chord)
    
    transposed_val = current_index + step

    if transposed_val > len(chord_list):
        transposed_val %= len(chord_list)
    return chord_list[transposed_val]


# chord = input('Enter a chord:')
# step = int(input('Steps:'))

# print(get_chord_transposed(chord,step))

str_input = input("Enter series of chords separated by spaces: ")
list_chords = str_input.split(" ")
step = int(input('Steps:'))

for item in list_chords:
    print(get_chord_transposed(item,step),end="\t")
print()

# list_inp_chords = []

# for item in list_inp_chords:
#     print(get_chord_transposed(chord,step))

