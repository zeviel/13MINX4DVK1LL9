import aminofix
from concurrent.futures import ThreadPoolExecutor
print("""Script by deluvsushi
Github : https://github.com/deluvsushi
╭━━━╮╱╱╱╱╱╱╱╱╱╭━━━╮╱╭╮╱╱╭╮╭━╮╭╮╭╮
┃╭━╮┃╱╱╱╱╱╱╱╱╱┃╭━╮┃╱┃┃╱╱┃┃┃╭╯┃┃┃┃
┃┃╱┃┣╮╭┳┳━╮╭━━┫┃╱┃┣━╯┣╮╭┫╰╯╯╭┫┃┃┃╭━━╮
┃╰━╯┃╰╯┣┫╭╮┫╭╮┃╰━╯┃╭╮┃╰╯┃╭╮┃┣┫┃┃┃┃╭╮┃
┃╭━╮┃┃┃┃┃┃┃┃╰╯┃╭━╮┃╰╯┣╮╭┫┃┃╰┫┃╰┫╰┫╭╮┃
╰╯╱╰┻┻┻┻┻╯╰┻━━┻╯╱╰┻━━╯╰╯╰╯╰━┻┻━┻━┻╯╰╯
""")
client = aminofix.Client()
email = input("-- Email::: ")
password = input("-- Password::: ")
client.login(email=email, password=password)
clients = client.sub_clients(start=0, size=100)
for x, name in enumerate(clients.name, 1):
	print(f"-- {x}:{name}")
com_id = clients.comId[int(input("-- Select the community::: ")) - 1]
sub_client = aminofix.SubClient(comId=com_id, profile=client.profile)

def global_advertise(message: str):
	while True:
		for i in range(0, 250, 20000):
			try:
				online_users = sub_client.get_online_users(start=i, size=100).profile.userId
				print(f"-- Advertising...")
				client.start_chat(userId=online_users, message=message)
				with ThreadPoolExecutor(max_workers=100) as executor:
					[executor.submit(client.start_chat, online_users, message) for user_id in online_users]
			except Exception as e:
				print(e)

global_advertise(message=input("-- Message::: "))
