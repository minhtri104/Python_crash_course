def print_models(unprinted_designs, completed_models):
    """
    Mô phỏng việc in từng thiết kế cho đến khi hết sạch.
    Chuyển từng thiết kế sang completed_models sau khi in.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        # Mô phỏng việc tạo bản in 3D từ thiết kế
        print("Printing model: " + current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Hiển thị tất cả các mô hình đã được in."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)