def generate_product_html(name, description, image_name,price):
    return f"""
    <div class="product">
        <img src="images/{image_name}" alt="{name}" width="200">
        <h3>{name}</h3>
        <p>{description}</p>
        <p>{price}</p>

    </div>
    """

def add_product_to_html():
    name = input("Enter product name (e.g., Casual T-Shirts): ")
    description = input("Enter description (e.g., Starting at ₹250): ")
    image_name = input("Enter image file name (e.g., tshirt.jpg): ")
    price = int(input("enter the price : "))

    product_html = generate_product_html(name, description, image_name,price)

    with open("products.html", "r", encoding="utf-8") as file:
        content = file.read()

    insert_point = content.rfind("</section>")
    new_content = content[:insert_point] + product_html + content[insert_point:]

    with open("products.html", "w", encoding="utf-8") as file:
        file.write(new_content)

    print(f"Added {name} to products.html!")

if __name__ == "__main__":
    add_product_to_html()