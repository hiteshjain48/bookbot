def count_char(str):
    chars = {}
    for c in str:
        if c in chars:
            chars[c] = chars[c] + 1
        else:
            chars[c] = 1
    return chars

with open(r'books/frankenstein.txt') as f:
    file_content = f.read()
    file_content = file_content.lower()
    count = count_char(file_content)
    words = file_content.split()

with open(r'report.txt','w') as f:
    f.write("---Report of the file---\n")
    f.write(f"The file has {len(words)} words.\n")
    for char in count:
        if char.isalpha():
            f.write(f"The character '{char}' was found {count[char]} times.\n")
    f.write("---End of Report---\n")