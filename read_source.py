def get_descs():
    with open('opig_research_src.html', 'r') as f:
        lines = f.read().split('\n')

    name_idx = -10

    desc_dict = {}

    for i, line in enumerate(lines):
        word = '<h4 id='
        if word in line:
            name_idx = i
            idx = line.index(word)
            line = line[idx:]
            start = line.index('>') + 1
            line = line[start:]
            end = line.index('<')
            line = line[:end]
            name = line
        if i == name_idx + 2:
            start = line.index('>') + 1
            line = line[start:]
            desc_dict[name] = line
    return desc_dict
