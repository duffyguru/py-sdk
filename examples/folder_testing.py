import guru

# call script with the credentials of the user you want to use
# ex: GURU_USER=user@example.com GURU_TOKEN=abcd1234-abcd-abcd-abcd-abcdabcdabcd python getCardExport.py
email = "mhornak@getguru.com"
token = "0ab65098-43df-42d6-9d22-bf4117f6b163"

g = guru.Guru(email, token, qa=True)

folder = g.get_folder("TEqxqbac")
print("Folder items: %s" % folder.items)

for subfolder in folder.folders:
  print("folder name: %s" % subfolder.title)

for card in folder.cards:
  print("card name: %s" % card.title)
