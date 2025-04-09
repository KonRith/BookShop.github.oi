from django.shortcuts import render, get_object_or_404, redirect
from .models import C_Acer, C_Asus, C_Lenovo, C_Mac, C_Mac_A, C_Mac_B, C_Mac_C, C_Msi, Computer
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Removed: from .models import Cart  <-- Because there's no Cart model in your models.py


def get_product_by_slug(slug):
    models_to_check = [Computer, C_Acer, C_Asus, C_Msi, C_Lenovo, C_Mac, C_Mac_A, C_Mac_B, C_Mac_C]
    for model in models_to_check:
        try:
            return model.objects.get(slug=slug)
        except model.DoesNotExist:
            continue
    return None


def add_to_cart(request, slug):
    """
    Add a product to the session-based cart.
    """
    if request.method == 'POST':
        product = get_product_by_slug(slug)
        if not product:
            # Optionally, you can show a message or 404 here
            return redirect('Computer:computer_list')
        
        cart = request.session.get('cart', {})

        if slug in cart:
            cart[slug]['quantity'] += 1
        else:
            cart[slug] = {
                'name': product.name,
                'price': str(product.price),
                'image': product.image,
                'quantity': 1,
            }
        request.session['cart'] = cart

        return redirect(request.META.get('HTTP_REFERER', 'Computer:computer_list'))
    
    return redirect('Computer:computer_list')



def cart_count(request):
    """
    Returns a context dict with the total quantity of items in the session-based cart.
    """
    cart = request.session.get('cart', {})
    total_quantity = sum(item['quantity'] for item in cart.values())
    return {'cart_count': total_quantity}


def cart_detail(request):
    cart = request.session.get('cart', {})
    total_price = 0
    total_quantity = 0
    for slug, item in cart.items():
        total_price += float(item['price']) * item['quantity']
        total_quantity += item['quantity']
    return render(request, 'cart_detail.html', {
        'cart': cart,
        'total_price': total_price,
        'total_quantity': total_quantity,
    })



def update_quantity(request, slug):
    """
    Increase or decrease the quantity of a product in the session-based cart.
    Expects a POST with 'action' = 'increase' or 'action' = 'decrease'.
    """
    if request.method == 'POST':
        action = request.POST.get('action')
        cart = request.session.get('cart', {})

        if slug in cart:
            if action == 'increase':
                cart[slug]['quantity'] += 1
            elif action == 'decrease':
                if cart[slug]['quantity'] > 1:
                    cart[slug]['quantity'] -= 1

        request.session['cart'] = cart

    return redirect('Computer:cart_detail')


def remove_item(request, slug):
    """
    Remove a product entirely from the session-based cart.
    """
    if request.method == 'POST':
        cart = request.session.get('cart', {})
        if slug in cart:
            del cart[slug]
        request.session['cart'] = cart

    return redirect('Computer:cart_detail')


def checkout(request):
    """
    Placeholder for checkout logic (session-based or otherwise).
    """
    return render(request, 'checkout.html')


def search_results(request):
    query = request.GET.get('q', '')
    results = []  # initialize an empty list

    if query:
        # Perform search on each model
        computer_results = Computer.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )
        acer_results = C_Acer.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )
        asus_results = C_Asus.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )
        msi_results = C_Msi.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )
        lenovo_results = C_Lenovo.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )
        mac_results = C_Mac.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )
        mac_a_results = C_Mac_A.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )
        mac_b_results = C_Mac_B.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )
        mac_c_results = C_Mac_C.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )

        # Combine results from all models (convert to list if necessary)
        results = list(computer_results) + list(acer_results) + list(asus_results) + list(msi_results) + \
                  list(lenovo_results) + list(mac_results) + list(mac_a_results) + list(mac_b_results) + list(mac_c_results)

        # Sort the combined list by date_post in descending order
        results.sort(key=lambda item: item.date_post, reverse=True)

    context = {
        'query': query,
        'results': results,
    }
    return render(request, 'search_results.html', context)

def payment(request):
    if request.method == 'POST':
        total_price = request.POST.get('total_price')
        payment_method = request.POST.get('payment_method')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        confirm_checkbox = request.POST.get('confirm_checkbox')
        
        # Capture cart details before clearing
        cart = request.session.get('cart', {})

        # Compute total quantity from the cart items
        total_quantity = sum(item.get('quantity', 0) for item in cart.values())
        
        # Create a dictionary for the payment details along with cart items
        payment_details = {
            'total_price': total_price,
            'payment_method': payment_method,
            'email': email,
            'phone_number': phone_number,
            'items': cart,  # This may include image URLs and other details
            'total_quantity': total_quantity,
            'confirm_checkbox': confirm_checkbox,
        }
        
        # Store the payment details in the session for later use
        request.session['payment_details'] = payment_details
        
        # Clear the cart after payment details are captured
        request.session['cart'] = {}
        
        # Render the payment_details.html template with the payment details context
        return render(request, 'payment_details.html', payment_details)
    
    # For non-POST requests, redirect appropriately (to the checkout page)
    return redirect('Computer:checkout')

