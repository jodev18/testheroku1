# import time

# file = open('ue_o_muite_arukou.txt')

# lines = file.readlines()

# for lyric in lines:
#     print(lyric)
#     time.sleep(2.5)

write_file = open('atarashii.txt','w')

for x in range(3):
    write_file.write("Something\n")

write_file.flush()
write_file.close()

