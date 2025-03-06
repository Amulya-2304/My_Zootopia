import json


def load_animal_data(filename):
    """Loads animal data from a JSON file."""
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)


def generate_animal_html(animal):
    """Formats animal data as an HTML list item."""
    return (
        f"""
        <li class='cards__item'>
            <div class='card__title'>{animal['name']}</div>
            <div class='card__text'>
                <strong>Diet:</strong> {animal['characteristics'].get('diet', 'Unknown')}<br>
                <strong>Location:</strong> {', '.join(animal['locations'])}<br>
                <strong>Type:</strong> {animal['characteristics'].get('type', 'Unknown')}<br>
            </div>
        </li>
        """
    )


def update_animals_html(input_html, output_html, animal_data):
    """Updates the animals.html file with new animal data."""
    with open(input_html, "r", encoding="utf-8") as file:
        html_content = file.read()

    start_marker = "<ul class=\"cards\">"
    end_marker = "</ul>"
    start_index = html_content.find(start_marker) + len(start_marker)
    end_index = html_content.find(end_marker, start_index)

    animal_html_list = "\n".join(
        generate_animal_html(animal) for animal in animal_data
    )

    new_html_content = (
            html_content[:start_index] + "\n" + animal_html_list + "\n" + html_content[end_index:]
    )

    with open(output_html, "w", encoding="utf-8") as file:
        file.write(new_html_content)


def main():
    """Main function to load data and update the HTML file."""
    animals = load_animal_data("animals_data.json")
    update_animals_html("animals.html", "animals.html", animals)
    print("Updated animals.html successfully!")


if __name__ == "__main__":
    main()