def checkout(request):
    """
    Computes the total price, discount, shipping fee, and final amount from the session-based cart,
    then renders the checkout page with these values.
    """
    cart = request.session.get('cart', {})
    total_price = 0.0
    for slug, item in cart.items():
        total_price += float(item['price']) * item['quantity']

    shipping = 1.5
    if total_price >= 200:
        discount = 10
    elif total_price >= 100:
        discount = 5
    else:
        discount = 0

    final_amount = total_price - discount - shipping

    return render(request, 'checkout.html', {
        'cart': cart,
        'total_price': total_price,
        'shipping': shipping,
        'discount': discount,
        'final_amount': final_amount,
    })




# -----------------------------
# Computer listing and detail
# -----------------------------

def computer_list(request):
    computer = Computer.objects.all().order_by('-date_post')
    return render(request, 'Computer/computer_list.html', {'computer_list': computer})

def computer_detail(request, slug):
    product = get_product_by_slug(slug)
    if not product:
        raise Http404("Product not found")
    return render(request, 'Computer/computer_detail.html', {'computer': product})

@login_required(login_url="/users/login/")
def computer_new(request):
    payment_details = request.session.get('payment_details')  # Don't pop it
    return render(request, 'Computer/computer_new.html', {'payment_details': payment_details})



def computer_list_Acer(request):
    computers = C_Acer.objects.all().order_by('-date_post')
    return render(request, 'Computer/computer_list_Acer.html', {'computer_list_Acer': computers})

def computer_detail_Acer(request, slug):
    computer = get_object_or_404(C_Acer, slug=slug)
    return render(request, 'Computer/computer_detail_Acer.html', {'computer': computer})

def computer_list_Asus(request):
    computers = C_Asus.objects.all().order_by('-date_post')
    return render(request, 'Computer/computer_list_Asus.html', {'computer_list_Asus': computers})

def computer_detail_Asus(request, slug):
    computer = get_object_or_404(C_Asus, slug=slug)
    return render(request, 'Computer/computer_detail_Asus.html', {'computer': computer})

def computer_list_Msi(request):
    computers = C_Msi.objects.all().order_by('-date_post')
    return render(request, 'Computer/computer_list_Msi.html', {'computer_list_Msi': computers})

def computer_detail_Msi(request, slug):
    computer = get_object_or_404(C_Msi, slug=slug)
    return render(request, 'Computer/computer_detail_Msi.html', {'computer': computer})

def computer_list_Lenovo(request):
    computers = C_Lenovo.objects.all().order_by('-date_post')
    return render(request, 'Computer/computer_list_Lenovo.html', {'computer_list_Lenovo': computers})

def computer_detail_Lenovo(request, slug):
    computer = get_object_or_404(C_Lenovo, slug=slug)
    return render(request, 'Computer/computer_detail_Lenovo.html', {'computer': computer})

def computer_list_Mac(request):
    computers = C_Mac.objects.all().order_by('-date_post')
    return render(request, 'Computer/computer_list_Mac.html', {'computer_list_Mac': computers})

def computer_detail_Mac(request, slug):
    computer = get_object_or_404(C_Mac, slug=slug)
    return render(request, 'Computer/computer_detail_Mac.html', {'computer': computer})

def computer_list_Mac_A(request):
    computers = C_Mac_A.objects.all().order_by('-date_post')
    return render(request, 'Computer/computer_list_Mac_A.html', {'computer_list_Mac_A': computers})

def computer_detail_Mac_A(request, slug):
    computer = get_object_or_404(C_Mac_A, slug=slug)
    return render(request, 'Computer/computer_detail_Mac_A.html', {'computer': computer})

def computer_list_Mac_B(request):
    computers = C_Mac_B.objects.all().order_by('-date_post')
    return render(request, 'Computer/computer_list_Mac_B.html', {'computer_list_Mac_B': computers})

def computer_detail_Mac_B(request, slug):
    computer = get_object_or_404(C_Mac_B, slug=slug)
    return render(request, 'Computer/computer_detail_Mac_B.html', {'computer': computer})

def computer_list_Mac_C(request):
    computers = C_Mac_C.objects.all().order_by('-date_post')
    return render(request, 'Computer/computer_list_Mac_C.html', {'computer_list_Mac_C': computers})

def computer_detail_Mac_C(request, slug):
    computer = get_object_or_404(C_Mac_C, slug=slug)
    return render(request, 'Computer/computer_detail_Mac_C.html', {'computer': computer})
