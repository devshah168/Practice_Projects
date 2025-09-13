import pandas 

df = pandas.read_csv("C:/PROJECTS/100 days of python/day26/nato_phonetic_alphabet.csv")
nato_dict={row.letter:row.code for (index,row) in df.iterrows()}
name=input("Enter a name: ").upper()
result=[nato_dict[letter] for letter in name]
print(result)



