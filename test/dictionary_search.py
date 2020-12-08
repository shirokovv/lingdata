
with open ('dictionary.tsv') as f:
    for line in f:
        determ = []
        determine = line.split('\t')
        words = determine[1].split()
        if words[0].startswith('\=') or words[0].startswith('\+') or words[0].startswith('<'):
            
            if len(words) >= 2:
                word = words[1]
                
            else:
                word = ''
                
            
        else:
            word = words[0]
        with open ('dictionary_2.tsv', 'a') as f:
            string = determine[0] + '\t' + word.strip(',') + '\n'
            f.write(string)
