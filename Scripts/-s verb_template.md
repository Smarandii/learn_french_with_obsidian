```python
prem_pers_sing = input('Première personne du singulier: ')
deux_pers_sing = input('Deuxième personne du singulier: ')
troi_pers_sing = input('Troisième personne du singulier: ')
prem_pers_plur = input('Première personne du pluriel: ')
deux_pers_plur = input('Deuxième personne du pluriel: ')
trois_pers_plur = input('Troisième personne du pluriel: ')
participe_passe = input('Particip passe: ')

present = ['### Present Simple:\n',
f'- Première personne du singulier: **je {data}**\n',
f'- Deuxième personne du singulier: **tu {data1}**\n',
f'- Troisième personne du singulier: **il/elle/on {data2.split(" ")[-1]}**\n',
f'- Première personne du pluriel: **nous {data3}**\n',
f'- Deuxième personne du pluriel: **vous {data4}**\n',
f'- Troisième personne du pluriel: **ils/elles {data5.split(" ")[-1]}**\n']

passe_compose = ['### Passé composé (Present perfect)',
f'- Première personne du singulier: **j'ai {participe_passe}**',
f'- Deuxième personne du singulier: **tu as {participe_passe}**',
f'- Troisième personne du singulier: **il/elle/on a {participe_passe}**',
f'- Première personne du pluriel: **nous avons {participe_passe}**',
f'- Deuxième personne du pluriel: **vous avez {participe_passe}**',
f'- Troisième personne du pluriel: **ils/elles ils ont {participe_passe}**']

with open(fr"D:\Media content\Stankin\French_Vault\Verbs\-v {data}.md" , "w") as f:
	f.writelines(template)
```


run with cmd: `python "D:\Media content\Stankin\French_Vault\Scripts\verb_template.py"`