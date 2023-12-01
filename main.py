def day1():
    pass


def process_file(filename):
    with open(filename, 'r') as file:
        # Read the content of the file
        content = file.read()

        # Process the content
        elf_groups = content.strip().split("\n\n")
        total_calories_per_elf = [sum(map(int, group.split('\n'))) for group in elf_groups]
        max_calories = max(total_calories_per_elf)

        return max_calories


# Example usage
max_calories = process_file('day1.txt')
print(f"The Elf carrying the most calories is carrying a total of {max_calories} calories.")

if __name__ == '__main__':
    day1()
