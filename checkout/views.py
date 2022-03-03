from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    contexts = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51KZDQBKayx5WrCGtnQntRfE9mwG6IEznA9N9JU3IVKtXejVxwsp7oKuqC6s6zoIRLxgBdIAVsz696UqNPAIjSE9E00gJbIAQUJ',
        'client_secret': 'test client secret',
    }

    return render(request, template, contexts)
