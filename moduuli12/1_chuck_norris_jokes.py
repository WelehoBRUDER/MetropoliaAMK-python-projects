import requests

def main():
  chuck_norris_joke = requests.get("https://api.chucknorris.io/jokes/random").json()["value"]
  print(f"Here's a Chuck Norris joke:\n{"-" * 25}")
  print(f"{chuck_norris_joke}\n{"-" * 25}")
  
main()