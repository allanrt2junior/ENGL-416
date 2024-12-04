def tokenize(sentence):
    # Define a list of delimiters to split the sentence
    delimiters = " .,!?;:\"'()[]{}-"
    # Define a set of common stopwords
    stopwords = {
       "Yaani", "abele","bali", "yase", "tah","ne", "sina","tah","ndala","sai" ,"ne",  
       "ili" ,"ewe" , "sikele" , "oli" ,"omusakhulu","omuleme" ,"nono" , "ese" ,"omuleme", "tah","oli"
       ,"nio" ,"hubela", 
        "ewe","ne" , "mao", "kakosa","sawa" ,"week" , "sisa"
    }
    
    tokens = []
    word = ""
    
    for char in sentence:
        if char in delimiters:
            if word:  # If there's a word accumulated, check for stopword
                if word.lower() not in stopwords:  # Convert word to lowercase and check
                    tokens.append(word)
                word = ""
        else:
            word += char  # Build the word character by character
    
    if word and word.lower() not in stopwords:  # Add the last word if it's not a stopword
        tokens.append(word)
    
    return tokens

# input a sentence
sentence = "Yaani khane abele bahakhuelesela bali amenyile hubelabembiko yase tah,reba mao sina nendi ne butekhele ,merebe akhubolele sina neekhahuesanga eraba tah, sikila sohuna lilisi online embiko ndala tah,nakhuila esikuli narunga chisendi ,wamwene wanywa enchaka yakhubea walekha chisendi esikuli,walekha khusoma ,sai heungatala mumonichase,Nafunangavavacado ne nkusia ili ewe osome ,ata nama khumusalachana  nakwa nafunikha sikele ,sai unanga else oli omusakhulu omuleme ,nono ,nokhobona oli ese omuleme tah,oli nasalwa niende kumutambotah,nio khobona nakosa khukusia kumkunda hubela ewe,ne khobona oli mao kakosa khubeela khwise tah,sawa ,week ahukholele sisa"


# Using tokenize function
tokens = tokenize(sentence)

# Using split method (splits based on spaces, no stopword removal)
split_words = sentence.split()

# Print both outputs


print("stemmed sentence")
print(split_words)
print(" ")
print("Tokenised sentence")
print(tokens)
