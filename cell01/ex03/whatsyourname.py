def main():
	first_name = input("Hey, what's your first name? : ").strip()
	last_name = input("And your last name? : ").strip()
	greetings = " ".join(["Well, pleased to meet you,", first_name, last_name + "."])
	print(greetings)

if __name__ == "__main__":
	main()