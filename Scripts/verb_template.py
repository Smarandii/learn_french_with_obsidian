data = input()
data1 = input()
data2 = input()
data3 = input()
data4 = input()
data5 = input()

template = ['### Present Simple:\n',
f'- Première personne du singulier: **je {data}**\n',
f'- Deuxième personne du singulier: **tu {data1}**\n',
f'- Troisième personne du singulier: **il/elle/on {data2.split(" ")[-1]}**\n',
f'- Première personne du pluriel: **nous {data3}**\n',
f'- Deuxième personne du pluriel: **vous {data4}**\n',
f'- Troisième personne du pluriel: **ils/elles {data5.split(" ")[-1]}**\n'] 

with open(fr"D:\Media content\Stankin\French_Vault\Verbs\-v {data}.md" , "w") as f:
	f.writelines(template)
	