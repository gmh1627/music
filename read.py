import os

# Get filenames from first directory
vip_path = r"H:\Music\网易云VIP"
vip_files = []
for filename in os.listdir(vip_path):
    name_without_ext = os.path.splitext(filename)[0]
    vip_files.append(name_without_ext)

# Write to first file
with open('vip_songs.txt', 'w', encoding='utf-8') as f:
    for name in vip_files:
        f.write(name + '\n')

# Get filenames from second directory  
no_lyric_path = r"H:\Music\无歌词"
no_lyric_files = []
for filename in os.listdir(no_lyric_path):
    name_without_ext = os.path.splitext(filename)[0]
    no_lyric_files.append(name_without_ext)

# Write to second file
with open('no_lyric_songs.txt', 'w', encoding='utf-8') as f:
    for name in no_lyric_files:
        f.write(name + '\n')

# Compare files
vip_set = set(vip_files)
no_lyric_set = set(no_lyric_files)

print("Songs in VIP but not in No Lyric:")
print(vip_set - no_lyric_set)

print("\nSongs in No Lyric but not in VIP:")
print(no_lyric_set - vip_set)